# Mostra sequência do olho piscando

import base64
import os
import sys
import time
import winsound
from ast import Try
from itertools import chain
from random import randint
from time import sleep

import keyboard

# Função que printa letra por letra de uma frase com delay


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
        time.sleep(0.04)


def clear() -> int:
    """
    The clear function clears the screen.
    It is used to make the output of multiple function calls easier to read by 
    clearing the screen before each call.

    :return: terminal reset
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


def readeyes() -> list[list[str]]:  # sourcery skip: low-code-quality
    """
    The read_eyes function reads in the three eye files and returns a list of 
    lists. the outer list contains 3 elements, each element is a list
    containing all lines from an eye file.


    :return: A list of lists
    """
    with open('resources/eye_01.txt', 'r') as file_1, open('resources/eye_02.txt', 'r') as file_2, open('resources/eye_03.txt', 'r') as file_3, open('resources/eye_04.txt', 'r') as file_4, open('resources/eye_05.txt', 'r+') as file_5, open('resources/eye_06.txt', 'r+') as file_6, open('resources/eye_07.txt', 'r+') as file_7, open('resources/eye_08.txt', 'r+') as file_8:

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


def olhopiscando(eyes) -> None:  # sourcery skip: low-code-quality
    """
    The olhoPiscando function prints out the eyes of a cartoon face.It does this by printing out each line of the eye in order, and then waiting for a keypress before moving on to the next line.
    The function will continue to do this until it is interrupted by a keypress. :param eyes: Pass the eyes list to the olhopiscando function :return: The function itself
    """
    while True:
        for i in eyes[0]:
            print(i)
        print("press-any-key")
        sleep(randint(2, 5))
        clear()
        for i in eyes[1]:
            print(i)
        print("press-any-key")
        sleep(0.01)
        clear()
        for i in eyes[2]:
            print(i)
        print("press-any-key")
        clear()
        for i in eyes[3]:
            print(i)
        print("press-any-key")
        sleep(randint(2, 5))
        winsound.Beep(randint(400, 450), 130)
        clear()
        for i in eyes[4]:
            print(i)
        print("press-any-key")
        clear()
        for i in eyes[5]:
            print(i)
            print("press-any-key")

        for i in eyes[6]:
            print(i)
        print("press-any-key")
        sleep(0.5)
        clear()
        for i in eyes[7]:
            print(i)
        print("press-any-key")
        sleep(randint(2, 5))
        winsound.Beep(randint(400, 450), 130)
        clear()

        olhopiscando(eyes)


def boot() -> None:
    """
    The boot function is used to print the boot sequence of the game. It uses a for loop to iterate through each line in 
    the text file and prints it with a delay between each character printed. The function also plays an audible tone at random 
    frequencies between 400 and 450 Hz for 130 milliseconds after printing each line.

    :return: nothing
    """
    with open('resources/boot/boot.txt', 'r') as f:
        for i in f:
            winsound.PlaySound(
                'typ.wav', winsound.SND_LOOP | winsound.SND_ASYNC)
            delay_print(i)
            winsound.PlaySound(
                'typ.wav', winsound.SND_PURGE | winsound.SND_ASYNC)

        delay_print('Loading...')
        time.sleep(1)


# sourcery skip: avoid-builtin-shadow
boot()
olhopiscando(readeyes())

'''def programa():
   
        
class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        # creating thread
        eyes = read_eyes()
        
        super(MyThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

        t1 = threading.Thread(target=eyes = olhoPiscando(eyes), args=(10,))
        t2 = threading.Thread(target=print_cube, args=(10,))

        # function using _stop function
        def stop(self):
            self._stop.set()

        def stopped(self):
            return self._stop.isSet()
        
       def run(self):
        while True:
            if self.stopped():
                return
    
        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()
          # both threads completely executed
        delay_print("Exiting terminal...")
'''
