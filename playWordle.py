linkList = open("data/linkFile.txt").read().splitlines()
scoreList = open("data/scoreFile.txt").read().splitlines()
answers = open("data/answers.txt").read().splitlines()


def likeness(word1, word2):
    green, yellow = [], []
    for i in range(5):
        if word1[i] == word2[i]:
            green.append((word1[i], i))
        elif word1[i] in word2:
            yellow.append((word1[i], i))
    for letter, index in yellow: # discard duplicate yellows
        word1Tot = yellow.count(letter) + green.count(letter)
        word2Tot = word2.count(letter)
        diff = word1Tot - word2Tot
        if diff > 0:
            for i in range(diff):
                yellow.remove(letter)
    return [green, yellow]

def fancyPrint(green, yellow):
    printy = ['⬛️','⬛️','⬛️','⬛️','⬛️']
    for (char, index) in green:
        printy[index] = "🟩"
    for (char, index) in yellow:
        printy[index] = "🟨"
    print("".join(printy))

green, yellow = likeness("slate", "hello")
fancyPrint(green, yellow)
