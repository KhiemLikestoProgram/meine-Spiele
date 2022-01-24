from time import sleep
from playsound import playsound
from os import *; from sys import *
from termcolor import colored
import pygame

## LIST OF COMMANDS:
# - hypno
# - shutdown

## "CONSTANTS":
global Running; Running = False

## LOOPIA
while True:
  print("")
  a = input(colored("\rmain menu >> ","yellow"))
  if a == '': pass

  elif a == "$shutdown" or a == "/shutdown":
    playsound("sounds\Auld Lang Syne 2.mp3",False)
    for i2 in range(1,10):
      s = 10-i2
      if s < 10: strs = str(s) + " "
      else: strs = str(s)
      print(colored("\rShut down in " + strs,"cyan"),end='')
      sleep(2)
    
    exit()

  elif a == "$sdemer" or a == "/sdemer":
    for i3 in range(0,3):
      s = 3-i3
      print(colored('\rShut down in ' + str(s),'red'),end='')
      sleep(0.5)
    exit()
  else: print("Nope. Invalid command.")

  elif a == "$calc":
    while 1:
      operator = input("calculator >> ").split()
