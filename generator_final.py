#LING 5410
#Maia Petee

#Midterm - Automatic Text Generation in a Particular Style (Based on a Conditional Frequency Distribution)

#First, let's take care of all the modules we need for this task

import random
import nltk

#Now let's make a function that takes a number of words and a specific text (the training text) as parameters.
def generateText(num, file):

    #Read the text in the file, and create a NLTK Text object that can have NLTK methods used on it.
    with open(file) as text:
        data = text.read().split()
        data = nltk.Text(data)

    # We want to take our text and create a frequency distribution of all the words therein.
    sciDist = nltk.FreqDist(data)

    # We will also need to grab the hundred most common words in this distribution, so we can pick one at random as a "start point."
    # Before we do this, we want to make sure to select only the word - not the frequency (an integer).
    words = sciDist.most_common(100)
    words = [w[0] for w in words]

    # Choosing the start word and capitalizing it!
    word = random.choice(words).title()

    #Next, we need to create a list of bigrams found in the text. We will use these to calculate the most common sequences of 2 words.
    scigrams = nltk.bigrams(data)

    #Finally, we create a conditional frequency distribution - the probability of a word given the existence of a previous target word.
    sciDistCond = nltk.ConditionalFreqDist(scigrams)

    #Here we make the same probabilistic calcuation num number of times.
    for i in range(num):
        #We print our target word with a space after it
        print(word, end=' ')
        #Calculate the 5 most common words that follow this word in out training data
        common = sciDistCond[word].most_common(5)
        #Choose one of those at random...
        strip = random.choice(common)
        #And make sure we grab the word, only the frequency.
        word = strip[0]
    print("\n")

#Telling the function to generate fifty words of science fiction, 50 words of Bertrand Russell, and 50 words of a strange, strange hybrid.
generateText(50, "Texts/astoundingstories0.txt")
generateText(50, "Texts/russell0.txt")
generateText(50, "Texts/combined0.txt")

#The output is almost intelligible - when I ran it it had some dialogue, some character names, and a distinctly pulpy feel. It was also somewhat surreal,
#and frequently not grammatically sound. All in all I could tell what data the model had been trained on.

#The hybrid data, which is Bertrand Russell and pulp sci-fi combined, is significantly less intelligible than the single-genre data. It seems to be more
#meandering, and it seems to have more function words and fewer content words. Names and dialogue do not appear.

#I also trained the model on pure Bertrand Russell, and that is also quite unintelligible. It could be that since Bertrand has a much larger
#lexicon than the pulp sci-fi, most of his content words are low-frequency and will not come up in the top 5 choices. Exceptions seem to be "doubt,"
#"mind," and "man," but these are interspersed by deserts of function words strung together.