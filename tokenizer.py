# LING 5410
# 31 January 2019
# Maia Petee

# Building a simple tokenizer for English

# Let's make sure we have Regex imported.
import re

# First we need to take user input and store it as a string in a variable
sentence = input("Hi there. Please enter a string you'd like to be tokenized: ")
print("Thank you!")

# Now we need to split it into a list in a basic way.
list = sentence.split()

# Initializing a new list to add tokenized words to later.
newList = []

# We still have contractions and punctuation grouped with words.
# We need to iterate across each word and search for these.

for item in list:
    # Initializing another new list to temporarily store concatenated contractions when they appear.
    endings = []
    # First, we need to search for contractions, and
    # (1) Split the last two letters of the word into their own token.
    # (2) If there's a "n't", "'ll", or "'ve" involved, make sure to include the entire split form
    if "'" in item:

        while "'" in item:

            if re.search(r"(n't\b|'ve\b|'ll\b|'re\b)", item):
                newending = item[-3:]
                item = item[:-3]
                endings.insert(0, newending)
            elif re.search(r"'all$", item):
                newending = item[-4:]
                item = item[:-4]
                endings.insert(0, newending)
            # elif re.search(r"'\w{4,}",item):
            # item = item
            else:
                newending = item[-2:]
                item = item[:-2]
                endings.insert(0, newending)

        # Then we add the newly truncated form to the final list of tokens, followed by all contractions that have been stripped.
        newList.append(item)
        newList.extend(endings)

    # We also need to search for any instances of common punctuation, and split those off into new items.
    elif re.search(r"(\?|!|,|\.)", item):
        punctuation = item[-1]
        item = item[:-1]
        newList.append(item)
        newList.append(punctuation)

    # If a word contains neither of these, it will be added to the new list unchanged.
    else:
        newList.append(item)

# The tokenized list has been created. Let's see it!
print(newList)