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

## Immediate
## Single Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 0 (23 bits) |
| :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Value A |

# Opcodes

ALL values are loaded or stored in big-endian.
| Opcode Mnemoic | [Ordering Type](#instruction-ordering-types) | Base Opcode (binary) | Sub Opcode (binary) | Description |
| :-: | :-: | :-: | :-: | :-: |
| M_MOVE | Double Register | 0000 | 0000 | Copies the value Register Source into Register Destination |
| M_RLOAD | Double Register | 0000 | 0001 | Copies from Memory at the value of Register Source into Register Destination |
| M_LILOAD | Single Register, Immediate | 0000 | 0010 | Copies Value A into lower 18 bits of Register Destination |
| M_RSTORE | Double Register | 0000 | 0011 | Copies Register Source into Memory at the value of Register Destination |
| AM_LISLOAD | Single Register, Immediate | 0000 | 0100 | Shifts Register Destination to the left by 18 and copies Value A into the lower 18 bits of Register Destination |
| M_SWP | Double Register | 0000 | 0101 | Swaps the value of Register Source and Register Destination |
| - | - | - | - | - |
| A_UADD | Triple Register | 0001 | 0000 | Adds the value of Register A and Register B as unsigned values and stores the lower 64 bits of the result in Register Destination |
| A_SADD | Triple Register | 0001 | 0001 | Adds the value of Register A and Register B as signed values using Two's complement and stores the lower 64 bits of the result in Register Destination |
| A_SUB | Triple Register | 0001 | 0010 | Subtracts the value of Register B from the value of Register A as signed values using Two's complement and stores the lower 64 bits of the result in Register Destination|
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
| A_BSR | Triple Register | 0001 | 1010 | Logically shifts the value of Register A by the value of Register B amount of times to the right and stores the result in Register Destination |
| A_IBSR | Double Register, Immediate | 0001 | 1011 | Logically shifts the value of Register A by value B amount of times to the right and stores the result in Register Destination |
| A_SBSL | Triple Register | 0001 | 1100 | Shifts the value of Register A by the value of Register B amount of times to the left ignoring the upper bit and stores the result in Register Destination |
| A_SIBSL | Double Register, Immediate | 0001 | 1101 | Shifts the value of Register A by value B amount of times to the left ignoring the upper bit and stores the result in Register Destination |
| A_SBSR | Triple Register | 0001 | 1110 | Shifts the value of Register A by the value of Register B amount of times to the right ignoring the upper bit and stores the result in Register Destination |
| A_SIBSR | Double Register, Immediate | 0001 | 1111 | Shifts the value of Register A by value B amount of times to the right ignoring the upper bit and stores the result in Register Destination |
| A_OR | Triple Register | 0010 | 0000 | Computes the bitwise OR of Register A and Register B and stores the result in Register Destination |
| A_AND | Triple Register | 0010 | 0001 | Computes the bitwise AND of Register A and Register B and stores the result in Register Destination |
| A_XOR | Triple Register | 0010 | 0010 | Computes the bitwise XOR of Register A and Register B and stores the result in Register Destination |
| A_NOR | Triple Register | 0010 | 0011 | Computes the bitwise NOR of Register A and Register B and stores the result in Register Destination |
| A_NAND | Triple Register | 0010 | 0100 | Computes the bitwise NAND of Register A and Register B and stores the result in Register Destination |
| A_XNOR | Triple Register | 0010 | 0101 | Computes the bitwise XNOR of Register A and Register B and stores the result in Register Destination |
| A_ADDS | Triple Register | 0010 | 0110 | Adds unsigned Register A and unsigned Register B and stores the lower 64 bits of the result in Register Destination, if the result is larger than 2^64, then it stores 0xFFFFFFFFFFFFFFFF in Register Destination |
| A_SUBS | Triple Register | 0010 | 0111 | Subtracts unsigned Register B from unsigned Register A and stores the lower 64 bits of the result in Register Destination, if the result is less than 0, then it stores 0x0000000000000000 in Register Destination |
| - | - | - | - | - |
| J_REQ | Double Register, Immediate | 0100 | 0000 | Checks if Register Destination and Register A are eqaul, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RULT | Double Register, Immediate | 0100 | 0001 | Checks if unsigned Register Destination is less than unsigned Register A, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RUGT | Double Register, Immediate | 0100 | 0010 | Checks if unsigned Register Destination is greater than unsigned Register A, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RULE | Double Register, Immediate | 0010 | 0011 | Checks if unsigned Register Destination is less than or equal to unsigned Register A, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RUGE | Double Register, Immediate | 0010 | 0100 | Checks if unsigned Register Destination is greater than or equal to unsigned Register A, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RSLT | Double Register, Immediate | 0100 | 0101 | Checks if signed Register Destination using Two's Complement is less than signed Register A using Two's Complement, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RSGT | Double Register, Immediate | 0100 | 0110 | Checks if signed Register Destination using Two's Complement is greater than signed Register A using Two's Complement, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RSLE | Double Register, Immediate | 0100 | 0101 | Checks if signed Register Destination using Two's Complement is less than or equal to signed Register A using Two's Complement, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| J_RSGE | Double Register, Immediate | 0100 | 0110 | Checks if signed Register Destination using Two's Complement is greater than or equal to signed Register A using Two's Complement, if so it adds Value B as a signed number using Two's Complement to PC and stores the result in PC, else it does nothing |
| - | - | - | - | - |eqaul
| B_REQ | Triple Register | 0101 | 0000 | Checks if Register A and Register B are equal, if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RULT | Triple Register | 0101 | 0001 | Checks if unsigned Register A is less than unsigned Register B,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RUGT | Triple Register | 0101 | 0010 | Checks if unsigned Register A is greater than unsigned Register B,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RULE | Triple Register | 0101 | 0011 | Checks if unsigned Register A is less than or equal to unsigned Register B,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RUGE | Triple Register | 0101 | 0100 | Checks if unsigned Register A is greater than or equal to unsigned Register B, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSLT | Triple Register | 0101 | 0101 | Checks if signed Register An using Two's Complement is less than signed Register B using Two's Complement, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSGT | Triple Register | 0101 | 0110 | Checks if signed Register A using Two's Complement is greater than signed Register B using Two's Complement, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSLE | Triple Register | 0101 | 0101 | Checks if signed Register A using Two's Complement is less than or equal to signed Register B using Two's Complement, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSGE | Triple Register | 0101 | 0110 | Checks if signed Register A using Two's Complement is greater than or equal to signed Register B using Two's Complement,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
