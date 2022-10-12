# Mostra sequência do olho piscando

from ast import Try
import base64
from itertools import chain
from random import randint
import sys


from time import sleep
import time


import winsound
import keyboard

import os

import threading


# Função que printa letra por letra de uma frase com delay


def delay_print(s):
    """
    The delay_print function prints the input string character by by, with a 100ms delay between each character.
    This is helpful for simulating print statements that take time to execute.

    :param s: Pass the string that you want to print
    :return: nothing
    """
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)


def clear():
    """
    The clear function clears the screen.
    It is used to make the output of multiple function calls easier to read by 
    clearing the screen before each call.

    :return: terminal reset
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


def readEyes():
    """
    The read_eyes function reads in the three eye files and returns a list of 
    lists. the outer list contains 3 elements, each element is a list
    containing all lines from an eye file.


    :return: A list of lists
    """
    with open('resources/eye_01.txt', 'r+') as file_1,\
         open('resources/eye_02.txt', 'r+') as file_2,\
         open('resources/eye_03.txt', 'r+') as file_3,\
         open('resources/eye_04.txt', 'r+') as file_4,\
         open('resources/eye_05.txt', 'r+') as file_5,\
         open('resources/eye_06.txt', 'r+') as file_6,\
         open('resources/eye_07.txt', 'r+') as file_7,\
         open('resources/eye_08.txt', 'r+') as file_8:


         list = []
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
         list.append(eye_01)
         list.append(eye_02)
         list.append(eye_03)
         list.append(eye_04)
         list.append(eye_05)
         list.append(eye_06)
         list.append(eye_07)
         list.append(eye_08)
         return list


def olhoPiscando(eyes):
    """
    The olhoPiscando function prints out the eyes of a cartoon face.
    It does this by printing out each line of the eye in order, and then waiting for a keypress before moving on to the next line.
    The function will continue to do this until it is interrupted by a keypress.
    
    :param eyes: Pass the eyes list to the olhopiscando function
    :return: The function itself
    """

    while True:
                print(i)
            print("press-any-key")
            sleep(0.01)
            if keyboard.on_press_key():
                break
        except:
        for i in eyes[0]:
            print(i)
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
        try:
        sleep(randint(2, 5))
        winsound.Beep(randint(400, 450), 130)
        clear()
                       
        olhoPiscando(eyes)


def boot():
    """
    The boot function is used to print the boot sequence of the game. It uses a for loop to iterate through each line in 
    the text file and prints it with a delay between each character printed. The function also plays an audible tone at random 
    frequencies between 400 and 450 Hz for 130 milliseconds after printing each line.

    :return: nothing
    """
    with open('resources/boot/boot.txt', 'r') as f:
        # Comment:
        for i in f:
            winsound.PlaySound('typ.wav', winsound.SND_LOOP|winsound.SND_ASYNC)
            delay_print(i)
            winsound.PlaySound('typ.wav', winsound.SND_PURGE|winsound.SND_ASYNC)
            
        # end open file)
        delay_print('Loading...')
        time.sleep(1)
        


# sourcery skip: avoid-builtin-shadow
boot()
list = readEyes()
olhoPiscando(list)

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
