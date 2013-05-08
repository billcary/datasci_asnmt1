import sys
import json

def hw():
    print 'Hello, world!'

def tweets(fp):
    print str(len(fp.readlines()))
    
    ## Open the file for reading
    tweetFile = open(fp, 'r')
    
    ## Read the file
    tweetFile.readlines()
    
    ## Initialize an empty list
    tweetList = []
    
    ## Iterate through file, using json.loads() to load each line into a list of
    ## dict objects from which the tweet text can later be extracted
    for line in tweetFile:
        tweetList.append(json.loads(line))
        
    ## Close the file
    tweetFile.close()
    
    ## Return the tweet list
    return tweetList
    
def sent_dict(fp):
    
    ## Read the file
    sentFile = open(fp, 'r').readlines()
    
    ## Initialize an empty dict object
    d = {}
    
    ## Iterate through each line of the file, adding a key and value to the dict
    for line in sentFile:
        d.update({line.split('\t')[0]:float(line.split('\t')[1])})
    
    ## Close the file
    ##sentFile.close()
    
    ## Return the dict object
    return d


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    ##hw()
    sentiments = sent_dict(sent_file)
    tweets = tweets(tweet_file)

if __name__ == '__main__':
    main()
