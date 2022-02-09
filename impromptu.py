import os
from time import sleep
from random import *
from webbrowser import open_new_tab
from keyboard import *
import click as cl
from mylib import *

## VARIABLES ###
illegalMes = "Error: You can't do that. It's \
illegal!"
pref = ">>>"; suf = " $ "

### LIST OF COMMANDS ###
# - prefixcommand {change prefix}
# - suffixcommand {change suffix}
# - do {do main activities}:
#   + fastend {exit very fast}
#   + search {search websites}
#   + slowend {exit slowly}

### FUNCTIONS ###
def endSession(time):
  for i3 in range(0,time):
      s = time-i3
      cl.secho('\rShut down in ' + str(s),nl=False,fg='red')
      sleep(0.5)
  exit()
def mainwork():
  global pref, suf

  command = str(cl.prompt(pref,prompt_suffix=suf))
  listofargs = command.split(" ")

  try:
    if listofargs[0] == "prefixcommand":
      if listofargs[1] == "change":
        if listofargs[2:] != " ":
          try:
            for word in listofargs[2:]:
              pref += word
            pref = word
          except: cl.secho(illegalMes,fg='red')
          pref == '>>>'
        else: cl.secho(illegalMes,fg='red')

    elif listofargs[0] == "do":
      if listofargs[1] == 'fastend' or listofargs[1] == 'kei':
        exit()
      elif listofargs[1] == 'slowend':
        endSession(3)
      elif listofargs[1] == 'search':
        if listofargs[2] == 'google':
          open_new_tab("https://google.com/search?q="+listofargs[3])
        elif listofargs[2] == 'duckduckgo':
          open_new_tab("https://duckduckgo.com/?q="+listofargs[3])
        elif listofargs[2] == 'ask':
          open_new_tab("https://ask.com/web?q="+listofargs[3])
        elif listofargs[2] == 'youtube':
          open_new_tab("https://youtube.com/results?search_query="+listofargs[3])

    elif listofargs[0] == "run":
      if listofargs[1] != ' ':
        os.open()
  except IndexError: cl.secho(illegalMes,fg='red'); pref = ">>>"

### MAIN ###
while True: mainwork()