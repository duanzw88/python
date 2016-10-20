#-*- coding:utf-8 -*-
#
import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "*** ***(@@@)":
        "From *** get the *** function,and call it with parameters self,@@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."

}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True;
else:
    PHRASES_FIRST = False;

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
# print "words = ",WORDS
def convert(snippet,phrase):
    # class_names = [w.capitalize() for w in random.sample(WORDS,
    #                                                 snippet.count("%%%"))]
    class_names = []
    #------
    count = snippet.count("%%%")
    sample = random.sample(WORDS,count)
    print "count = ",count," sample = ",sample
    for w in sample:
        print "W = ",w
        class_names.append(w.capitalize())

    print "class_names = ",class_names
    other_names = random.sample(WORDS,snippet.count("***"))
    print "other_names = ",other_names
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(','.join(random.sample(WORDS,param_count)))
        print '-' * 10

    for sentence in snippet,phrase:
        print "sentence = ",sentence
        result = sentence[:]
        print "result = ",result

        for word in class_names:
            result = result.replace("%%%",word,1)

        for word in other_names:
            result = result.replace("***",word,1)
        for word in param_names:
            result = result.replace("@@@",word,1)

        results.append(result)

        print "results = ",results
        return results

try:
    while True:
        snippets = PHRASES.keys()
        # print snippets
        # print '-' * 10
        random.shuffle(snippets)
        # print snippets
        for snippet in snippets:
            phrase = PHRASES[snippet]
            print "phrase = ",phrase
            print "snippet = ",snippet
            question,answer = convert(snippet,phrase)
            if PHRASES_FIRST:
                question,answer = answer,question
            print question

            raw_input(">")
            print "answer:%s\n\n" % answer
except EOFError:
    print "\nBye"
