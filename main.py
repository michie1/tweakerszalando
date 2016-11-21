import urllib2
import xml.etree.ElementTree
import pynotify

import sched, time

def do(sc):

    pref_link = ''

    url = 'https://gathering.tweakers.net/rss/list_messages/1543297'
    data = urllib2.urlopen(url)
    first = xml.etree.ElementTree.parse(data).getroot()[0][10]
    description = first[3].text
    link = first[1].text

    #if 'helaas' in first_description or 
    if link != pref_link:
        if 'zalando' in description or 'Zalando' in description:
            pynotify.init('Zalando')
            notice = pynotify.Notification('Tweakers.net', 'Zalando kortingsbon')
            notice.show()
            pref_link = link

    sc.enter(60, 1, do, (sc,))

def main():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, do, (s,))
    s.run()

if __name__ == '__main__':
    main()
