# tweet_word_analysis
tweets.csv����p�o�P��𒊏o����
# �g����
python extract_tweet.py tweets.csv | sed -e '/^RT/d' | sed -e '/����RT�F/d' | sed -e 's/^@[a-zA-Z_0-9].* //' | sed -e '/^http/d' > tweets

