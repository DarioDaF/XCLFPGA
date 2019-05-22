#
# Xilinx FPGA main makefile
#   Dario Fagotto, 2019
#
# Version: 2.1
#

# Project variables

export TL_NAME := TopLevel
export FPGA_PART := xc6slx16-ftg256

# ISE toolchain

export ISE_BIN := /opt/Xilinx/12.1/ISE_DS/ISE/bin/lin64

# Extra flags

export EXTRA := -intstyle silent

# Makefile bootstrap

all: build

build: build/Makefile
	@$(MAKE) -C build

build/Makefile: Makefile.build
	cp $^ $@

clean:
	-rm -R build/*

.PHONY: all build clean
