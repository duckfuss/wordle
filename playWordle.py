import random
random.seed(10)
linkList = open("data/linkFile.txt").read().splitlines()
scoreList = open("data/scoreFile.txt").read().splitlines()
answers = open("data/answers.txt").read().splitlines()

def fancyPrint(green, yellow):
    printy = ['⬛️','⬛️','⬛️','⬛️','⬛️']
    for (char, index) in green:
        printy[index] = "🟩"
    for (char, index) in yellow:
        printy[index] = "🟨"
    print("".join(printy))

def printHistogram(data, total):
    while data[-1] == 0:
        data.pop()
    for i in range(len(data)):
        num = data[i]
        mult = round((num * 50)/total)
        if mult != 0:
            string = "|" * mult
        else:
            string = "."
        print("{:02d}".format(i),"⏐" + string)

def addFreqs(listy):
    tot = 0
    for i in range(len(listy)):
        tot += listy[i]*i
    return tot

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

    

def nextValid(list, greenList, yellowList, blackList, attempt=10):
    greenLetters = []
    for char, index in greenList:
        greenLetters.append(char)
    yellowLetters = []
    for char, index in yellowList:
        yellowLetters.append(char)
    blackLetters = []
    for char, index in blackList:
        blackLetters.append(char)

    for word in list:
        wrong = False
        for char, index in greenList:
            if word[index] != char: # and attempt > 1: # doesn't
                wrong = True
        for char, index in yellowList:
            if char not in word:
                wrong = True
            elif word[index] == char:
                wrong = True
        for char in blackLetters:
            if char in word:
                wrong = True
        if wrong:   continue
        else:       return word

def playGame(ans, priorityList, log=True):
    word = priorityList[0]
    green, yellow, black = [], [], []
    for j in range(12):
        g, y, b = likeness(word, ans)
        green = list(set(green) | set(g))
        yellow = list(set(yellow) | set(y))
        black = list(set(black) | set(b))
        if log: fancyPrint(g, y)
        word = nextValid(priorityList, green, yellow, black, attempt=j)
        if len(green) == 5:
            if log: print("success!", j, "\n")
            break
    return j


attemptsS = [0] * 15
attemptsL = [0] * 15
games = 1000
priorityList = scoreList # change me
for i in range(games):
    if i % 50 == 0:    log = True
    else:   log = False
    ans = answers[random.randrange(0,len(answers))]
    if log:
        print("---------", i, ans)
    if log: print("\nscoreList")
    attemptsS[playGame(ans, priorityList=scoreList, log=log)] += 1
    if log: print("linkList")
    attemptsL[playGame(ans, priorityList=linkList, log=log)] += 1

print("\nscore based:")
printHistogram(attemptsS, games)
print("average no. attempts:", addFreqs(attemptsS)/games)
print("\nlink based:")
printHistogram(attemptsL, games)
print("average no. attempts:", addFreqs(attemptsL)/games, "\n")