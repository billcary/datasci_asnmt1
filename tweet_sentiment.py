import sys
import json
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
    
def sent_dict(fp):
    
    #pdb.set_trace()
    ## Open the file
    sentFile = open(str(fp))
    
    ## Initialize an empty dict object
    sentDict = {}
    
    ## Iterate through each line of the file, adding a key and value to the dict
    for line in sentFile.readlines():
        if len(line.split('\t')) == 2:
            word, score = line.split('\t')
        else:
            word, score = line.split('\t')[0], 0
            
        sentDict.update({word:float(score)})
    
    ## Close the file
    sentFile.close()
    
    ## Return the dict object
    return sentDict


def main():
    #pdb.set_trace()
    sent_file = sys.argv[0]
    tweet_file = sys.argv[1]
    ##hw()
    
    ## Retrieve the dictionary of sentiments
    sentiments = sent_dict(sent_file)
    
    #pdb.set_trace()
    
    ## Retrieve the list of tweet texts
    tweetList = tweets(tweet_file)
    
    ## Iterate through the list of tweets, splitting each tweet into
    ## individual words and comparing the word to the sentiment dictionary
    ## to determine a sentiment score for the word.  Accumulate the score.
    ## Print the accumulated score to the screen, then move to the next tweet.
    for text in tweetList:
        score = 0.0
        for word in text.split():
            score += sentiments.get(word, 0.0)
            
        print score
    
if __name__ == '__main__':
    main()
