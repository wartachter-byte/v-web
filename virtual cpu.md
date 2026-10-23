<!-- Status: WIP, Basics Complete, Markup good, net-com is TODO -->
# Workspace
* "Worskspace" shall mean the environment for all the [Proccess('s)](#proccess)
* The first Proccess to be created is gained from the 'index' of the Server, as detailed in [net-com.md](/net-com.md)

# Proccess
* "Procces" shall mean a collection of 1 State, 1 Code and any CPU shared by multiple Proccess or exclusive to this Proccess
* Proccess can be made by other Proccess as detailed in [hostcall.md](/hostcall.md)
* A Proccess does not stop Executing its Code untill the Workspace is destroyed or the Proccess [exits](/hostcall.md)
* When a Proccess is first created, ita PC will start at 0

# Definition
* "Code" shall mean a section of [Memory](#state-detailed-definition) that is not writable or readable by the proccess, but can be executed on.
* "CPU" shall mean anything capable of Executing the Code.
* "Executing the Code" (also referred to as "Execution of the Code", "Execution" or "Executing") shall mean the process of the CPU doing exactly as defined in [Execution Detailed Definition](#execution-detailed-definition).
* "State" shall mean all data stored by the CPU at any given moment, consisting of what is described in the [State Detailed Definition](#state-detailed-definition).
* "0x" shall mean a notation prefix detailing that the immediately following sentence is a numeric value written in base-16 (hexadecimal) where 0 through 9 have the values 0 through 9 and A through F have the values 10 through 15.

# State Detailed Defintion
The [State](#definition) consist of sub-groups storing a N amount of data as described below.

> Whenever the term '-bit' is used with a decimal number coming immediately in front of it, it specifies the size of an object in bits, if the object needs to be interpreted as a value it MUST be interpreted in the order of big-endian.

* "Memory" shall mean a continuous sequence of readable and writable bytes, each of which can be addressed with a 64-bit value belonging to this [Proccess](#proccess), parts of Memory can serve a seperate function.
* "Stack" shall mean a first in, first out (FIFO) data structure stored within [Memory](#memory), its position of which is defined by the [Stack Pointer (SP)](#stack-pointer).
* "R0" to "R31" shall mean 32 64-bit numbers referred to as "R0" through "R31".
* "Program Counter" (also referred to as "PC") shall mean a 64-bit number used to specify the location of the [Execution of the Code](#definition) in the [Code](#definition).
* "Stack Pointer" (also referred to as "SP") shall mean a 64-bit number used to specify where in [Memory](#memory) the [Stack](#stack) is.

# Execution Detailed Definition
* "Instruction" shall mean a 32-bit number telling the [CPU](#definition) exactly what to do, as detailed below.
* "Current Instruction" shall mean the [Instruction](#execution-detailed-definition) at the address specified by the [PC](#program-counter) within [Memory](#memory).
* "Time Step" shall mean a singular step in the [Execution Cycle](#execution-cycle).

## Operation
The [CPU](#definition) MUST [Run](#execution-cycle) the [Current Instruction](#current-instruction) on every [Time Step](#execution-detailed-definition) when Executing the Code.

# Execution Cycle
The [CPU](#definition) MUST change the [State](#definition) every [Time Step](#execution-detailed-definition) according to the [Current Instruction](#execution-detailed-definition) and its corresponding description as defined in table 'Opcodes' in [opcodes.md](/opcodes.md) and inbetween every Time Step the CPU MUST increment the PC by 8.
