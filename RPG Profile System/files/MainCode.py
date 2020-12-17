#MainCode

import os
import os.path
import ctypes
import time
from os import system, name

ProfileFolder = 'profiles/'

#-------------------------------------------------------------------------------
#Clear--------------------------------------------------------------------------
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

#-------------------------------------------------------------------------------
#Profile------------------------------------------------------------------------
class Profile:
    #Load
    def Load():
        try:
            print('=======================================================================')
            print('Type the profile name to load.')
            ProfileName = input('>')
            print('')
            with open('profiles/' + ProfileName + '.profile', 'r') as ProfileInfo:
                ProfileFile = ProfileInfo.read()
                print('=======================================================================')
                print(ProfileFile)
                print('')
                print('Press "Enter" to continue.')
                print('=======================================================================')
                input()
                clear()

        except:
            print('Profile not found.')
            print('')
            print('Press "Enter" to continue.')
            print('=======================================================================')
            input()
            clear()


    #Create
    def Create():
        print('=======================================================================')
        print('Name the profile file.')
        ProfileName = input('>')
        print('')
        print('=======================================================================')
        print('Select a class:')
        print('1.Warrior\n2.Archer\n3.Tank')
        ProfileClass = input('>')

        if ProfileClass == '1':
            ProfileClassType = 'Warrior'
            HP = '150'
            DF = '75'
            SPD = '50'
            AT = '50'
            ASPD = '30'

        if ProfileClass == '2':
            ProfileClassType = 'Archer'
            HP = '50'
            DF = '20'
            SPD = '75'
            AT = '10'
            ASPD = '50'

        if ProfileClass == '3':
            ProfileClassType = 'Tank'
            HP = '200'
            DF = '100'
            SPD = '15'
            AT = '20'
            ASPD = '20'

        ProfileCreation = os.path.join(ProfileFolder, ProfileName + '.profile')
        Profile = open(ProfileCreation, 'w')
        ProfileStatus = f'PROFILE: {ProfileName}\nCLASS: {ProfileClassType}\nHP: {HP}\nDF: {DF}\nSPD: {SPD}\nAT: {AT}\nASPD: {ASPD}'
        Profile.write(ProfileStatus)
        Profile.close()
        clear()

    #Show
    def Show():
        print('=======================================================================')
        print('Profiles:')
        print('')
        ProfileList = os.listdir(ProfileFolder)
        for f in ProfileList:
	           print(f)
        print('')
        print('Press "Enter" to continue.')
        print('=======================================================================')
        input()
        clear()

    #Delete
    def Delete():
        try:
            print('=======================================================================')
            print('Type the profile name to delete.')
            ProfileName = input('>')
            print('')
            os.remove('profiles/' + ProfileName + '.profile')
            print('Profile have been deleted.')
            print('')
            print('Press "Enter" to continue.')
            print('=======================================================================')
            input()
            clear()

        except:
            print('Profile not found.')
            print('')
            print('Press "Enter" to continue.')
            print('=======================================================================')
            input()
            clear()
