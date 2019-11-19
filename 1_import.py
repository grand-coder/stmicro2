import jieba
jieba.set_dictionary("dict.txt.big")
jieba.load_userdict("entertain.txt")
from jieba.analyse import extract_tags
import glob

for fn in glob.glob("news/*.txt"):
    # r: 讀取 w:寫入 a:寫入(結尾)
    f = open(fn, "r", encoding="utf-8")
    article = f.read()
    f.close()

    print("分詞:", list(jieba.cut(article)))
    keywords = extract_tags(article)
    print("關鍵詞:", keywords)