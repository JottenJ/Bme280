print("Enter a lucky number")
def fav():
    guesscount = 0
    while True:
        num = int(input("What is the lucky number?: "))
        if num == 5:
            print(f"Grattis! Du gissade rätt i {guesscount} försök")
        else:
            print("Fel gissat, försök igen!")
            guesscount += 1

fav()
