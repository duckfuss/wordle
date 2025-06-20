import time
start = time.time()

answers = open("answers.txt").read().splitlines()
allowed = open("allowed.txt").read().splitlines()

print(len(allowed), len(answers))

def printTopN(dict, n):
    c = 0
    for key, value in dict.items():
        c += 1
        if c > n:  break
        print(c, key, value/2315)


def likeness(word1, word2):
    green, yellow = [], []
    for i in range(5):
        if word1[i] == word2[i]:
            green.append(word1[i])
        elif word1[i] in word2:
            yellow.append(word1[i])
    for letter in yellow: # discard duplicate yellows
        word1Tot = yellow.count(letter) + green.count(letter)
        word2Tot = word2.count(letter)
        diff = word1Tot - word2Tot
        if diff > 0:
            for i in range(diff):
                yellow.remove(letter)
    similarity = (len(green)/5) + (len(yellow)/10)
    return similarity

def exploreGraph(word, totalScoreDict, linkDict):
    for (link, linkStrength) in linkDict[word]:
        pass
    pass

# 1. brute force compare every word with every other word
totalScoreDict = {}
linkDict = {}
linkThreshold = 0.3
for i in range(len(allowed)):
    allow = allowed[i]
    totalScoreDict[allow] = 0
    linkDict[allow] = []
    for answer in answers:
        score = likeness(allow, answer)
        totalScoreDict[allow] += score
        if score > linkThreshold:
            linkDict[allow].append((answer, score))
    if linkDict[allow] == []: 
        linkDict.pop(allow)
    if i % 1000 == 0:
        print(i, allow, str(round(time.time()-start,1)) + "s")

# 2. Score based analysis
# sort totalScoreDict by scores
totalScoreDict = dict(sorted(totalScoreDict.items(), key = lambda item: item[1], reverse=True))
# print out
printTopN(totalScoreDict, 10)
#print(list(totalScoreDict).index("stale"), "stale", totalScoreDict["stale"])


# 3. Link based analysis
linkScoreDict = {}
for word, data in linkDict.items():
    linkScoreDict[word] = 0
    for (link, linkStrength) in data: # look just at 1st generation links
        linkTotalScore = totalScoreDict[link]
        linkScoreDict[word] += linkTotalScore * linkStrength # idk what this function should be
# sort linkScoreDict
linkScoreDict = dict(sorted(linkScoreDict.items(), key = lambda item: item[1], reverse=True))
printTopN(linkScoreDict, 10)


print(time.time()-start)