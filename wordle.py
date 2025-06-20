def likeness(word1, word2):
    green, yellow = 0, 0
    for i in range(5):
        if word1[i] == word2[i]:
            green += 1
        elif word1[i] in word2:
            yellow += 1
    print(green, yellow)
    score = (green/5) + (yellow/10)
    print(score)

likeness("stale", "scrap")
