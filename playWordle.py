import random

linkList = open("data/linkFile.txt").read().splitlines()
scoreList = open("data/scoreFile.txt").read().splitlines()
answers = open("data/answers.txt").read().splitlines()


def likeness(word1, word2):
    green, yellow, black = [], [], []
    for i in range(5):
        if word1[i] == word2[i]:
            green.append((word1[i], i))
        elif word1[i] in word2:
            yellow.append((word1[i], i))
        else:
            black.append((word1[i], i))
    for letter, index in yellow: # discard duplicate yellows
        word1Tot = yellow.count(letter) + green.count(letter)
        word2Tot = word2.count(letter)
        diff = word1Tot - word2Tot
        if diff > 0:
            for i in range(diff):
                yellow.remove(letter)
    return green, yellow, black

def fancyPrint(green, yellow):
    printy = ['⬛️','⬛️','⬛️','⬛️','⬛️']
    for (char, index) in green:
        printy[index] = "🟩"
    for (char, index) in yellow:
        printy[index] = "🟨"
    print("".join(printy))

def nextValid(list, greenList, yellowList, blackList):
    greenLetters = []
    for char, index in greenList:
        greenLetters.append(char)
    yellowLetters = []
    for char, index in greenList:
        yellowLetters.append(char)
    blackLetters = []
    for char, index in blackList:
        blackLetters.append(char)

    for word in list:
        wrong = False
        for char, index in greenList:
            if word[index] != char:
                wrong = True
        for char, index in yellowList:
            if word.count(char) < yellowLetters.count(char) + greenLetters.count(char):
                wrong = True
            if word[index] == char:
                wrong = True
        for char in blackLetters:
            if char in word:
                wrong = True
        if wrong:   continue
        else:       return word
        

for i in range(2):
    ans = "refer"#answers[random.randrange(0,len(answers))]
    word = linkList[0]
    green, yellow, black = [], [], []
    print("NEW GAME")
    print("CORRECT:", ans)
    for j in range(6):
        g, y, b = likeness(word, ans)
        green = green + g
        yellow = yellow + y
        black = black + b
        fancyPrint(g, y)
        print(word)
        print(green, yellow, black)
        word = nextValid(linkList, green, yellow, black)
        if len(green) == 5:
            print("success!")
            break

# SEELT SOREE
# BYYBB