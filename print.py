import urllib
import json

for page in range(1,11):

    urlstr = 'http://search.twitter.com/search.json?q=microsoft&page=' + str(page)
    response = urllib.urlopen(urlstr)
    tweetstream = json.load(response)
    print tweetstream.get(u'text')
    print '\n'

