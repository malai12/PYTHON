import random
import pyautogui

chs = "abcdefghijklmnopqrstuvwxyz"
ch_list = list(chs)

passwd = pyautogui.password("Enter the password: ")

guess_passwd = ""

while(guess_passwd!=passwd):
    guess_passwd = random.choices(ch_list,k=len(passwd))
    print("<=============== "+str(guess_passwd)+" =================>")
    if guess_passwd == list(passwd):
        print("Your password is : " + "".join(guess_passwd))
        break
