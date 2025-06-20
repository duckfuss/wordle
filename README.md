# wordle

## project structure

rankWordle.py generates linkFile and scoreFiles which both contain words ordered by to what extent they eliminate other words. The difference is simply they're two different methods of doing it.

playWordle.py plays wordle using these files

## explanation of link based analysis (linkFile)

Undirected graph of words where each word links to other words with a weight.

This weight is = to the similarity (likeness) between the two words. a.k.a how much guessing one word eliminates the other.

Network stored in linkDict = = {word: [(linked word, connection weight)]}.

Words are given a score based off the sums of the totalScores of their linked words multiplied by the strength of the link to that word and the recursion depth (counts down) which is done recursively in exploreGraph.
