"""STANDARD INTERPRETER for the V-WEB ISA"""

import struct

class State:
  def __init__(self):
    self.R0 = bytearray(8)
    self.R1 = bytearray(8)
    self.R2 = bytearray(8)
    self.R3 = bytearray(8)
    self.R4 = bytearray(8)
    self.R5 = bytearray(8)
    self.R6 = bytearray(8)
    self.R7 = bytearray(8)
    self.R8 = bytearray(8)
    self.R9 = bytearray(8)
    self.R10 = bytearray(8)
    self.R11 = bytearray(8)
    self.R12 = bytearray(8)
    self.R13 = bytearray(8)
    self.R14 = bytearray(8)
    self.R15 = bytearray(8)
    self.R16 = bytearray(8)
    self.R17 = bytearray(8)
    self.R18 = bytearray(8)
    self.R19 = bytearray(8)
    self.R20 = bytearray(8)
    self.R21 = bytearray(8)
    self.R22 = bytearray(8)
    self.R23 = bytearray(8)
    self.R24 = bytearray(8)
    self.R25 = bytearray(8)
    self.R26 = bytearray(8)
    self.R27 = bytearray(8)
    self.R28 = bytearray(8)
    self.R29 = bytearray(8)
    self.R30 = bytearray(8)
    self.R31 = bytearray(8)
    self.PC = bytearray(8)
    self.MEMORY = bytearray(0)

  def step(self):
    instruction = struct.unpack_from('>I', self.MEMORY, offset=self.PC*4)[0]
    base_opcode = instruction >> 28
    sub_opcode = ((instruction >> 24) && 0xF0) >> 4
    destination = ((instruction >> 20) && 0xF00) >> 8
    
    
