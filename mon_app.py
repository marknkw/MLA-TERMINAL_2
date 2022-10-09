#System.Random random = new();
#int randomPitch = random.Next(400, 450);
#int beepPause = 140;
#Console.Beep(randomPitch, 140);
#Thread.Sleep(beepPause);
#Console.Beep(randomPitch + random.Next(-20, 50), 140);

#Mostra sequência do olho piscando

import time
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
         list.append(eye_01)
         list.append(eye_02)
         list.append(eye_03)
         return list

eyes = read_eyes()

def olhoPiscando(eyes):
    for i in eyes[0]:
        print(i)
    for i in eyes[1]:
        print(i)
    for i in eyes[2]:
        print(i)

olhoPiscando(eyes)

