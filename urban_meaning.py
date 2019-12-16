from requests_html import HTMLSession
import pyperclip
import os


session = HTMLSession()
#InputA = open('lib/temp_keyword.txt', 'r')

InputB = input("Type in keyword: ")
if "/" in InputB:
    InputC = InputB[-1:]
    InputB = InputB[:-2]
    url = session.get('https://www.urbandictionary.com/define.php?term='+ InputB)
    
    meaning = url.html.find('.meaning', first = False)
    keci = int(InputC)-1
    print(meaning[keci].text)
    pyperclip.copy(meaning[keci].text)
else:
    url = session.get('https://www.urbandictionary.com/define.php?term='+ InputB)
    meaning = url.html.find('.meaning', first = False)
    print(meaning[0].text)
    pyperclip.copy(meaning[0].text)




os.system('pause')

