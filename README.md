## Full Information

* Name: Luke Unterman
* VID: V00949703

## GitHub Account Link

https://github.com/untermanlm/CMSC312

## Project Requirements

* Python version required: Python 3.7
* Modern operating systems recommended (i.e. Windows 10)
* Can run with executable file (exe); otherwise, standard compilation requirements

## Project Description

* Source code can be found in src folder in GitHub
* Coded entirely in Python using Tkinter for GUI
* Uses very bare-bones GUI as a way to provide program with input; otherwise, all output comes from system. In project part 3, I finally got my GUI to (somewhat) auto-update the process values as the processes are running! Whenever processes are created or exit, process stats now appear under the command input.
* Consists of 5 main Python files including main (which runs the GUI), Process (which implements a custom multithreading Process class), SeedGeneration (which reads files such as programfiles1.txt and generates custom seeds), Operations (which involves the implementation of the First Come First Serve scheduler and the Shortest Job First scheduler along with the calculate(), fork(), and io() functions), and Memory (which implements Main and Virtual memory classes along with Paging).
* More specifically, the Memory file has a VirtualMemory class which adds pages for each Process operation, adds those pages to a PageTable, and converts the logical addresses of those Pages to the physical address of the Main Memory.
* The toPhysical() function in the VirtualMemory class uses the Basic page replacement algorithm mentioned in Lectures 13-14 and selects its victim through a FIFO queue.
* Each process/Thread shares the MainMemory as a pool so that processes can run concurrently with the help of Locks.
* **Part 3 Changes**: Processes class coded to have a hard afffinity to CPU; this is entirely based on the processes' ID numbers. If the PID number if even, CPU 0 is chosen. Otherwise, CPU 1 is chosen. Also, a new command in the GUI was added. This command is called `MULTI`, and simulates two CPUS running each of their processes concurrently. *Note that currently, MULTI has a limitation meaning the number of processes has to be even.* Since threading has been implemented into my program from the first phase, I did not need to implement that functionality for this phase. Furthermore, I have been using a simple mutex lock which has ensured that everything works concurrently. Finally, the `STATS` command was updated to reflect the runtime and CPU information of the processes depending on their status. For example, the STATS will only print runtime information if the Processes have exited. Also, it will only print information about the simulated CPU if the user used the `MULTI` command.

## Simulator Guide

The currently functional commands for the OS Simulator include LOAD , SETPROC <num. processes>, START, SUSPEND , and
STATS. You can use LOAD to read a program file (such as programfile1.txt), which essentially initializes the program. SETPROC
determines the number of processes running concurrently during the simulation, and currently sets the last process to have the
SJF scheduler. START allows the Processes to run each of their operations (i.e. calculate) for the generated amount of cycles.
Suspend allows you to run the processes for a limited number of cycles. STATS generates the statistics for each process and a
log file for each of the processes is generated detailing the individual operations each process completed. MULTI simulates two CPUS running each of their processes concurrently.

Example string of commands: LOAD programfile1.txt -> SETPROC 2 -> START -> STATS
                            or LOAD programfile1.txt -> SETPROC 4 -> MULTI -> STATS
