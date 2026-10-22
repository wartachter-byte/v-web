This document inherits all definitions from [virtual cpu.md](/virtual+cpu.md).

#wip

# Register as Number
In [Opcodes](#opcodes) any reference to Register Source, Register Destination, Register A or Register B shall be interpreted according to the Instruction Ordering Type and the numerical values corresponding to the registers: 0x00 = Register R0 till 0x1F = Register R31.

# Instruction Ordering Types

## Double Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 13 (5 bits) | Bits 12 till 0 (13 bits) |
| :-: | :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Register Source | No purpose |

## Double Register, Immediate
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 13 (5 bits) | Bits 12 till 0 (13 bits) |
| :-: | :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Register A | Value B |

## Triple Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 13 (5 bits) | Bits 12 till 8 (5 bits) | Bits 7 till 0 (8 bits) |
| :-: | :-: | :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Register A | Register B | No purpose |

## Single Register, Immediate
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 0 (18 bits) |
| :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Value A |

## Single Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 0 (18 bits) |
| :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | No purpose |

# Opcodes

ALL values are loaded or stored in big-endian.
| Opcode Mnemoic | [Ordering Type](#instruction-ordering-types) | Base Opcode (binary) | Sub Opcode (binary) | Description |
| :-: | :-: | :-: | :-: | :-: |
| M_MOVE | Double Register | 0000 | 0000 | Copies Register Source into Register Destination |
| M_RLOAD | Double Register | 0000 | 0001 | Copies from Memory at the value of Register Source into Register Destination |
| M_LILOAD | Single Register, Immediate | 0000 | 0010 | Copies Value A into lower 18 bits of Register Destination |
| M_RSTORE | Double Register | 0000 | 0011 | Copies Register Source into Memory at the value of Register Destination |
| AM_LISLOAD | Single Register, Immediate | 0000 | 0100 | Shifts Register Destination to the left by 18 and copies Value A into the lower 18 bits of Register Destination |
| M_SWP | Double Register | 0000 | 0101 | Swaps the value of Register Source and Register Destination |
| A_UADD | Triple Register | 0001 | 0000 | Adds the value of Register A and Register B as unsigned values and stores the result in Register Destination truncated to 64 bits |
| A_SADD | Triple Register | 0001 | 0001 | Adds the value of Register A and Register B as signed values using Two's complement and stores the result in Register Destination truncated to 64 bits |
| A_SUB | Triple Register | 0001 | 0010 | Subtracts the value of Register B from the value of Register A as signed values using Two's complement and stores the result in Register Destination truncated to 64 bits |
| A_UMULH | Triple Register | 0001 | 0011 | Multiplies the value of Register A and Register B as unsigned values and stores the upper 64 bits of the result in Register Destination |
| A_UMULL | Triple Register | 0001 | 0100 | Multiplies the value of Register A and Register B as unsigned values and stores the lower 64 bits of the result in Register Destination |
| A_SMULH | Triple Register | 0001 | 0011 | Multiplies the value of Register A and Register B as signed values using Two's Complement and stores the upper 64 bits of the result in Register Destination |
| A_SMULL | Triple Register | 0001 | 0100 | Multiplies the value of Register A and Register B as signed values using Two's Complement and stores the lower 64 bits of the result in Register Destination |
| A_UDIV | Triple Register | 0001 | 0101 | Divides the value of Register A by Register B as unsigned values and stores the lower 64 bits of the result in Register Destination. if the value of Register B is eqaul to 0, the highest possible value is instead stored in Register Destination |
| A_SDIV | Triple Register | 0001 | 0110 | Divides the value of Register A by Register B as signed values using Two's Complement and stores the lower 64 bits of the result in Register Destination. if the value of Register B is eqaul to 0, the highest possible value is instead stored in Register Destination |
| A_UMOD | Triple Register | 0001 | 0111 | Divides the value of Register A by Register B as unsigned values and stores the lower 64 bits of the remainder in Register Destination. if the value of Register B is eqaul to 0, the highest possible value is instead stored in Register Destination |
| A_SMOD | Triple Register | 0001 | 0111 | Divides the value of Register A by Register B as signed values using Two's Complement and stores the lower 64 bits of the remainder in Register Destination. if the value of Register B is eqaul to 0, the highest possible value is instead stored in Register Destination |
| A_BSL | Triple Register | 0001 | 1000 | Shifts the value of Register A by the value of Register B amount of times to the left and stores the result in Register Destination |
| A_IBSL | Double Register, Immediate | 0001 | 1001 | Shifts the value of Register A by value B amount of times to the left and stores the result in Register Destination |
| A_BSR | Triple Register | 0001 | 1010 | Shifts the value of Register A by the value of Register B amount of times to the right and stores the result in Register Destination |
| A_IBSR | Double Register, Immediate | 0001 | 1011 | Shifts the value of Register A by value B amount of times to the right and stores the result in Register Destination |
