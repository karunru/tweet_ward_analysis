# tweet_word_analysis
tweets.csv����p�o�P��𒊏o����
# �g����
`
		python extract_tweet.py tweets.csv | sed -e '/^RT/d' | sed -e '/����RT�F/d' | sed -e 's/^@[a-zA-Z_0-9].* //' | sed -e '/^http/d' | sed -e 's/https\:\/\/t\.co\/[a-zA-Z0-9|\.|\/|:].*//' | sed -e 's/http\:\/\/t\.co\/[a-zA-Z0-9|\.|\/|:].*//' > tweet

		python count_word.py tweet (| head -100)
`
# mecab ipadic�ɂ��ă���
`
		cd /usr/local/lib/mecab/dic/ipadic/

		sudo cp unk.dic unc.dic.org

		sudo /usr/local/libexec/mecab/mecab-dict-index -U

		sudo cp unk.dic.org unk.dic
`
����Ŕ��p�L��������,�T�ϐڑ�����Ȃ��Ȃ���
