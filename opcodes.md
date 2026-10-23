This document inherits all definitions from [virtual cpu.md](/virtual+cpu.md).
<!-- Status: Base is done -->

# Details
* In [Opcodes](#opcodes) any reference to Register Source, Register Destination, Register A or Register B shall be interpreted according to the Instruction Ordering Type and the numerical values corresponding to the registers: 0x00 = Register R0 till 0x1F = Register R31.
* ALL values are loaded or stored in big-endian.
* ANY store deletes all the information in the Register it is applied to.
* BOTH Base Opcode AND Sub Opcode MUST match what is written in the table for it to be that exact instruction.
* ANY getting / setting in the Memory is of the size of 64 bits with the exception of M_RSTORE32, M_RSTORE16, M_RSTORE8, M_RLOAD32, M_RLOAD16 and M_RLOAD8.
* ANY getting / setting in the Memory ranges from specified Location till +64 bits or +specified size.

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

## Quadruple Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 13 (5 bits) | Bits 12 till 8 (5 bits) | Bits 7 till 3 (5 bits) | Bits 2 till 0 (3 bits) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Register A | Register B | Register C | No Purpose |

## Single Register, Immediate
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 0 (18 bits) |
| :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Value A |

## Single Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 0 (18 bits) |
| :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | No purpose |

## Immediate
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 0 (23 bits) |
| :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Value A |

# Opcodes

| Opcode Mnemoic | Ordering Type | Base Opcode (binary) | Sub Opcode (binary) | Description |
| :-: | :-: | :-: | :-: | :-: |
| M_RMOVE | Double Register | 0000 | 0000 | Copies the value of Register Source into Register Destination |
| M_RLOAD | Double Register | 0000 | 0001 | Copies from Memory at the value of Register Source into Register Destination |
| M_RSTORE | Double Register | 0000 | 0010 | Copies Register Source into Memory at the value of Register Destination |
| AM_IORLOAD | Double Register, Immediate | 0000 | 00011 | Copies from Memory at the value of unsigned Register A + unsigned Value B into Register Destination |
| AM_IORSTORE | Double Register, Immediate | 0000 | 0100 | Copies the value of Register Destination into memory at the value of unsigned Register A + unsigned Value B |
| M_LILOAD | Single Register, Immediate | 0000 | 0101 | Copies Value A into lower 18 bits of Register Destination |
| AM_LISLOAD | Single Register, Immediate | 0000 | 0110 | Shifts Register Destination to the left by 18 and copies Value A into the lower 18 bits of Register Destination |
| M_SWP | Double Register | 0000 | 0111 | Swaps the value of Register Source and Register Destination |
| M_PUSH | Single Register | 0000 | 1000 | Copies the value of Register Destination to Memory at the Value of SP and increments SP by 8 |
| M_POP | Single Register | 0000 | 1001 | Copies the value in Memory at the Value of SP into Register Destination and decrements SP by 8 |
| M_RSTORE32 | Double Register | 0000 | 1010 | Copies the lower 32 bits of Register Source into Memory at the location of Register Destination |
| M_RSTORE16 | Double Register | 0000 | 1011 | Copies the lower 16 bits of Register Source into Memory at the location of Register Destination |
| M_RSTORE8 | Double Register | 0000 | 1100 | Copies the lower 8 bits of Register Source into Memory at the location of Register Destination |
| M_RLOAD32 | Double Register | 0000 | 1101 | Copies 32 bits from Memory at the location of Register Destination into Register Source |
| M_RLOAD16 | Double Register | 0000 | 1110 | Copies 16 bits from Memory at the location of Register Destination into Register Source |
| M_RLOAD8 | Double Register | 0000 | 1111 | Copies 8 bits from Memory at the location of Register Destination into Register Source |
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
| A_SADDS | Triple Register | 0010 | 0111 | Adds signed Register A using Two's Complement and signed Register B using Two's Complement and stores the lower 64 bits of the result in Register Destination, if the result is larger than 2^32, then it stores 0x7FFFFFFFFFFFFFFF in Register Destination, if it is less than 2^-32, then it stores 0xFFFFFFFFFFFFFFFF in Register Destination |
| A_SUBS | Triple Register | 0010 | 1000 | Subtracts unsigned Register B from unsigned Register A and stores the lower 64 bits of the result in Register Destination, if the result is less than 0, then it stores 0x0000000000000000 in Register Destination |
| A_SSUBS | Triple Register | 0010 | 1001 | Subtracts signed Register B using Two's Complement from signed Register A using Two's Complement and stores the lower 64 bits of the result in Register Destination, if the result is larger than 2^32, then it stores 0x7FFFFFFFFFFFFFFF in Register Destination, if it is less than 2^-32, then it stores 0xFFFFFFFFFFFFFFFF in Register Destination  |
| A_FMA | Qaudruple Register | 0010 | 1010 | Multiplies Register A and B and adds Register C to the result, then stores the final result in Register Destination |
| A_UMIN | Triple Register | 0010 | 1011 | Stores unsigned Register A or unsigned Register B in Register Destination based on which is the smallest |
| A_SMIN | Triple Register | 0010 | 1100 | Stores signed Register A using Two's Complement or signed Register B using Two's Complement in Register Destination based on which is the smallest |
| A_UMAX | Triple Register | 0010 | 1101 | Stores unsigned Register A or unsigned Register B in Register Destination based on which is the largest |
| A_SMAX | Triple Register | 0010 | 1110 | Stores signed Register A using Two's Complement or signed Register B using Two's Complement in Register Destination based on which is the largest |
| A_SEL | Qaudruple Register | 0010 | 1111 | Stores Register A in Register Destination if Register C is 0x00, else it stores Register B in Register Destination |
| A_ABS | Double Register | 0011 | 0000 | Stores the positive value of Register A in Register Destination, behaviour is equal to doing AND 0x7FFFFFFFFFFFFFFF on Register A |
| A_UCLAMP | Quadruple Register | 0011 | 0001 | Stores unsigned Register A in Register Destination. If unsigned Register A is larger than unsigned Register B, it stores Register B in Register Destination. Else if unsigned Register A is smaller than unsigned Register C, it stores Register C in Register Destination. |
| A_SCLAMP | Quadruple Register | 0011 | 0010 | Stores signed Register A using Two's Complement in Register Destination. If signed Register A using Two's Complement is larger than signed Register B using Two's Complement, it stores Register B in Register Destination. Else if signed Register A using Two's Complement is smaller than signed Register C using Two's Complement, it stores Register C in Register Destination. |
| A_UAVG | Triple Register | 0011 | 0011 | Adds unsigned Register A and unsigned Register B and divides the result by 2, then stores the final result in Register Destination. |
| A_SAVG | Triple Register | 0011 | 0100 | Adds signed Register A using Two's Complement and signed Register B using Two's Complement and divides the result by 2, then stores the final result in Register Destination. |
| A_CLZ | Double Register | 0011 | 0101 | Computes exactly how much 0 (binary) 's are from the most significant bit till the most significant 1 (binary) in Register A and stores the result in Register Destination. If Register A  is zero, it stores 32 in Register Destination. Else if Register A is 0xFFFFFFFFFFFFFFFF it stores 0 in Register Destination |
| A_CTZ | Double Register | 0011 | 0110 | Computes exactly how much 0 (binary) 's are from the least significant bit till the least significant 1 (binary) in Register A and stores the result in Register Destination. If Register A is zero, it stores 32 in Register Destination. Else if Register A is 0xFFFFFFFFFFFFFFFF it stores 0 in Register Destination |
| A_PBE | Triple Register | 0011 | 0111 | Takes all the bits from Register A where the corresponding bit of Register B is 1 and packs all the combined bits to the least significant portion maintaining the original order of the bits from Register A and stores the result in Register Destination |
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
| J_LOOP | Single Register, Immediate | 0100 | 0111 | Repeats the instruction of PC till Register Destination, value A amount of times, then exits at Register Destination |
| J_CALL | Immediate | 0100 | 1000 | Pushes the PC to the stack (-> Instruction M_PUSH) and adds Value A to the PC and stores the result in the PC |
| J_RET | Immediate | 0100 | 1001 | Pops a value from the stack (-> Instruction M_POP) and stores the result in PC |
| - | - | - | - | - |
| B_REQ | Triple Register | 0101 | 0000 | Checks if Register A and Register B are equal, if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RULT | Triple Register | 0101 | 0001 | Checks if unsigned Register A is less than unsigned Register B,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RUGT | Triple Register | 0101 | 0010 | Checks if unsigned Register A is greater than unsigned Register B,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RULE | Triple Register | 0101 | 0011 | Checks if unsigned Register A is less than or equal to unsigned Register B,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RUGE | Triple Register | 0101 | 0100 | Checks if unsigned Register A is greater than or equal to unsigned Register B, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSLT | Triple Register | 0101 | 0101 | Checks if signed Register An using Two's Complement is less than signed Register B using Two's Complement, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSGT | Triple Register | 0101 | 0110 | Checks if signed Register A using Two's Complement is greater than signed Register B using Two's Complement, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSLE | Triple Register | 0101 | 0101 | Checks if signed Register A using Two's Complement is less than or equal to signed Register B using Two's Complement, i if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| B_RSGE | Triple Register | 0101 | 0110 | Checks if signed Register A using Two's Complement is greater than or equal to signed Register B using Two's Complement,  if so it stores 0x0000000000000001 in Register Destination, else it stores 0x0000000000000000 in Register Destination |
| - | - | - | - | - |
| F_SCNB512 | Double Register | 0110 | 0000 | Increments Register Destination until the value in Memory at Register Destination matches Register Source or Register Destination is +512 from the original value |
| F_SCNB4K | Double Register | 0110 | 0001 | Increments Register Destination until the value in Memory at Register Destination matches Register Source or Register Destination is +4096 from the original value |
| F_SCNB262K | Double Register | 0110 | 0010 | Increments Register Destination until the value in Memory at Register Destination matches Register Source or Register Destination is +262144 from the original value |
| F_SCNB2M | Double Register | 0110 | 0011 | Increments Register Destination until the value in Memory at Register Destination matches Register Source or Register Destination is +2097152 from the original value |
| F_SCNB268M | Double Register | 0110 | 0100 | Increments Register Destination until the value in Memory at Register Destination matches Register Source or Register Destination is +268435456 from the original value |
| F_NOP | None | 0110 | 0101 | Does nothing |
| F_HOSTCALL | Immediate | 0110 | 0101 | Behavior specified in [hostcall.md](/hostcall.md) |
