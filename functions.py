# Mostra sequência do olho piscando
from codecs import ignore_errors
import os
import sys
import time
import winsound
from random import randint
from time import sleep
import threading
from click import command
from sqlalchemy import false, true
from sympy import O
import os, glob

def terminalCommands() -> list:
    """
    It reads a text file and returns a list of the lines in the text file
    :return: A list of commands
    """
    path = './resources/terminals/help'
    commandlist = []
    with open(path + '/help_commands.txt', 'r+', encoding="utf-8") as file:
        for i in file:
            commandlist.append(i)
        for i in range(0, len(commandlist)):
           commandlist[i] = commandlist[i].rstrip("\n")
    return commandlist


def delay_print(se) -> None:
    """
    The delay_print function prints the input string character by by, with a 100ms delay between each character.
    This is helpful for simulating print statements that take time to execute.
    :param s: Pass the string that you want to print
    :return: nothing
    """
    for ce in se:
        sys.stdout.write(ce)
        sys.stdout.flush()
        time.sleep(0.02)


def clear() -> int:
    """
    The clear function clears the screen.
    It is used to make the output of multiple function calls easier to read by 
    clearing the screen before each call.
    :return: terminal reset
    """
    return os.system('cls' if os.name == 'nt' else 'clear')

def waitForCommand() -> None:
    """
    It waits for a command to be entered, then it splits the command into a list of commands
    """
    exit_var = input('[guest@local]# ').rsplit('\n')

def readeyes() -> list:    # type: ignore # sourcery skip: low-code-quality
    """
    The readeyes function reads in the text files containing the eye emojis and returns a list of lists.
    The outer list contains 8 elements, each element is a list containing all of the lines from an individual file.
    This allows for easy access to each set of eyes.
    :return: A list of lists
    """

    with open('resources/eyes/eye_01.txt', 'r', encoding='utf-8') as file_1, open('resources/eyes/eye_02.txt', 'r', encoding='utf-8') as file_2, open('resources/eyes/eye_03.txt', 'r', encoding='utf-8') as file_3, open('resources/eyes/eye_04.txt', 'r', encoding='utf-8') as file_4, open('resources/eyes/eye_05.txt', 'r', encoding='utf-8') as file_5, open('resources/eyes/eye_06.txt', 'r', encoding='utf-8') as file_6, open('resources/eyes/eye_07.txt', 'r', encoding='utf-8') as file_7, open('resources/eyes/eye_08.txt', 'r', encoding='utf-8') as file_8:

        eye_01 = file_1.readlines()
        eye_02 = file_2.readlines()
        eye_03 = file_3.readlines()
        eye_04 = file_4.readlines()
        eye_05 = file_5.readlines()
        eye_06 = file_6.readlines()
        eye_07 = file_7.readlines()
        eye_08 = file_8.readlines()

        file_1.close()
        file_2.close()
        file_3.close()
        file_4.close()
        file_5.close()
        file_6.close()
        file_7.close()
        file_8.close()
        return [eye_01, eye_02, eye_03, eye_04, eye_05, eye_06, eye_07, eye_08]

def olhopiscando(eyes) -> None:
    """
    The olhopiscando function is a function that prints out the eyes of the olho de boi.
    It has no parameters and returns nothing.

    :param eyes: Pass the eyes to the olhopiscando function
    :return: None
    """
    for i in eyes[0]:
        print(i)
    winsound.Beep(randint(420, 500), 180)
    sleep(randint(1, 2))
    clear()
    for i in eyes[1]:
        print(i)    
    sleep(0.01)
    clear()
    for i in eyes[2]:
        print(i)
    clear()
    for i in eyes[3]:
        print(i)
    sleep(randint(1, 2))
    winsound.Beep(randint(410, 460), 180)
    clear()
    for i in eyes[4]:
        print(i)
    clear()
    for i in eyes[5]:
        print(i)
    for i in eyes[6]:
        print(i)
    sleep(0.2)
    clear()
    for i in eyes[7]:
        print(i)
    sleep(randint(1, 3))
    winsound.Beep(randint(410, 450), 180)
    clear()

piscandoolhos = true
def capturarThread() -> None:
    """
    It captures the input from the user and sets the global variable piscandoolhos to 1.
    """
    global piscandoolhos
    input()
    piscandoolhos = false

def continuePiscando() -> None:
    t1 = threading.Thread(target= olhopiscando(readeyes()), name='piscandoolhos', daemon=True)
    t1.start()
    while piscandoolhos:
       print("\nPress enter to continue")

def unknownCommand() -> None:
    """
    If the user types in an unknown command, the program will ask the user to type in a known command.
    """ 

    while True:
        print("Unknow command. Type 'help' for list of available commands.")
        command = input().lower()
        if command == 'help':
            programa()


def boot() -> None:  # type: ignore
    """
    It plays a sound, then prints a file line by line, then prints another file, then asks for input.
    """

    winsound.PlaySound(
                './resources/sounds/TerminalPowerOn.wav', winsound.SND_FILENAME | winsound.SND_NOSTOP)

    with open('./resources/boot/boot.txt', 'r') as fe:

        for i in fe:
            winsound.PlaySound(
                './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            delay_print(i)

    with open('./resources/boot/boot_2.txt', 'r') as fe:
        prt = fe.readlines()
        for ltr in prt:
            sys.stdout.write(ltr)
            sys.stdout.flush()
            time.sleep(0.01)

        z = input("")
        if z in terminalCommands():
            programa()
        unknownCommand()

def programa() -> None:
    """
    It opens a file, reads it line by line, and prints it out with a delay.
    """
    while True:
        with open('./resources/terminals/help/help.txt', 'r', encoding="utf-8") as file:

            for i in file:
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                delay_print(i)
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_PURGE | winsound.SND_ASYNC)

        print("\n")

        exit_var = input('[guest@local]# ').rsplit('\n')
        if exit_var != "":
            exit()

continuePiscando()
boot()
