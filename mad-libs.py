def getKeywords (formatString):
    #Returns a list of all the key word strings.
    
    keywordList = list()
    end = 0
    reps =  formatString.count('{')
    for i in range (reps):
        start = formatString.find('{', end) + 1
        end = formatString.find('}', start)
        keyword = formatString[start : end]
        keywordList.append(keyword)

    return (keywordList)

# def getInput (prompt):
#     userInput = input(prompt)
#     return userInput

def addWord (word, dictionary):
    #Prompts user then saves prompts in a dictionary
    promptFormat = "Enter a {name}: "    
    prompt = promptFormat.format(name=word)
    response = input(prompt)
    dictionary[word] = response

def getUserWords (words):
    #loops through added words to get user words and saves them to dictionary
    userWords = dict()
    for word in words:
        addWord(word, userWords)
    return userWords

def tellStory (storyFormat):
    #gets key words and user words and formats the story
    words = getKeywords(storyFormat)
    userWords = getUserWords(words)
    story = storyFormat.format(userWords)
    print (story)

#Initialize Story
def madLib():
    theStory = '''
    There once was a {animal}, that
    was very {adjective}. Everyone in {place}
    knew about this and decided to {verb} until
    {celebrity}. Causing the next town over to {verb}.
    '''

    tellStory(theStory)
    input("Press Enter to end the program.")        


madLib()