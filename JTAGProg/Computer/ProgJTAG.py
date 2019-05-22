#! /usr/bin/env python3

#
# JTAG programmer using Arduino (computer script)
#   Dario Fagotto, 2019
#
# Version 1.0
#
#   Based on https://github.com/mattdibi/Programmatore-JTAG-per-Xilinx/blob/master/JTAG/JTAG.ino
#     by Mattia Dal Ben
#     by Mattia Marson
#     by Manuel Guglielmini
#
#   Extended command set:
#     *!       -> tms bit
#     .,       -> tdi bit
#     [0-9a-f] -> tdi nibble (sent LSB first)
#     :;       -> tdi end bit
#     <>       -> start and stop tdo output
#     #        -> sync and flush
#

#
# Known bugs:
#   - Readback operations (containing TDO) are limited by
#     the serial buffer since the write is done before
#     reading
#   - Does not handle trailer or headers (but aborts,
#     if they are not empty)
#   - Not exactly a bug, but antlr4 is slow-ish, parse
#     directly next time or find why...
#

from antlr4 import *
from SVFLexer import SVFLexer
from SVFListener import SVFListener
from SVFParser import SVFParser

from serial import Serial

# 5us between edges and 115200 -> time = 85s
# 2us between edges and 230400 -> time = 62s
# 1us between edges and 500000 -> time = 53s /* BEST */
# only digitalWrite delay between edges and 500000 -> time = 44s
# only digitalWrite delay between edges and 500000 -> time = 44s

# Tested on Arduino DUE

def strHexMask(c, mask):
	return hex(int(c, 16) & int(mask, 16))[2:]

def strHexCheck(s1, s2, mask):
	l = len(s1)	
	if(l != len(s2) or l != len(mask)):
		return False
	for i in range(l):
		if(strHexMask(s1[i], mask[i]) != strHexMask(s2[i], mask[i])):
			return False
	return True

class ProgramSVFListener(SVFListener):
	BLOCK_SIZE = 50000
	def __init__(self, serial):
		self.serial = serial
	def exitStateCmd(self, ctx):
		if(ctx.name == 'STATE'):
			print('New state: {}'.format(ctx.state))
			if(ctx.state == 'RESET'):
				self.serial.write(b'!!!!!*')
			elif(ctx.state == 'IDLE'):
				self.serial.write(b'*')
			else:
				print('Unknown state: {}'.format(ctx.state))
	def exitRuntestCmd(self, ctx):
		nNibbles = (ctx.ticks + 3) // 4
		print('Running for {} ticks'.format(nNibbles * 4))
		self.serial.write(b'0' * nNibbles)
	def exitDataCmd(self, ctx):
		if(ctx.name == 'SIR'):
			self.serial.write(b'!!**')
		elif(ctx.name == 'SDR'):
			self.serial.write(b'!*')
		else:
			if(ctx.len > 0):
				raise Exception('Unhandled non-empty directive: {}'.format(ctx.name))
			return # Discard non active commands
		print('Writing {} bit(s) on {}'.format(ctx.len, ctx.name))
		if(ctx.len > 0):
			nNibbles = (ctx.len - 1) // 4
			nBits = (ctx.len - 1) % 4 + 1
			data = ctx.attrs['TDI'][::-1]
			doCheck = 'TDO' in ctx.attrs
			if(doCheck):
				# This solves a bug in iMPACT (Xilinx)
				# where the `program` output checks the
				# `idcode` without masking the version
				doCheck = 'MASK' in ctx.attrs
				if(not doCheck):
					print('\tUnmasked check request ignored')
			if(doCheck):
				self.serial.write(b'<')
			#self.serial.write(data[:nNibbles].encode('ASCII'))
			for i in range(0, nNibbles, self.BLOCK_SIZE):
				iend = min(i + self.BLOCK_SIZE, nNibbles)
				self.serial.write(data[i:iend].encode('ASCII'))
				print('\t{:.2f}%'.format(100 * iend / nNibbles))
			data = int(data[-1], 16)
			for i in range(nBits - 1):
				self.serial.write((data & 1) and b',' or b'.')
				data >>= 1
			self.serial.write((data & 1) and b';' or b':')
			if(doCheck):
				self.serial.write(b'>#');
				resp = self.serial.read_until(b'#')[:-1]
				resp = resp.decode("ASCII")[::-1]
				respVal = 0
				for i in range(nBits):
					respVal <<= 1
					if(resp[i] == ','):
						respVal |= 1
				resp = hex(respVal)[2:] + resp[nBits:]
				expResp = ctx.attrs['TDO']
				mask = ('MASK' in ctx.attrs) and ctx.attrs['MASK'] or (hex(2**nBits - 1)[2:] + 'f' * nNibbles)
				if(not strHexCheck(resp, expResp, mask)):
					raise Exception('Check failed: found 0x{} while expecting 0x{} (with mask 0x{})'.format(resp, expResp, mask))
				print('Readback successful')
		self.serial.write(b'!*')

def main(args):
	if(args is None):
		from argparse import ArgumentParser
		argp = ArgumentParser(description = 'Program an SVF file with Arduino')
		argp.add_argument('-p', '--port', required = True, help = 'Serial port to use')
		argp.add_argument('-B', '--baud', default = 500000, help = 'Serial baud rate')
		argp.add_argument('svf', help = 'SVF file to load')
		args = argp.parse_args()
	
	print('Reading and parsing SVF file...')
	lex = SVFLexer(FileStream(args.svf))
	tstr = CommonTokenStream(lex)
	pars = SVFParser(tstr)
	tr = pars.svf()
	
	print('Opening serial comunication...')
	with Serial(args.port, args.baud) as ser:
		psvf = ProgramSVFListener(ser)
		w = ParseTreeWalker()
		w.walk(psvf, tr)

if(__name__ == '__main__'):
	main(None)
