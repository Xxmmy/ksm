#!/usr/bin/env python3.2
# Mark executable sections as non-pagable, this is necessary because VMX root mode runs
# with interrupts off, so all pages must be physically contiguous.
# This file is only for the MinGW build!
import sys
try:
    import pefile
except:
    print "Please install pefile before running this script."

pe = pefile.PE(sys.argv[1])
for section in pe.sections:
    if ".text" in section.Name:
        section.Characteristics |= 0x68000000

pe.write(sys.argv[1])

