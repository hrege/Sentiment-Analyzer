import nltk

def get_words_in_reviews(reviews):
      totalwords = []
      for (words, sentiment) in reviews:
            totalwords.extend(words)
      return totalwords

def get_word_features(wordList):
      wordList = nltk.FreqDist(wordList)
      word_features = wordList.keys()
      return word_features

#Need to extract all relevant features from input document(review) - returns dictionary of words features present in test set
def extract_features(document):
      document_words = set(document)
      features = {}
      for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
      return features
  

#Develop input lists of pos/neg reviews
#Read one positive review and one negative review, store in tuple list as (string review, string sentiment)

neg = open('cv000_29416.txt', 'r')
neg = neg.read()
neg1 = open('cv001_19502.txt', 'r')
neg1 = neg1.read()
neg2 = open('cv002_17424.txt', 'r')
neg2 = neg2.read()
neg3 = open('cv003_12683.txt', 'r')
neg3 = neg3.read()
neg4 = open('cv004_12641.txt', 'r')
neg4 = neg4.read()

neg_review = [(str(neg), "negative"), (str(neg1), "negative"), (str(neg2), "negative"), (str(neg3), "negative"), (str(neg4), "negative")]

pos = open('cv000_29590.txt', 'r')
pos = pos.read()
pos1 = open('cv001_18431.txt', 'r')
pos1 = pos1.read()
pos2 = open('cv002_15918.txt', 'r')
pos2 = pos2.read()
pos3 = open('cv003_11664.txt', 'r')
pos3 = pos3.read()
pos4 = open('cv004_11636.txt', 'r')
pos4 = pos4.read()

pos_review = [(str(pos), 'positive'), (str(pos1), 'positive'), (str(pos2), 'positive'), (str(pos3), 'positive'), (str(pos4), 'positive')]

reviews = []

#filter both and join into one 'reviews list'
for(words, sentiment) in pos_review + neg_review:
      filteredWords = [e.lower() for e in words.split() if len(e) >= 3]
      reviews.append((filteredWords, sentiment))

test = [] #insert test reviews

#Need to extract each distinct feature by determining freq dist of each word feature
word_features = get_word_features(get_words_in_reviews(reviews))

training_set = nltk.classify.apply_features(extract_features, reviews)

#Uses internal Python libraries to apply frequency distribution of labels along
#with the feature probability of each word with corresponding sentiment label
#Creates classifier based on training set
classifier = nltk.NaiveBayesClassifier.train(training_set)

#Now we need to test the classifier on test set

#test_input = [] #implement file i/o to create test set similar to format of training

#for i in test_input:
f = open('cv004_12641.txt', 'r')
f = f.read()
#print(f.split())
print(classifier.classify(extract_features(f.split())))
      





