import time
start = time.time()

# open files
answers = open("answers.txt").read().splitlines()
allowed = open("allowed.txt").read().splitlines()

# Functions:
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

def exploreGraph(word, totalScoreDict, linkDict, output=0, recDepth=1):
    if recDepth == 0:
        return 0
    for (link, linkStrength) in linkDict[word]:
        if linkStrength > (1-(2**-recDepth)): # prune
            output += totalScoreDict[link] * linkStrength * recDepth
            output += exploreGraph(link, totalScoreDict, linkDict, output, recDepth-1)
    return output

# 1. brute force compare every word with every other word
totalScoreDict = {} # key: word, value: sum of it's likenesses with all other words
linkDict = {}       # key: word, value: [(linked word, similarity with said word), (...)]
                    # a "link" is two words with a similarity score above this threshold
for i in range(len(allowed)):
    allow = allowed[i]
    totalScoreDict[allow], linkDict[allow] = 0, []
    for answer in answers:
        similarity = likeness(allow, answer)
        totalScoreDict[allow] += similarity
        linkDict[allow].append((answer, similarity))
    if linkDict[allow] == []: 
        linkDict.pop(allow)
    if i % 1000 == 0:
        print(i, allow, str(round(time.time()-start,1)) + "s")

# 2. Score based analysis
# sort totalScoreDict by scores
totalScoreDict = dict(sorted(totalScoreDict.items(), key = lambda item: item[1], reverse=True))
printTopN(totalScoreDict, 10)
print("done in ", str(round(time.time()-start,2)) + "s")

# 3. link based analysis
#   Undirected graph of words where each word links to other words with a weight.
#   This weight is = to the similarity (likeness) between the two words.
#   ...a.k.a how much guessing one word eliminates the other.
#   Network stored in linkDict = {word: [(linked word, connection weight)]}.
#   Words are given a score based off the sums of the totalScores of their linked words
#   ...multiplied by the strength of the link to that word and the recursion depth (counts down)
#   ...which is done recursively in exploreGraph.
linkScoreDict = {}
for word, data in linkDict.items():
    linkScoreDict[word] = exploreGraph(word, totalScoreDict, linkDict, recDepth=3)
linkScoreDict = dict(sorted(linkScoreDict.items(), key = lambda item: item[1], reverse=True))
printTopN(linkScoreDict, 10)

print("completed in ", str(round(time.time()-start,2)) + "s")