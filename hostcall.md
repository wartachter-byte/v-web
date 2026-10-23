<!-- Satus: WIP -->

This document inherits all definitions from [virtual cpu.md](/virtual%20cpu.md) and [opcodes.md](/opcodes.md)

# F_HOSTCALL
1. 'SYSNUM' shall be the value of register R0 when this instruction is called
2. 'SYSARG0' shall be the value of register R1 when this instruction is called
3. 'SYSARG1' shall be the value of register R2 when this instruction is called
4. 'SYSARG2' shall be the value of register R3 when this instruction is called
5. 'SYSARG3' shall be the value of register R4 when this instruction is called
6. 'SYSARG4' shall be the value of register R5 when this instruction is called
7. 'SYSARG5' shall be the value of register R6 when this instruction is called
8. 'SYSARG6' shall be the value of register R7 when this instruction is called

For it be the operation, SYSNUM MUST be equal to the specified value.
| Mnemonic | SYSNUM | Description |
| :-: | :-: | :-: |
| EXIT | 0 | Destroys the current Process |
