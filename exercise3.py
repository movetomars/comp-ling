#LING 5410
#26 January 2019
#Exercise 3

#3.4 - 3.7 - Make a list of at least three people you'd like to invite to dinner.

idealGuests = ["Jane Austen", "Emily Dickinson", "Ada Lovelace", "Marie Curie"]

#Be sure to actually invite them all!


for guest in idealGuests:
    print(guest + ", would you care to dine at my house this evening?")

#But it looks like someone has RSVPed "no."

negRSVP = idealGuests[3]

print("It looks like " + negRSVP + " can't make it, for perfectly valid radiation-poisoning-related reasons.")

#Who else to invite?

idealGuests.remove(negRSVP)
idealGuests.append("Ursula Le Guin")

for guest in idealGuests:
    print(guest + ", would you care to dine at my house this evening?")

#There's now more room, too. I'll invite three more writerly guests

print("It looks like I have three more place settings after all.")

idealGuests.insert(0, "Ann Leckie")
idealGuests.insert(3, "N.K. Jemisin")
idealGuests.append("Isaac Asimov")

for guest in idealGuests:
    print(guest + ", would you care to dine at my house this evening?")

#There's now LESS room. This is awkward.

print("This is awkward, everyone, but it looks like I'll only have space for two guests.")


#Disinviting people:

while True:
     disinvited = idealGuests.pop()
     print("Sorry about this, " + disinvited + ".")
     if len(idealGuests) < 3:
        break


#Letting Ann Leckie and Jane Austen know they're still welcome.

for guest in idealGuests:
    print(guest + ", no worries - I can still feed you!")


while True:
    del idealGuests
    if len(idealGuests > 0):
            break


#You know what, maybe we should just cancel altogether.

del idealGuests[0]
del idealGuests[0]

print(idealGuests)


#3.11 - List error - you mean no one's invited anymore?

print(idealGuests[-1])

#3.10 - Creating a list and manipulating it using EVERY method in chapter.

snacks = ["popcorn", "beef jerky", "gummy candy", "taquitos", "chocolate"]

#Accessing a list item
print(snacks[0])

#Printing a list item in another message

hunger = "I love " + snacks[0]
print(hunger)

#Append

snacks.append("popsicles")
print(snacks)

#Insert

snacks.insert(-1, "chips")
print(snacks)

#Remove

del snacks[-1]
print(snacks)

#Pop

ateItAll = snacks.pop(2)
print(snacks)
print(ateItAll)

#Remove

myFavorite = "popcorn"
snacks.remove(myFavorite)
print(snacks)

#Sort

snacks.sort(reverse = True)
print(snacks)

#Temporarily Sort

print(sorted(snacks))

#Reverse

print(snacks)
snacks.reverse
print(snacks)

#Length

print(len(snacks))
