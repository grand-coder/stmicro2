import jieba
jieba.set_dictionary("dict.txt.big")
jieba.load_userdict("entertain.txt")
import jieba.analyse

# r: 讀取 w:寫入 a:寫入(結尾)
f = open("news/a.txt", "r", encoding="utf-8")
article = f.read()
f.close()

print("分詞:", list(jieba.cut(article)))
keywords = jieba.analyse.extract_tags(article)
print("關鍵詞:", keywords)