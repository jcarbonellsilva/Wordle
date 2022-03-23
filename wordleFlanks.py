import pandas as pd
from colorama import init, Fore, Back, Style
# https://www.geeksforgeeks.org/print-colors-python-terminal/
import random
init()

df = pd.read_excel("D:\VSCode-Py\Python\Scraping\wordle_words.xlsx")

def list_of_words(dataframe):
    """
    Given a DataFrame with the game words, 
    this function will create a list with these words.

    dataframe - dataframe you want process.
    IT IS A MUST THE COLUMN WORDS HAS A COLUMN NAMED ['words']
    """
    wordList = []
    for i in df['words']:
        wordList.append(i)
    return wordList

loop = True

while loop:
    print(Back.WHITE + Fore.BLACK + "Nou joc: si/no" + Style.RESET_ALL)
    inp = input()
    if (inp == "No" or inp == "no"):
        loop = False
        print("Fins la pròxima!")
    elif (inp == "si" or inp == "Si"):
        intent = 0
        paraula = random.choice(list_of_words(df))

        print("Escriu una paraula ;)")
        while intent < 7:
            while intent < 6:
                bona_sort = input()
                if (len(bona_sort)!=5):
                    print("La paraula ha de tindre 5 lletres...")
                else:
                    sortida = ""

                    for i in range(len(paraula)):
                        if bona_sort[i] == paraula[i]:
                            sortida = sortida + Back.GREEN + bona_sort[i] + Back.RESET
                            
                        elif bona_sort[i] in paraula:
                            sortida = sortida + Back.YELLOW + bona_sort[i] + Back.RESET
                            
                        else:
                            sortida = sortida + Back.WHITE + bona_sort[i] + Back.RESET
                            
                    print(sortida)
                    if paraula == bona_sort:
                        print("L'has clavat!")
                        intent = intent + 10
                    intent = intent + 1
            
            print("La paraula correcta es: {}".format(paraula))
            intent = intent + 1






  
  
      
        