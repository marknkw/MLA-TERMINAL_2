#System.Random random = new();
#int randomPitch = random.Next(400, 450);
#int beepPause = 140;
#Console.Beep(randomPitch, 140);
#Thread.Sleep(beepPause);
#Console.Beep(randomPitch + random.Next(-20, 50), 140);
import cgi
file = open('resources/monad.html', 'r+')
file_lines = file.readlines()
for i in file_lines:
    print(i.)
