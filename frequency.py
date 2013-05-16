import sys
import json
import re
#import pdb

def hw():
    print 'Hello, world!'

def tweets(fp):
    #pdb.set_trace()
    
    ## Open the file for reading
    tweetFile = open(fp, 'r')
    
    ## Initialize an empty list to hold the full tweet (list of dicts)
    tweetData = []
    
    ## Initialize an empty list to hold the text of each tweet
    tweetText = []
    
    ## Iterate through file, using json.loads() to load each line into a list of
    ## dict objects from which the tweet text can later be extracted
    for line in tweetFile.readlines():
        tweetData.append(json.loads(line))
    
    ## Iterate through the full tweets and extract only the text    
    for item in tweetData:
        tweetText.append(item.get('text', ''))
        ##tweetText.append(item[u'text'])
        
    ## Close the file
    tweetFile.close()
    
    ## Return the tweet text list
    return tweetText


def main():
    #pdb.set_trace()
    tweet_file = sys.argv[0]
    ##hw()
    
    #pdb.set_trace()
    
    ## Retrieve the list of tweet texts
    tweetList = tweets(tweet_file)
    
    ## Iterate through the list of tweets, concatenating each tweet, along with
    ## a space, into a single string.
    fullText = ''
    for text in tweetList:
        text = '' + text
        fullText += text
        
    words = re.split('\s+', fullText.lower()) ## Split the text into words and normalize to lowercase
    
    wordCount = len(words) ## Count the total number of words in the text

    # create dictionary of word:frequency pairs
    wordFrequencies = {}
    # punctuation marks to be removed
    punctuation = re.compile(r'[.?!,":;]') 
    for word in words:
        # remove punctuation marks
        word = punctuation.sub("", word)
        # form dictionary
        try: 
            wordFrequencies[word] += 1
        except: 
            wordFrequencies[word] = 1
    
    # create list of (key, val) tuple pairs
    freq_list = wordFrequencies.items()
    # sort by key or word
    freq_list.sort()
    # display result
    for word, freq in freq_list:
        print word, float(freq)/float(wordCount)
    
if __name__ == '__main__':
    main()