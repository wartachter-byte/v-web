This document inherits all definitions from [virtual cpu.md](/virtual+cpu.md).

#wip

# Opcodes
| Opcode Name | Opcode Value | Operands | Description |
| :-: | :-: | :-: | :-: |
| MOVE | 0x00 | "Destination" is a 8-bit [Operand](/virtual%20cpu.md), "Source" is a 8-bit [Operand](/virtual%20cpu.md) immediately following Destination | Copies the value of the register [Source](/registers.md) into register [Destination](/registers.md) |
| LOAD | 0x01 | "Destination" is a 8-bit [Operand](/virtual%20cpu.md), "Source" is a 64-bit [Operand](/virtual%20cpu.md) immediately following Destination | Copies the value from Memory at Source to register [Destination](/registers.md) |
| STORE | 0x02 | "Destination" is a 64-bit [Operand](/virtual%20cpu.md), "Source" is a 8-bit [Operand](/virtual%20cpu.md) immediately following Destination | Copies the value from register [Source](/registers.md) to Memory at Destination |
| ADD | 0x03 | "Destination" is a 8-bit [Operand](/virtual%20cpu.md), "A" is a 8-bit [Operand](/virtual%20cpu.md) immediately following Destination, "B" is a 8-bit [Operand](/virtual%20cpu.md) immediately following A | Adds register [A](/registers.md) and register [B](/registers.md) together and stores in register [Destination](/registers.md)
