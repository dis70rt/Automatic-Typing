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

# Default Values
time_speed = 0.5
loop = True    
ch2 = 77
temp2 = False


class Settings:
    
    def AppendList(self, x):
        len1 = len(x)
        dummy_list = []
        for i in range(0, len1):
            for j in x[i] [::-1]:
                dummy_list.append(j)
            if i < len1 - 1:
                dummy_list.append(" ")
        return dummy_list
    
    def Developer(self):
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
    
    def TextSettings(self):
        
        print("Settings:")
        print(" 33 to Change Typing Speed")
        print(" 44 to Change Output Text Format")
        print(" 55 to Back")
    
        ch1 = int(input("\n>>>>> "))
    
        if ch1 == 33:
            global time_speed
            print("The Typing Speed is ", time_speed, "(Default : 0.5) [Range : 0 < x < 10]")
            print("Enter The Typing Speed")
            time_speed = float(input(">>>>> "))
            
            clear = lambda: os.system('cls')
            clear()
    
        elif ch1 == 44:
            clear = lambda: os.system('cls')
            clear()
            
            add.Developer()
            
            print()
            print(" 66 to Change Every Character to Uppercase")
            print(" 77 to Change Every First Char. Of Word To Uppercase")
            print(" 88 to Disable Over-writing of Characters")
            global ch2
            ch2 = int(input(">>>>>> "))
    
        elif ch1 == 55:
            global temp2
            temp2 = False
            clear = lambda: os.system('cls')
            clear()
            
        else:
            print("\nInvalid Option")
            clear = lambda: os.system('cls')
            clear()
            
        return temp2
    
    def CapitalizeWords(self, x):
        words = x.split()
     
        for x in range(len(words)):
            words[x] = words[x] [::-1]
            words[x] = words[x].capitalize() 
    
        return words

add = Settings()

while loop == True:
    add.Developer()
        
    print("Enter:")
    print(" 11 to Start")
    print(" 22 for Settings")
    print(" 00 to Exit...")

    print()
    ch = int(input(">>>>>> "))
    print()

    if ch == 11:
        name = input("Enter Sentence : ") [::-1]
        t = len(name)
        
        if ch2 == 66:
            name = name.upper()
            list_name = list(name)
        
        elif ch2 == 77:
            name = name.lower()
            list_name = add.CapitalizeWords(name)
            list_name = add.AppendList(list_name)
        
        elif ch2 == 88:
            list_name = list(name)
        
        print()
        clear = lambda: os.system('cls')
        clear()
        
        add.Developer()
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
        clear = lambda: os.system('cls')
        clear()
        
        add.Developer()
        checkSettings = True
        while checkSettings == True:
            checkSettings = add.TextSettings() 
    
    else:
        temp = input("Invalid Option Press [Enter] to Try Again...")
    
    clear = lambda: os.system('cls')
    clear()
   
