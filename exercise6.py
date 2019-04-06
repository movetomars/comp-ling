#LING 5410
#Maia Petee

#Exercise 6: Dictionaries, User Input, and Reading Files

#1. Adapted from Python Crash Course, Chapter 6, Exercise 6-11 (p. 115)

#Make a dictionary called languages.

languages = {}

# Use the names of three languages as keys in your dictionary.

languages = {'Russian', 'Japanese', 'Spanish'}

# Create a dictionary of information about each language and include the main country (or countries) that the language is
#spoken in, its approximate number of speakers, and one fact about that language. The keys for each
#language’s dictionary should be something like location, speakers, and fact.

languages = {
    'Russian': {
        'countries':'Russia',
        'numberSpeakers':166000000,
        'fact':'Does not have auxiliary verbs.'
    },
    'Japanese': {
        'countries':'Japan',
        'numberSpeakers':126000000,
        'fact':'Marks subjects and objects with particles.'
    },
    'Spanish': {
        'countries':['Spain', 'Mexico', 'Argentina', 'Bolivia', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama', 'Paraguay', 'Puerto Rico', 'Uruguay', 'Venezuela'],
        'numberSpeakers':420000000,
        'fact':'Determiners and adjectives must agree with nouns in number and gender.'
    }
}

#Print the name of each language and all of the information you have stored about it.

for language, languageInfo in languages.items():
    print('Language: ' + language)

    country = languageInfo['countries']
    speakers = str(languageInfo['numberSpeakers'])
    fact = languageInfo['fact']

    #We have a list here - all the countries that speak Spanish. This will require some different code.
    if isinstance(country, str) == False:
        print("It is spoken in ")
        for place in country:
            print(place)
    #If it's a simple string, printing is easy.
    else:
        print("It is spoken in " + country + ".")

    print("It has " + speakers + " speakers.")
    print(fact + "\n")

#2. Python Crash Course, Chapter 7, Exercise 7-10 (p. 131)
#Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one
#place in the world, where would you go? Include a block of code that prints the results of the poll.

dreamVacay = input("If you had two weeks to be wherever you wanted in the world, where would it be? ")

print("You would go to " + dreamVacay + "? How fascinating!")


#3. Write a program	that reads some text files found in Project Gutenberg, and count how many times the word "the" appears in them.

#I found a text file of "Astounding Stories," delightful pulp sci-fi from the 1930s.

def the(filename):
    try:
        with open(filename) as file:
            text = file.read()
            #Converts all instances of "the" to lowercase before counting
            the = text.lower().count('the')

        print(the)
    except FileNotFoundError:
        msg = "Sorry, this text " + filename + " can't be found."
        print(msg)

filename = 'AstoundingStories.txt'
the(filename)