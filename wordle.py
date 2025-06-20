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
    score = (len(green)/5) + (len(yellow)/10)
    return score

# 1. brute force compare every word with every other word
scoreDict = {}
linkDict = {}
linkThreshold = 0.5
for i in range(len(allowed)):
    allow = allowed[i]
    scoreDict[allow] = 0
    linkDict[allow] = []
    for answer in answers:
        score = likeness(allow, answer)
        scoreDict[allow] += score
        if score > linkThreshold:
            linkDict[allow].append((answer, score))
    if linkDict[allow] == []: 
        linkDict.pop(allow)
    if i % 1000 == 0:
        print(i, allow, str(round(time.time()-start,1)) + "s")

# 2. Score based analysis
# sort scoreDict by scores
scoreDict = dict(sorted(scoreDict.items(), key = lambda item: item[1], reverse=True))

# 3. Link based analysis
for word, data in linkDict.items():
    print(word, data)
    


# print out
printTopN(scoreDict, 10)
print(list(scoreDict).index("stale"), "stale", scoreDict["stale"])
print(list(scoreDict).index("adieu"), "adieu", scoreDict["adieu"])
print(list(scoreDict).index("audio"), "audio", scoreDict["audio"])

print(time.time()-start)