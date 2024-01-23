﻿from datetime import *
from random import *
from math import *
#Ülesanne 13
print("Arv Ruut kuup")
print()

for i in range(1,11):
    ruut = i ** 2
    kuup = i ** 3
    print(f"{1:2} {ruut:2} {kuup:3}")
#Ülesanne 11
from random import *
number=randint(1,100)
katsed=3
while katsed>0:
    külaline = int(input("Угадайте число от 1 до 100"))
    if külaline == number:
        print("Поздравляем, вы угадали число")
        break
    else:
        katsed -= 1
        print(f"Неверно у вас осталось {katsed} попыток")
        if katsed -- 0:
            print(f"Извините, вы использлвали все попытки. Загаданное число было {number}.")
            veelkord = input("Хотите ли угадать?: ").lower()
            if veelkord.lower()=="нет":
                break
            else:
                katsed=3
#Ülesanne 8.2
paaris=0
paaritu=0
for i in range(1, 101):
    if i%2==0:
        print(f"{i}-paaris")
        paaris+=1
    else:
        print(f"{i}-paaritu")
        paaritu+=1

print(f"Paarisarvude arv: {paaris}")
print(f"Paaritute arvude arv: {paaritu}")

#Ülesanne 8.1
for arv in range(1, 101):
    if arv % 5 == 0:
        print(arv)
#Ülesanne 10
for arv in range(1, 101):
    if arv % 5 == 0:
        print(arv)
for i in range(1,6):
    derivative= i * (i - i)
    print(f"GH {i} d {derivative}")

#Ülesanne 9.2
korrutamine=["5"]
arv=["1","2","3","4","5","6","7","8","9","10",]
for i in range(10):
    tulemus = int(arv[i]) * 5
    print(f"{arv[i]} * 5 = {tulemus}")
#Ülesanne 9.1
korrutamine=5
for i in range(1,11):
    tulemus=(i) * 5
    print(f"{i} * 5 = {tulemus}")
#Ülesanne 7
number = ["3","3","5","6","9",]
for num in number:
    print(num)
#Ülesanne 3
k=0
while True:
    k+=1
    a=randint(1,50)
    b=randint(1,50)
    p=0
    v=-1000
    while p!=3:
        p+=1
        v=int(input("Millega võrdub {0}+{1}".format(a,b)))
        if v==a+b:
            print("Tubli!")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(a,b,a+b))
    if k==5:break
#Ülesanne 2
summa=0
for i in range(10):
    arv=float(input("Sisesta arv: "))
    summa+=arv
print(summa)

summa=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta arv: "))
    summa+=arv
    if i==10: break
print(summa)

#Ülesanne 1
nimi=input("Mis in sinu nimi?")
mitu=int(input("Mitu korda tervitada?"))
for i in range(1,mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")

#Praktiline töö "Tsükkel"
a=["8:30","9:20","10:10","11:05","11:55",]
b=["9:15","10:05","11:00","11:50","12:35",]
for i in range(5):
    print(a[i]+"-"+b[i])

#komm
print("1. variandt -while True-")
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. variandt -while tingimusega-")
v=""
while v!="komm":
    v=input("Tahan komme!").lower()

#Nädala päevad
paevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev",]
tunnid=["8 tundi","9 tundi","5 tundi","8 tundi","8 tundi","tunde pole","tunde pole",]
for i in range(7):
    print(paevad[i]+"-"+tunnid[i])

#8 Poes koeduslaused
arve_nr=datetime.now() # date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
tooded=["Piim","Leib","Komm"] #index 0-1-2
for i in range(3): #(0,3,1) #i=0, i=1, i=2
    toode=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
       mitu=int(input("Mitu?"))
       tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
       summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
