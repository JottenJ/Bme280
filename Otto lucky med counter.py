import random


def fav():
    luckynum = random.randint(1, 10)
    guesscount = 1
    print("Enter a lucky number between 1 and 10")
    while True:
        num_str = input("What is the lucky number?: ")
        if not num_str.isdigit():
            print("håll nu fingrarna bara på siffrorna, tack!")
            continue
        num = int(num_str)
        if num == luckynum:
            print(f"Grattis! Du gissade rätt i {guesscount} försök")
            break
        else:
            print("Fel gissat, försök igen!")
            guesscount += 1


fav()
