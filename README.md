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
* Uses very bare-bones GUI as a way to provide program with input; otherwise, all output comes from system
* Consists of 5 main Python files including main (which runs the GUI), Process (which implements a custom multithreading Process class), SeedGeneration (which reads files such as programfiles1.txt and generates custom seeds), Operations (which involves the implementation of the First Come First Serve scheduler and the Shortest Job First scheduler along with the calculate(), fork(), and io() functions), and Memory (which implements Main and Virtual memory classes along with Paging).
* More specifically, the Memory file has a VirtualMemory class which adds pages for each Process operation, adds those pages to a PageTable, and converts the logical addresses of those Pages to the physical address of the Main Memory.
* The toPhysical() function in the VirtualMemory class uses the Basic page replacement algorithm mentioned in Lectures 13-14 and selects its victim through a FIFO queue.
* Each process/Thread shares the MainMemory as a pool so that processes can run concurrently with the help of Locks.

## Simulator Guide

The currently functional commands for the OS Simulator include LOAD , SETPROC <num. processes>, START, SUSPEND , and
STATS. You can use LOAD to read a program file (such as programfile1.txt), which essentially initializes the program. SETPROC
determines the number of processes running concurrently during the simulation, and currently sets the last process to have the
SJF scheduler. START allows the Processes to run each of their operations (i.e. calculate) for the generated amount of cycles.
Suspend allows you to run the processes for a limited number of cycles. STATS generates the statistics for each process and a
log file for each of the processes is generated detailing the individual operations each process completed.

Example string of commands: LOAD programfile1.txt -> SETPROC 2 -> START -> STATS
