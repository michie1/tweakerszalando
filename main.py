import urllib2
import xml.etree.ElementTree
#import pynotify
import subprocess

import sched, time

pref_link = ''

def do(sc):
    global pref_link
    url = 'https://gathering.tweakers.net/rss/list_messages/1764859'
    data = urllib2.urlopen(url)
    first = xml.etree.ElementTree.parse(data).getroot()[0][10]
    description = first[3].text
    link = first[1].text

    #if 'helaas' in first_description or 
    if link != pref_link:
        # if 'zalando' in description or 'Zalando' in description: # Niet nodig meer, want apart Zalando topic
            #pynotify.init('Zalando')
            #notice = pynotify.Notification('Tweakers.net', 'Zalando kortingsbon')
            #notice.show()
        print(link, pref_link)
        subprocess.Popen(['notify-send', 'Tweakers.net', 'Zalando kortingsbon'])
        pref_link = link

    sc.enter(60, 1, do, (sc,))

def main():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, do, (s,))
    s.run()

if __name__ == '__main__':
    main()
