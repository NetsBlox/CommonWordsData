cat FrequencyWords/content/2018/en/en_full.txt | sed 's/\(.*\) [0-9]\+/\1/' | hunspell -G -d en_US,en_GB | python filter_profanity.py --lang en | head -n 5000 > words/en.txt
