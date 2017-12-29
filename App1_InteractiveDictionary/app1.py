import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys()))>0:
		yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
		if yn=="Y":
			return data[get_close_matches(word,data.keys())[0]]
		elif yn == "N":
			return "The word does n't exist. Please double check your entry."
		else :
			return "We did n't understand your entry."

	else:
		return "The word does n't exist. Please double check it."
	

word = input("Enter word:")
print(translate(word))
