This document inherits all definitions from [virtual cpu.md](/virtual+cpu.md).

#wip

# Opcodes
| Opcode Name | Opcode Value | Operands | Description |
| :-: | :-: | :-: | :-: |
| MOVE | 0x00 | "Destination" is an Operand of the size of 8 bits, "Source" is an Operand of the size of 8 bits immediately following Destination | Copies the value of the register [Source](/register.md) into register [Destination](/registers.md) |
| LOAD | 0x01 | "Destination" is an Operand of the size of 8 bits, "Source" is an Operand of the size of 64 bits immediately following Destination | Copies the value from Memory at Source to register [Destination](/registers.md) |
| STORE | 0x02 | "Destination" is an Operand of the size of 64 bits, "Source" is an Operand of the size of 8 bits immediately following Destination | Copies the value from register [Source](/register.md) to Memory at Destination |
