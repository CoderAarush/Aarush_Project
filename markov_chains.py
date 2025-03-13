import numpy as np

#Get the data
trump = open("tweets.csv", "r").read()
corpus = trump.split()

#Make the keys for the dictionary
def make_pairs(corpus):
    for i in range(1, len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])

pairs = make_pairs(corpus)

#Appending the word dictionary
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

#Building the Markov model
first_word = np.random.choice(corpus)
first_word = str(first_word)

while first_word.islower():
    first_word = str(np.random.choice(corpus))

chain = [first_word]
n_words = 20
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

#Print the Predictions

chain = str(chain).replace(",", "")
chain = str(chain).replace("'", "")
chain = chain.replace("[", "")
chain = str(chain).replace("]", "")
print("".join(chain))