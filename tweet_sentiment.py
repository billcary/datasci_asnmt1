import sys
import json

def hw():
    print 'Hello, world!'

def tweets(fp):
    print str(len(fp.readlines()))
    
    ## Open the file for reading
    tweetFile = open(fp, 'r')
    
    ## Initialize an empty list to hold the full tweet (list of dicts)
    tweetData = []
    
    ## Initialize an empty list to hold the text of each tweet
    tweetText = []
    
    ## Iterate through file, using json.loads() to load each line into a list of
    ## dict objects from which the tweet text can later be extracted
    for line in tweetFile:
        tweetData.append(json.loads(line))
    
    ## Iterate through the full tweets and extract only the text    
    for item in tweetData:
        tweetText.append(item[u'text'])
        
    ## Close the file
    tweetFile.close()
    
    ## Return the tweet text list
    return tweetText
    
def sent_dict(fp):
    
    ## Read the file
    sentFile = open(fp, 'r').readlines()
    
    ## Initialize an empty dict object
    d = {}
    
    ## Iterate through each line of the file, adding a key and value to the dict
    for line in sentFile:
        d.update({line.split('\t')[0]:float(line.split('\t')[1])})
    
    ## Close the file
    sentFile.close()
    
    ## Return the dict object
    return d


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ##hw()
    
    ## Retrieve the dictionary of sentiments
    sentiments = sent_dict(sent_file)
    
    ## Retrieve the list of tweet texts
    tweets = tweets(tweet_file)
    
    ## Iterate through the list of tweets, splitting each tweet into
    ## individual words and comparing the word to the sentiment dictionary
    ## to determine a sentiment score for the word.  Accumulate the score.
    ## Print the accumulated score to the screen, then move to the next tweet.
    for text in tweets:
        score = 0.0
        for word in text.split():
            score += sentiments[word]
            
        print score
    
if __name__ == '__main__':
    main()
