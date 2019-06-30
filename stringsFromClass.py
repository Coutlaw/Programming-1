def lists():
    name =["jackson", "andrew", "josh", "cass"]
    nums = [1,2,3]

    #name + num = jackson, andrew, josh, cass, 1, 2, 3
    #num * 4 = 1,2,3,1,2,3,1,2,3,1,2,3
    #len(num) = 3
    #name[1] = andrew
    #name[:3] = jackson, andrew, josh -> comes back as a list
        #means number of items
    #name[len(name) - 1] = cass
    #name[5] = index out of range error
    #for name in range(len(name)):
        #print(name[i])
    #= names printed down
    #name[2:4] = josh, cass
    #   because it is positions 2 and 3 printed
    #name[0] is not equal to name[0:1]
    #name [0] is a string
    #name[0:1] is a list

    names = ["jackson", "andrew", "josh", "cass"]

##    names[1][2] - > yields the item andrew and takes the 2nd sub
    # gives you the string "d"
    
##    when going into a list think about what you are returning
    
#    values = [3, "hi", 5.5, Ball]
#    val0 = value[0]


def strings():

    # common terms: conncatination = adding
    #               string = collection of information
    #               index possition = location of a character in string
    #strings are imutable (cant change)

    #string.upper() makes uppercase

    place = "Charleston is cool"
    place.upper()
    # retruns an upper case string
    
    place.lower()
    #retruns lowercase string

    place.capitalize()
    #returns the first letter of the string as capital

    place.title()
    # returns the first letter of all words capitalized

    place.center(30)
    # sets asside 30 spaces and centers the string

    # you can use muttiple methods
    place.center(40).title()
    # executs the center and title method

    place.center(40, "*")
    #retruns the centered string with "*" takeing up the empty spaces

    
    # ITEMS NOT IN LIST WILL RETRUN A -1
    # methods will only retrun what is searched
    place.find("a")
    #retruns index possition of the first "a" in string

    place[3:].find("a")
    #slices the string after the first "a" and looks for the next

    place.count("a")
    #counts the ammount of "a"'s in the series

    place.replace("a", "aaa")
    #            (old,  new, index number to modify)
    #finds the first value "a" and replaces it with "aaa"
    place.replace("a", "aaa", 2)
    # will only replace the "a" with "aaa" for first two it finds

    

    
    # this loses the original string and creates a new one. does not
    # mutate the original string
    # the variable place is reasigned to the new varialbe place and
    # overwritten
    place = place.upper()

def stringSlicing():

    #things you can do to a string
    name = "Nhan"

    #SLICING returns a string
    #SPLITTING retruns a list of strings

    #SLICING
    #takes 2 index position to end of string
    namePart = name[2:]
    #returns a STRING of : "an"

    phrase = "2 cool 4 school"
    #METHOD
    #SPLITTING method
    wordList = phrase.split()
    #retruns ["2", "cool", "4", "school"]
    #split command removes white space and turns all values into list


    #JOINING
    #joining is string class method
    #separator.joint(listOfStrings)
    "*".join(wordList)
    #will rejoin the wordList with "*" in between each individual string

    #compound methods
    newPhrase = "---".join(phrase.split())
    #returns phrase with "---" between each word

    #splitting into what we just made
    newPhrase.split("---")
    # will break back up by the separator which is normaly white space
    

def counting():
    sent = "cass joe katie jack"
    words = sent.split()
    print(words)
    len(words)
    num = sent.count("a")
    denom = len(words)
    avg = num / denom

def sent():
    sent = "Katie Jack Hitarth Zhou"
    #trun into kaTie jaCk hiTarth zhOu"
    namesList = sent.split()

    string = " "
    for name in namesList:
        name = name[:2].lower () + name[2:].capitalize()
        print(name)
        string += name + " "
    print(string)

    newString = string[len(string) - 1]
    shorterString = newString[:1]
    print(newString)
    print(shorterString)

def username():
    email = "outlawcd@g.cofc.edu"
    username = email.split("@") [0]
    # bracket [0] prints the first item in list
    print(username)

##getting info from a file

def countWords():
    paragraph = "How are   \n\t  you today. Well  I hope."
    first = paragraph.split(".") [0]
    second = paragraph.split(".") [1]
    #list will have three items because you are not using the default
    # split command with white space
    print(first)
    print(second)
    firstWords = first.split()
    secondWords = second.split()
    print(firstWords)
    print(secondWords)

    # use loop to finnish

    
    # count the number of characters in the given paragraph using
    # string only methods
def countWords2():
    paragraph = "how are  \n\t you today. Well   I hope."
    firstList = paragraph.split(".") [0]
    secondList = paragraph.split(".") [1]

    firstList2 = firstList.split()
    secondList2 = secondList.split()
    

    words1 = "".join(firstList2)
    words2 = "".join(secondList2)
  
    characters1 = len(words1)
    characters2 = len(words2)

    total = characters1 + characters2

    print(total)

    
    
    
    
        

    
    
    
    
    
    




    
