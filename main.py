import feedparser
import time
import os
import re
import pytz
from datetime import datetime

def get_link_info(feed_url, num):
    result = ""
    feed = feedparser.parse(feed_url)
    feed_entries = feed["entries"]
    feed_entries_length = len(feed_entries)
    all_number = 0;

    if(num > feed_entries_length):
        all_number = feed_entries_length
    else:
        all_number = num

    for entrie in feed_entries[0: all_number]:
        title = entrie["title"]
        link = entrie["link"]
        result = result + "\n" + "[" + title + "](" + link + ")" + "\n"

    return result

def main():
    chenhao = get_link_info("", 1)
    #chenhao = get_link_info("https://coolshell.cn/feed", 1)
    #pthink = get_link_info("https://feeds2.feedburner.com/programthink", 1)
    insert_info = chenhao

    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    tag_beg = "---start---"
    tag_end = "---end---"
    timenow = "Update time: " + datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    msg = " Auto update by GitHub Actions."

    insert_info = tag_beg + "\n\n## " + timenow + msg + "\n" + insert_info + "\n" + tag_end

    with open (os.path.join(os.getcwd(), "news.md"), 'r', encoding='utf-8') as f:
        news_md_content = f.read()

    new_news_md_content = re.sub("", insert_info, news_md_content)

    with open (os.path.join(os.getcwd(), "news.md"), 'w', encoding='utf-8') as f:
        f.write(new_news_md_content)

main()
