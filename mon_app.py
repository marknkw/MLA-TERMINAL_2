#Mostra sequência do olho piscando

from random import randint
from time import sleep
import winsound

import os

def clear():
    """
    The clear function clears the screen.
    It is used to make the output of multiple function calls easier to read by 
    clearing the screen before each call.
    
    :return: The output of the os
    """
    return os.system('cls' if os.name == 'nt' else 'clear')

def read_eyes():
    """
    The read_eyes function reads in the three eye files and returns a list of lists.
    The outer list contains 3 elements, each element is a list containing all lines from an eye file.
    
    
    :return: A list of lists
    """
    with open('resources/eye_01.txt', 'r+') as file_1, \
         open('resources/eye_02.txt', 'r+') as file_2,  \
         open('resources/eye_03.txt', 'r+') as file_3:
         list = []
         eye_01 = file_1.readlines()
         eye_02 = file_2.readlines()
         eye_03 = file_3.readlines()
         file_1.close()
         file_2.close()
         file_3.close()
         list.append(eye_01)
         list.append(eye_02)
         list.append(eye_03)
         return list

eyes = read_eyes()


def olhoPiscando(eyes):
    """
    The olhoPiscando function prints out the eyes of a smiley face.
    It takes in an array of arrays, and uses that to print out the eyes.
    
    :param eyes: Determine the eyes that will be printed
    :return: The eyes variable
    """
    while True:
        for i in eyes[0]:
            print(i)
        sleep(randint(2,5))
        clear()
        for i in eyes[1]:
            print(i)
        sleep(0.4)
        winsound.Beep(randint(400, 450), 160)
        clear()
        for i in eyes[2]:
            print(i)
        clear()

olhoPiscando(eyes)

