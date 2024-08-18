from termcolor import colored
import os

os.system("cls")

#--------------------------------------------------------
# Ma'lumotlarni olish
jins = input('Jinsingizni kiriting: Erkak[E] / Ayol[A]: ').lower()
yosh = int(input("Yoshingizni kiriting: "))
#-------------------------------------------------------

# Ayollar
def pensiya_ayol(yosh):
    if yosh >= 55:
        print(colored('Siz pensiyaga chiqgansiz!', 'green', 'on_red'))
    elif yosh < 55:
        chiqishi = 55 - yosh
        tt = f'Siz {chiqishi} yildan keyin pensiyaga chiqasiz'
        print(colored(tt, 'blue', 'on_blue'))
    else:
        print(colored("Qandaydir xatolik", 'red'))

# Erkaklar
def pensiya_erkak(yosh):
    if yosh >= 60:
        print(colored('Tabriklayman! Siz pensiyaga chiqgansiz!', 'green', 'on_red'))
    elif yosh < 60:
        chiqishi = 60 - yosh
        tt = f"Siz {chiqishi} yildan keyin pensiyaga chiqasiz"
        print(colored(tt, 'blue', 'on_blue'))
    else:
        print(colored("Qandaydir xatolik", 'red'))

#routing
if jins == 'a':
    pensiya_ayol(yosh)
elif jins == 'e':
    pensiya_erkak(yosh)
else:
    print(colored("Siz noto'g'ri jins tanladingiz, iltimos namunada ko'rsatilgandek qiling!", 'light_red'))

