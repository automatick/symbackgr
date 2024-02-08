import os
from colorama import init, Fore
from random import randint, choice
from sys import argv, exit
import platform as pl
from string import printable, whitespace

temp = []

for i in printable:
    if i not in whitespace:
        temp.append(i)

del printable, whitespace
printable = tuple(temp)
del temp

if pl.system() == "Linux":
    from cfuncs import *
    clear = lambda: os.system("clear")
else:
    from time import sleep
    write = print
    read = input
    nanosleep = lambda x: sleep(x / 1e9)
    clear = lambda: os.system("cls")
    write("this code may be run slowly at this system yet")
    nanosleep(1000000000)

init()
term: os.terminal_size = os.get_terminal_size()
colors: tuple[str, str, str, str] = ('red', 'blue', 'green', 'random')

if "-h" in argv:
    write(f"""
    {Fore.BLUE}command: {Fore.RESET}  {Fore.LIGHTMAGENTA_EX}python3 symbackgr  {Fore.GREEN}int {Fore.LIGHTCYAN_EX}speed {Fore.GREEN}string {Fore.LIGHTCYAN_EX}color{Fore.RESET} 
    {Fore.LIGHTCYAN_EX}color: {Fore.GREEN}tuple{Fore.RESET} ('blue', 'red', 'green', 'random')
    {Fore.LIGHTCYAN_EX}speed: {Fore.GREEN}int{Fore.RESET} in nanosec from 0 to +inf, 1000000< been High CPU consumption

    {Fore.BLUE}usage: {Fore.RESET}python3 symbackgr 1000000 green
    """)
    exit(0)
color: str = Fore.RESET
try:
        speed: int = int(argv[-2])
        col: str = argv[-1]
        if col not in colors:
            write(f"{Fore.RED} incorrect usage, type 'python3 symbackgr -h' for help.")
            exit(-1)
        match col:
            case "green":
                color = Fore.GREEN
            case "red":
                color = Fore.RED
            case "blue":
                color = Fore.BLUE
            case "random":
                color = "rand"
        del col, argv
except IndexError:
        write(f"{Fore.RED} incorrect usage, type 'python3 symbackgr -h' for help.")
        exit(-1)

clrs: tuple = (Fore.RED, Fore.BLUE, Fore.GREEN)
clear()
if color != 'rand':
    while True:
        string: str = ''
        for i in range(term.columns):
            if randint(0, 1) == 1:
                string += " "
            else:
                string += choice(printable)
        write(f"{color}{string}\n")
        nanosleep(speed)
        del string
else:
    while True:
        for i in range(term.columns):
            if randint(0, 1) == 1:
                write(" ")
            else:
                write(f"{choice(clrs)}{choice(printable)}{Fore.RESET}")
        write('\n')
        nanosleep(speed)
