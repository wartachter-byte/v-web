This document inherits all definitions from [virtual cpu.md](/virtual+cpu.md).

#wip



# Instruction Ordering Types

## Double Register
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 13 (5 bits) | Bits 12 till 0 (13 bits) |
| :-: | :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Register Source | No purpose |

## Double Register, Immediate
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 13 (5 bits) | Bits 12 till 0 (13 bits) |
| :-: | :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Register A | Value B |

## Single Register, Immediate
| Bit 31 till 28 (4 bits) | Bits 27 till 23 (4 bits) | Bits 22 till 18 (5 bits) | Bits 17 till 0 (18 bits) |
| :-: | :-: | :-: | :-: |
| Base Opcode | Sub Opcode | Register Destination | Value A |

| Opcode Mnemoic | [Ordering Type](#instruction-ordering-types) | Base Opcode (binary) | Sub Opcode (binary) | Description |
| :-: | :-: | :-: | :-: | :-: |
| M_MOVE | Double Register | 0000 | 0000 | Copies Register Source into Register Destination |
| M_RLOAD | Double Register | 0000 | 0001 | Copies from Memory at the value of Register Source into Register Destination |
| M_LILOAD | Single Register, Immediate | 0000 | 0010 | Copies Value A into least significant section of Register Destination |
| M_RSTORE | Double Register | 0000 | 0011 | Copies Register Source into Memory at the value of Register Destination |
| A_ADD | Double Register | 0001 | 0000 |
