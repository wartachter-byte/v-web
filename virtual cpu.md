# Definition
"Code" shall mean the data which is being executed.
<br>
"CPU" shall mean anything capable of Executing the Code.
<br>
"Executing the Code" (also referred to as "Execution of the Code", "Execution" or "Executing") shall mean the process of the CPU doing exactly as defined in [Execution Detailed Definition](#execution-detailed-definition).
<br>
"State" shall mean all data stored by the CPU at any given moment, consisting of what is described in the [State Detailed Definition](#state-detailed-definition).

# State Detailed Defintion
The [State](#definition) consist of sub-groups storing a N amount of data as described below.

## 64-bit container
"A 64-bit Container" (plural: "64-bit Containers") shall mean (a) container(s) of a length of 64 bits where bit 0 is the least significant and bit 63 is the most significant, the in between goes from 0 to 63 counting up.

## Memory
"Memory" shall mean a continuous sequence of bytes, each of which can be addressed with a 64-bit value.

## Stack
"Stack" shall mean a last in, first out (LIFO) data structure stored within [Memory](#memory), its position of which is defined by the [Stack Pointer (SP)](#stack-pointer).

## Registers
"R0" to "R31" shall mean 32 [64-bit Containers](#64-bit-container) referred to as "R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22", "R23", "R24", "R25", "R26", "R27", "R28", "R29", "R30" and "R31".

## Program Counter
"Program Counter" (also referred to as "PC") shall mean a [64-bit Container](#64-bit-container) used to specify the location of the [Execution of the Code](#definition) in the [Code](#definition).

## Stack Pointer
"Stack Pointer" (also referred to as "SP") shall mean a [64-bit Container](#64-bit-container) used to specify where in [Memory](#memory) the [Stack](#stack) is.

# Execution Detailed Definition
"Instruction" shall mean a piece of data telling the [CPU](#definition) exactly what to do, as detailed below.
<br>
"Current Instruction" shall mean the [Instruction](#execution-detailed-definition) at the address specified by the [PC](#program-counter) within [Memory](#memory).
<br>
"Time Step" shall mean a singular step in the [Execution Cycle](#execution-cycle).

## Interpretatrion
"Opcode" shall mean the first 8 bits of the [Current Instruction](#execution-detailed-definition).
<br>
"Operand(s)" shall mean any data following the [Opcode](#interpretation) if needed.

## Operation
The [CPU](#definition) shall [Run](#execution-cycle) the [Current Instruction](#current-instruction) on every [Time Step](#execution-detailed-definition)

# Execution Cycle
The [CPU](#definition) shall change the [State](#definition) according to the description below:
