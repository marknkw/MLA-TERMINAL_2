
# Mostra sequência do olho piscando

import os
import sys
import time
from typing import Any, Literal, NoReturn
import winsound
from random import randint
from time import sleep
from PIL import Image, ImageSequence

def terminalCommands() -> list:
    """
    It reads a text file and returns a list of the lines in the text file
    :return: A list of commands
    """
    path: Literal['resources/terminals/help'] = 'resources/terminals/help'
    with open(f'{path}/help_commands.txt', 'r+', encoding="utf-8") as file:

        commandlist = file.readlines()
        time.sleep(1)
        for i in range(len(commandlist)):
            commandlist[i] = commandlist[i].rstrip('\n')
        
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

def waitForCommand() -> str:
    """
    It waits for a command to be entered, then it splits the command into a list of commands
    """
    print(" ")

    return input('[guest@local]# ')

def readeyes() -> list[list[str]]:
    """
    The readeyes function reads in the text files containing the eye emojis and returns a list of lists.
    The outer list contains 8 elements, each element is a list containing all of the lines from an individual file.
    This allows for easy access to each set of eyes.
    :return: A list of lists
    """

    with open('resources/eyes/eye_01.txt', 'r', encoding='utf-8') as file_1, open('resources/eyes/eye_02.txt', 'r', encoding='utf-8') as file_2, open('resources/eyes/eye_03.txt', 'r', encoding='utf-8') as file_3, open('resources/eyes/eye_04.txt', 'r', encoding='utf-8') as file_4, open('resources/eyes/eye_05.txt', 'r', encoding='utf-8') as file_5, open('resources/eyes/eye_06.txt', 'r', encoding='utf-8') as file_6, open('resources/eyes/eye_07.txt', 'r', encoding='utf-8') as file_7, open('resources/eyes/eye_08.txt', 'r', encoding='utf-8') as file_8:

        eye_01: list[str] = file_1.readlines()
        eye_02: list[str] = file_2.readlines()
        eye_03: list[str] = file_3.readlines()
        eye_04: list[str] = file_4.readlines()
        eye_05: list[str] = file_5.readlines()
        eye_06: list[str] = file_6.readlines()
        eye_07: list[str] = file_7.readlines()
        eye_08: list[str] = file_8.readlines()

        file_1.close()
        file_2.close()
        file_3.close()
        file_4.close()
        file_5.close()
        file_6.close()
        file_7.close()
        file_8.close()
        return [eye_01, eye_02, eye_03, eye_04, eye_05, eye_06, eye_07, eye_08]

def blinkingEyes(eyes, j) -> None:

    # Printing the eyes and making a sound.
    if j % 2 != 0:
        for i in eyes[j]:
            print(i)
        winsound.Beep(randint(420, 500), 180)
        sleep(randint(1, 2))
    else:
        for i in eyes[j]:
            print(i)

    clear()

def monadSphere() -> NoReturn:
    while True:
        with Image.open(('./resources/eyes/gifs/monad_sphere.gif')) as gif:
            gif.seek(1)
            try:
                while 1:
                    gif.seek(gif.tell()+1)
                    gif.show()
            except KeyboardInterrupt or EOFError:
                clear()
                gif.close()
                boot()
            


"""def monadSphereFunctioning() -> NoReturn:
    
    # A function that prints the sphere spinning.
    while True:
        try:
            monadSphere()
        except KeyboardInterrupt:
            clear()
            boot()"""


def olhopiscando(eyes) -> NoReturn:
    
    # A function that prints the eyes blinking.
    while True:
        try:
            for i in range(len(eyes)):
                blinkingEyes(eyes, i)  # type: ignore

        except KeyboardInterrupt:
            clear()
            boot()


"""
piscandoolhos = 0


    def capturarThread() -> None:
    
    It captures the input from the user and sets the global variable piscandoolhos to 1.
    
    global piscandoolhos
    input()
    piscandoolhos = 1

def continuePiscando() -> None:
    t1 = threading.Thread(target= olhopiscando(readeyes()), name='piscandoolhos', daemon=True)
    t1.start()
    while piscandoolhos:
       print("Press enter to continue")"""





def unknownCommand() -> NoReturn: # type: ignore
    """
    If the user types in an unknown command, the program will ask the user to type in a known command.
    """ 

    while True:

        winsound.PlaySound(
                './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        z = "Unknow command. Type 'help' for list of available commands."
        for i in z:    
            delay_print(i)

        command: str = waitForCommand()
        if command.rstrip('\n') == 'help':
            programa(command.rstrip('\n'))



def boot() -> NoReturn:  # type: ignore
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

    # Printing the file boot_2.txt line by line with a delay of 0.01 seconds.
    with open('./resources/boot/boot_2.txt', 'r') as fe:
        prt = fe.readlines()
        for ltr in prt:
            sys.stdout.write(ltr)
            sys.stdout.flush()
            time.sleep(0.01)
    
    """
    The boot function plays a sound, then prints a file line by line, then prints another file, 
    then asks for input.
    
    
    :return: A none type
    """
    command_list_terminal = waitForCommand().rstrip("\n")

    clear()

    if command_list_terminal in terminalCommands():
        programa(command_list_terminal)
    else:
        unknownCommand()

def helpCommand() -> NoReturn:
    """
    The helpCommand function is a function that prints out the help.txt file in the resources/terminals/help folder.
    
    :return: The help
    """
    while True:
        with open('./resources/terminals/help/help.txt', 'r', encoding="utf-8") as file:
            for i in file:
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                delay_print(i)
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_PURGE | winsound.SND_ASYNC)

        

def programa(comando = "exit") -> NoReturn:
    """
    The programa function is the main function of the game. It will be called at every iteration of a loop that
    controls the flow of our game. The programa function will take in a string as an argument, and depending on what 
    that string is, it will do different things. If you pass 'exit' to this function, it'll close out your game session 
    and exit back into your command prompt.
    :param comando=&quot;exit&quot;: Close the programa function and return to the main menu
    :return: The text of the file in the path passed as parameter
    """
   
    if comando == 'exit':
        with open('./resources/terminals/exit/exit.txt', 'r', encoding="utf-8") as file:
            for i in file:
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                delay_print(i)
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_PURGE | winsound.SND_ASYNC)
            exit()

    elif comando == 'help':
        with open('./resources/terminals/help/help.txt', 'r', encoding="utf-8") as file:
            for i in file:
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                delay_print(i)
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_PURGE | winsound.SND_ASYNC)
                
        programa(waitForCommand())

    elif comando == 'list':
        with open('./resources/terminals/exit/help.txt', 'r', encoding="utf-8") as file:
            for i in file:
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                delay_print(i)
                winsound.PlaySound(
                    './resources/sounds/TerminalTypingComputer.wav', winsound.SND_PURGE | winsound.SND_ASYNC)
    
    else:
        olhopiscando((readeyes()))

monadSphere()
