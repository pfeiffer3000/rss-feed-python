import feedparser
from time import sleep

def grab_print_feed():

    d = feedparser.parse("http://feeds.reuters.com/reuters/topNews")

    for i in range(len(d.entries)):
        print(i+1, d.entries[i].title)
        sleep(3)

while True:
    grab_print_feed()
