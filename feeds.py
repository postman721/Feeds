#Feeds Copyright (c) 2019 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")

#!/usr/bin/env python3


########################################################
#Install python-feedparser python3-feedparser (Debian 10).
##########################################################
import feedparser

#Feed url -> Customize if wanted.
url= "https://www.techtimejourney.net/feed/"

#Print to terminal
print ("Showing 5 most recent posts on Techtimejourney" + '\n' ) 

#Parse feed
feed = feedparser.parse(url)

#Get titles. Notice that counting always starts from 0.
title0=feed.entries[0]
title1=feed.entries[1]
title2=feed.entries[2]
title3=feed.entries[3]
title4=feed.entries[4]

#Print out dates & titles & links
print (title0.published + ":" + title0.title + '\n' + title0.link + '\n' )
print (title1.published + ":" + title1.title + '\n' + title1.link + '\n')
print (title2.published + ":" + title2.title + '\n' + title2.link + '\n')
print (title3.published + ":" + title3.title + '\n' + title3.link + '\n')
print (title4.published + ":" + title4.title + '\n' + title4.link + '\n')

#Feedparser documentation is at: https://pythonhosted.org/feedparser/	

#TODO: GUI.
