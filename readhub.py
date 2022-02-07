import feedparser

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
    readhub = get_link_info("https://readhub.cn/topics", 10)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    msg = "Here The News"
    insert_info = "# " + msg + "\n> Update time: " + datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + "\n" + readhub + "\n"
    filename = "readhub.md"

    with open (os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as f:
        news_content = f.read()

    with open (os.path.join(os.getcwd(), filename), 'w', encoding='utf-8') as f:
        f.write(insert_info)

main()
