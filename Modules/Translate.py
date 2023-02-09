from Data.Words import words

from Modules.Mathematics import Mathematics
from Modules.String import String
from Modules.Utils import Utils

class Translate:

    def Render(): 
        print()

        boolean = Mathematics.GetRandomBoolean()

        if (boolean == 0): 
            Translate.EnglishTranslate()
        if (boolean == 1): 
            Translate.RussianTranslate()

    def EnglishTranslate():

        word = words[Mathematics.GetRandomInteger(len(words))]

        if (len(word["english.description"]) == 0):
            print(Utils.Message("Как переводится слово", "white") + " - " + String.JoinWithColor(word["english"], "blue"))
            Utils.Speech(String.Join(word["english"]), "en")
        else:
            print(Utils.Message("Как переводится слово", "white") + " - " + String.JoinWithColor(word["english"], "blue") + " ( " + Utils.Message(word["english.description"], "yellow") + " )")
            Utils.Speech(String.Join(word["english"]), "en")

        answer = input("Введите слово: ")

        if (answer.lower() in word["russian"]): 
            print(Utils.Message("Правильно.", "green"))
        else: 
            print(Utils.Message("Неправильно.", "red"))

        print(Utils.Message("Правильные слова", "white") + ": " + String.JoinWithColor(word["russian"], "green"))

        Translate.Render()

    def RussianTranslate():

        word = words[Mathematics.GetRandomInteger(len(words))]

        if (len(word["russian.description"]) == 0):
            print(Utils.Message("Как переводится слово", "white") + " - " + String.JoinWithColor(word["russian"], "blue"))
            Utils.Speech(String.Join(word["russian"]), "ru")
        else:
            print(Utils.Message("Как переводится слово", "white") + " - " + String.JoinWithColor(word["russian"], "blue") + " ( " + Utils.Message(word["russian.description"], "yellow") + " )")
            Utils.Speech(String.Join(word["russian"]), "ru")

        answer = input("Введите слово: ")

        if (answer.lower() in word["english"]): 
            print(Utils.Message("Правильно.", "green"))
        else: 
            print(Utils.Message("Неправильно.", "red"))

        print(Utils.Message("Правильные слова", "white") + ": " + String.JoinWithColor(word["english"], "green"))

        Translate.Render()