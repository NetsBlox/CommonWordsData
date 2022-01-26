cat FrequencyWords/content/2018/en/en_full.txt | sed 's/\(.*\) [0-9]\+/\1/' | hunspell -G -d en_US,en_GB | python filter_profanity.py --lang en | head -n 5000 > words/en.txt
cat FrequencyWords/content/2018/hu/hu_full.txt | sed 's/\(.*\) [0-9]\+/\1/' | hunspell -G -d hu_HU | python filter_profanity.py --lang hu | head -n 5000 > words/hu.txt
cat FrequencyWords/content/2018/es/es_full.txt | sed 's/\(.*\) [0-9]\+/\1/' | hunspell -G -d es | python filter_profanity.py --lang es | head -n 5000 > words/es.txt
