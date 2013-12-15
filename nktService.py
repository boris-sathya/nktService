#!/usr/bin/python

import socket
import feedparser

#FB Notificiation RSS Parse
def fbParse():
    cover = 0
    profile = 0

    fbFeed = feedparser.parse('_YOUR_FB_RSS_FEED_URL')

    for post in fbFeed.entries:
        if post.title == "__NAME__ changed his cover photo.":
            cover = cover + 1
        elif post.title == "__NAME__ changed his profile picture.":
            profile = profile + 1

    no = len(fbFeed['entries'])
    res = "Since " +fbFeed['entries'][no-1].published + "\n"
    res = res + "__NAME__ Changed "+str(cover)+" Cover picture(s) and "+str(profile)+" Profile picture(s)\n"
    return res

#main
#server: Bind and Listen
#call fbParse on accept
host = ''
port = 1337
backlog = 10
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)

while 1:
    client, address = s.accept()
    data = fbParse() #Parse FB Notification
    client.send(data)
    client.close()
