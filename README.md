# tweet_word_analysis
tweets.csvから頻出単語を抽出する
# 使い方
`
		python extract_tweet.py tweets.csv | sed -e '/^RT/d' | sed -e '/うちRT：/d' | sed -e 's/^@[a-zA-Z_0-9].* //' | sed -e '/^http/d' | sed -e 's/https\:\/\/t\.co\/[a-zA-Z0-9|\.|\/|:].*//' | sed -e 's/http\:\/\/t\.co\/[a-zA-Z0-9|\.|\/|:].*//' > tweet

		python count_word.py tweet (| head -100)
`
# mecab ipadicについてメモ
`
		cd /usr/local/lib/mecab/dic/ipadic/

		sudo cp unk.dic unc.dic.org

		sudo /usr/local/libexec/mecab/mecab-dict-index -U

		sudo cp unk.dic.org unk.dic
`
これで半角記号が名詞,サ変接続じゃなくなった
