import re
from collections import defaultdict

def wordcount(text):
    # 去掉标点符号并将所有单词转换为小写
    text = re.sub(r"[^\w\s']", '', text).lower()
    words = text.split()
    
    # 使用defaultdict统计每个单词出现的次数
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
        
    return dict(word_count)

# 测试
text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

print(wordcount(text))
