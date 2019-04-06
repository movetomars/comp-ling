#LING 5410
#Maia Petee

#Homework 2: Answering a Text-Based Question with Regular Expressions

#To answer this question, I'm going to write a function to detect and display all the utterances of a particular character in a story/novel.
#The text I'm using is from 1930; it's from a delightful science-fiction pulp serialization called "Astounding Stories."
#The character I'm grabbing utterances from is Dodd, or Jimmy Dodd, an adventurer in a prehistoric land.

import re

def utterances(text, character):

    #This character search goes through each sentence, and searches for a pattern of two quotation marks with anything inside them -
    #Except more quotation marks! We also want to eliminate the use of "to" before our target character, because that guarantees
    #That someone else is saying something TO them; they're not saying it themselves.
    #We then want to search the character's name, and then allow for any additional non-quotation expansion.
    charsearch = r"\"[^\"]*\"[^(\"|to)]*" + re.escape(character) + r"[^\"]*"

    #Initializing a list to add the character's statements to.
    statements = []

    #Opening our file parameter
    with open(text) as content:

        #If the file given is a valid file path:
        try:

            con = content.read()
            #This will take the text and split it into sentence-sized chunks. I decided to split on multiple characters, despite the fact
            #that it will truncate some utterances - without this, another character's lead-in utterances were also being captured.
            sentence = re.split('\.|\?|!', con)

            for s in sentence:
                #Searching each sentence for our target Regex
                if re.search(charsearch, s):
                    #Add each sentence where the quotations and character are present to the list.
                    statements.append(s)

        #If the file given is not a valid file path:
        except FileNotFoundError:

            error_message = "Sorry, the file you'd like analyzed, " + text + ", does not exist."
            print(error_message)

        #Printing out all our character's utterances.
        #Don't forget to add the period back in!
        for state in statements:
            print(state + ".\n")

        #Message if nothing is found.
        if len(statements) == 0:
            print("It doesn't seem like this person says anything.")


#Calling the function with Mr. Dodd and our desired pulp sci-fi! Feel free to call your own.
utterances("Texts/astoundingstories.txt", "Dodd")

#There's a very long way to go, but I am happy that everything I am getting is something said by the character.