# tweet_word_analysis
tweets.csvから頻出単語を抽出する
# 使い方
python extract_tweet.py tweets.csv | sed -e '/^RT/d' | sed -e '/うちRT：/d' | sed -e 's/^@[a-zA-Z_0-9].* //' | sed -e '/^http/d' > tweets

