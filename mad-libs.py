def getKeywords(formatString):
    # Returns a list of all the key word strings.
    keywordList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1  # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start: end]
        keywordList.append(key)  # may add duplicates

    return set(keywordList)  # removes duplicates: no duplicates in a set


def addWord(word, dictionary):
    # Prompts user then saves prompts in a dictionary
    promptFormat = "Enter a {name}:  "
    prompt = promptFormat.format(name=word)
    response = input(prompt)
    dictionary[word] = response


def getUserWords(words):
     # loops through added words to get user words and saves them to dictionary
    userWords = dict()
    for word in words:
        addWord(word, userWords)
    return userWords


def tellStory(storyFormat):
     # gets key words and user words and formats the story
    words = getKeywords(storyFormat)
    userWords = getUserWords(words)
    story = storyFormat.format(**userWords)
    print(story)


# Initialize Story


def main():
    originalStoryFormat = '''
Once upon a time, deep in an ancient jungle,
there lived a {animal}.  This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer.  One day, an
explorer found the {animal} and discovered
it liked {food}.  The explorer took the
{animal} back to {city}, where it could
eat as much {food} as it wanted.  However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End
'''
    tellStory(originalStoryFormat)
    input("Press Enter to end the program.")


main()
