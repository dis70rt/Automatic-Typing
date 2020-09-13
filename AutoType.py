'''
Created on 13-Sep-2020

@author: SAIKAT DAS
@instagram = @saikat._
@GitHub = saikat0326
Website : https://cutt.ly/Saikat
'''

import sys
import time
import os

#Default Values
time_speed = 0.5
loop = True    
letter_status = "DISABLE"

while loop == True:
    print(r"""
 ________  ________  ___  ___  __    ________  _________   
|\   ____\|\   __  \|\  \|\  \|\  \ |\   __  \|\___   ___\ 
\ \  \___|\ \  \|\  \ \  \ \  \/  /|\ \  \|\  \|___ \  \_| 
 \ \_____  \ \   __  \ \  \ \   ___  \ \   __  \   \ \  \  
  \|____|\  \ \  \ \  \ \  \ \  \\ \  \ \  \ \  \   \ \  \ 
    ____\_\  \ \__\ \__\ \__\ \__\\ \__\ \__\ \__\   \ \__\
   |\_________\|__|\|__|\|__|\|__| \|__|\|__|\|__|    \|__|
   \|_________|                                            

                                                                                                                                                                                      
            """)

    print("Enter:")
    print(" 11 to Start")
    print(" 22 for Settings")
    print(" 00 to Exit...")

    print()
    ch = int(input(">>>>>> "))
    print()

    if ch == 11:
        name = input("Enter Sentence : ") [::-1]
        if letter_status == "ENABLE":
            name = name.upper()
        print()
        clear = lambda: os.system('cls')
        clear()
        t = len(name)
        list_name = list(name)
        while t:
            mins, secs = divmod(t, 60)
            sys.stdout.write(list_name[t - 1])
            sys.stdout.flush()
            time.sleep(time_speed)
            t -= 1
        print("\n")
        temp = input("\nPress [Enter] to Continue...")
   
    elif ch == 00:
        loop = True
        exit(0)

    elif ch == 22:
        checkSettings = True
        while checkSettings == True:
            print("The Typing Speed is ", time_speed, "(Default : 1.00) [Range : 0 < x < 10]")
            print("Enter The Typing Speed")
            time_speed = float(input(">>>>> "))
            print("\nCaptialize Each Letter :", letter_status)
            letter_status = input("Enable/Disable >>>> ").upper()
            
            if (letter_status == "ENABLE" or letter_status == "DISABLE") and time_speed > 0.0 and time_speed < 10.0:
                checkSettings = False
            else:
                print("\nInvalid Option !\n")
                checkSettings = True 
    
    else:
        temp = input("Invalid Option Press [Enter] to Try Again...")
    
    clear = lambda: os.system('cls')
    clear()
   
