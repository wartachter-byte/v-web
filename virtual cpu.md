# Work In Progress
This document is still being worked, nothing in this document is complete yet and as such MUST not yet be active.

# Proccess
"Proccess" shall mean a collection of 1 State and 1 Code, Execution of the Code in the Proccess can be on any CPU.
"This Proccess" shall mean the current Proccess.

# Definition
"Code" shall mean the data which is being executed.
<br>
"CPU" shall mean anything capable of Executing the Code.
<br>
"Executing the Code" (also referred to as "Execution of the Code", "Execution" or "Executing") shall mean the process of the CPU doing exactly as defined in [Execution Detailed Definition](#execution-detailed-definition).
<br>
"State" shall mean all data stored by the CPU at any given moment, consisting of what is described in the [State Detailed Definition](#state-detailed-definition).
<br>
"0x" shall mean a notation prefix detailing that the immediately following sentence is a numeric value written in base-16 (hexadecimal) where 0 through 9 have the values 0 through 9 and A through F have the values 10 through 15.

# State Detailed Defintion
The [State](#definition) consist of sub-groups storing a N amount of data as described below.

## 64-bit container
"A 64-bit Container" (plural: "64-bit Containers") shall mean (a) container(s) of a length of 64 bits where bit 0 is the least significant and bit 63 is the most significant, the in between goes from 0 to 63 counting up.

## Bit order
Whenever the term '-bit' is used with a decimal number coming immediately in front of it, it specifies the size of an object in bits, if the object needs to be interpreted as a value it MUST be interpreted in the order of big-endian.

## Memory
"Memory" shall mean a continuous sequence of bytes, each of which can be addressed with a 64-bit value belonging to this [Proccess](#proccess)

## Stack
"Stack" shall mean a last in, first out (LIFO) data structure stored within [Memory](#memory), its position of which is defined by the [Stack Pointer (SP)](#stack-pointer).

## Registers
"R0" to "R31" shall mean 32 [64-bit Containers](#64-bit-container) referred to as "R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22", "R23", "R24", "R25", "R26", "R27", "R28", "R29", "R30" and "R31".

## Program Counter
"Program Counter" (also referred to as "PC") shall mean a [64-bit Container](#64-bit-container) used to specify the location of the [Execution of the Code](#definition) in the [Code](#definition).

## Stack Pointer
"Stack Pointer" (also referred to as "SP") shall mean a [64-bit Container](#64-bit-container) used to specify where in [Memory](#memory) the [Stack](#stack) is.

# Execution Detailed Definition
"Instruction" shall mean a 32-bit number telling the [CPU](#definition) exactly what to do, as detailed below.
<br>
"Current Instruction" shall mean the [Instruction](#execution-detailed-definition) at the address specified by the [PC](#program-counter) within [Memory](#memory).
<br>
"Time Step" shall mean a singular step in the [Execution Cycle](#execution-cycle).

## Operation
The [CPU](#definition) MUST [Run](#execution-cycle) the [Current Instruction](#current-instruction) on every [Time Step](#execution-detailed-definition).

# Execution Cycle
The [CPU](#definition) MUST change the [State](#definition) every [Time Step](#execution-detailed-definition) according to the [Current Instruction](#execution-detailed-definition) and its corresponding description as defined table 'Opcodes' in [opcodes.md](/opcodes.md).
