## Xilinx Command Line FPGA Tools

This tool set consists of a Makefile to build
a bitstream and SVF boundary scan file and an
Arduino-like and computer program to program
them.

# FPGA Makefile

The FPGA Makefile in `FPGAMake` need:
- A project file `TopLevel.prj` containing library-associated sources path
- A user constraint file `TopLevel.prj` with locations and timing constraints
- A extra XST directive file `TopLevel.prj` (in doubt leave empty)
- A `build` directory
- A `src` directory (with sources)

After this simply type `make` and the bitstream and SVF files are
generated inside build from VHDL and Verilog sources using the Xilinx
ISE toolchain.

Remember to check `Makefile` to adapt the toolchain path to your installation!

# JTAG Programmer

Inside `JTAGProg` you find both the Arduino-like project (configurable)
and the Computer program to send SVF files to the boards.
The software should work on all OSs supporting Python3 (and pyserial).

Remember to install python dependencies with `pyInstallDep.sh`.

If you are a developer and want to edit the parser `SVF.g4` use
`buildtools.sh` to download the parser compiler and `buildParser.sh SVF.g4`
to compile it overwiting `SVF*.py` files.

## License

Author: Dario Fagotto, 2019

This program is released under [**Attribution 4.0 International (CC BY 4.0)**](https://creativecommons.org/licenses/by/4.0/)
you are free to share this software and use it also for commercial products as
long as you give attribution to the author and link the original material.
