#coding: UTF-8
import MeCab


# オプション
# 1. -Ochasen
# 2. -Owakati
# 3. -Oyomi
# 4.mecabrc
text = '男だろ、負けてもいいから戦うくらいの勇気をもて'
tagger = MeCab.Tagger("-Ochasen")
str_output = tagger.parse(text)
print(str_output)
