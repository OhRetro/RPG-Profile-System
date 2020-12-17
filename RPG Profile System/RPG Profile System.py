#RPG Profile System
#Versão:1.0

import os
import os.path
import ctypes
import time
import csv
from os import system, name
from files.MainCode import *

ctypes.windll.kernel32.SetConsoleTitleW('RPG Profile System')

while True:
    print('=======================================================================')
    print('1.Load Profile\n2.Create Profile\n3.Show Profiles\n4.Delete Profile')
    print('')
    ProfileMode = input('Choose a mode:>')
    if ProfileMode == '1':
        print('')
        Profile.Load()

    if ProfileMode == '2':
        print('')
        Profile.Create()

    if ProfileMode == '3':
        print('')
        Profile.Show()

    if ProfileMode == '4':
        print('')
        Profile.Delete()

    else:
        clear()
