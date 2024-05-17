import time
import pyautogui as p
from pyautogui import pixel
import autoit

print('Roblox funky friday script. =)')
print('----------------------------------------------------------')
print('Version 1.00')
print('Hell keys are not supported, must play player 2!, circle keys and keys on the bottom!')
print('---------------------------------------------------------------------------------------------------------')

key1=input('Enter key 1')
key2=input('enter key 2')
key3 = input('enter key 3')
key4 = input('enter key 4')

circle1 = (1162, 1012)
circle2 = (1326, 1012)
circle3 = (1490, 1012)
circle4 = (1652, 1012)

green = (18, 250, 5)
teal = (0, 255, 255)
red = (249, 57, 63)
purple = (194, 75, 153)

while True:
    if p.pixelMatchesColor(circle1[0], circle1[1], purple):
        autoit.send(key1)
        print('Pressed q')
    if p.pixelMatchesColor(circle2[0], circle2[1], teal):
        autoit.send(key2)
        print('Pressed w')
    if p.pixelMatchesColor(circle3[0], circle3[1], green):
        autoit.send(key3)
        print('Pressed o')
    if p.pixelMatchesColor(circle4[0], circle4[1], red):
        autoit.send(key4)
        print('Pressed p')