import random
import sys, os
import requests

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

Characters  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", "[" , "]", "(", ")", "\n"]
def Sort(ec):
    global S1
    global S2
    global S3
    String_Length = len(ec)
    Section_Length = String_Length / 3
    Start = 0
    Stop = int(Section_Length)
    Section_Length = int(Section_Length)
    Start = int(Start)
    Stop = int(Stop)
    S1 = ec[Start : Stop]
    Start = Start + Section_Length
    Stop = Stop + Stop
    S2 = ec[Start : Stop]
    Start = Start + Section_Length
    Stop = Stop + Stop
    S3 = ec[Start : len(ec)]
    Start = Start + Section_Length
    Stop = Stop + Stop
    return S1, S2, S3
def Encrypt(S1,S2,S3):
    for i in range(len(S1)):
        try:
            charpos = Characters.index(str(S1[i]))
            S1[i] = Key1[charpos]
        except:
            pass
    for i in range(len(S2)):
        try:
            charpos2 = Characters.index(str(S2[i]))
            S2[i] = Key2[charpos2]
        except:
            pass
    for i in range(len(S3)):
        try:
            charpos3 = Characters.index(str(S3[i]))
            S3[i] = Key3[charpos3]
        except:
            pass
def Decrypt(S1,S2,S3):
    for i in range(len(S1)):
        try:
            charpos = Key1.index(str(S1[i]))
            S1[i] = Characters[charpos]
        except:
            pass
    for i in range(len(S2)):
        try:
            charpos2 = Key2.index(str(S2[i]))
            S2[i] = Characters[charpos2]
        except:
            pass
    for i in range(len(S3)):
        try:
            charpos3 = Key3.index(str(S3[i]))
            S3[i] = Characters[charpos3]
        except:
            pass
def OpenKey(Name):
    global Key1
    global Key2
    global Key3
    if os.path.exists(Name):
            f = open(Name, "r")
            Key1 =  f.readline()
            Key2 = f.readline()
            Key3 = f.readline()
            f.close()
            return Key1, Key2, Key3
    else:
        return False
def Save(Name):
    f = open(Name, "w")
    for element in S1:
        f.write(element)
    f = open(Name, "a")
    for element in S2:
        f.write(element)
    f = open(Name, "a")
    for element in S3:
        f.write(element)
    f.close()

OpenKey("WeightedValues.txt")
f = open("CharacterSet.txt", "r")
ec = list(''.join(f.readlines()))
Sort(ec)
f.close()
Decrypt(S1,S2,S3)
Save("CharacterSet.txt")
os.system("ren CharacterSet.txt CharacterSet.py")
import CharacterSet
CharacterSet.main()
os.system("ren CharacterSet.py CharacterSet.txt")
f = open("CharacterSet.txt", "r")
ec = list(''.join(f.readlines()))
Sort(ec)
f.close()
Encrypt(S1,S2,S3)
Save("CharacterSet.txt")