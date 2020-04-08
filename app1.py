import json
from difflib import get_close_matches


data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        res = input("Did you mean [%s]? Enter Y if yes or N if No \n"  % get_close_matches(word,data.keys())[0])
        if res == 'Y' or res == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif res =='N' or res == 'n': 
            return "The word doesn't exist. Please try again"
        else: 
            return "We didn't understand the entry"       
    else:
        return "The word doesn't exist. Please try again"



word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)