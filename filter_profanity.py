"""A simple script to filter out profanity given a language"""
import errno
import sys
more_bad_words = {
    'en': ['dammit']
}

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--lang')
args = parser.parse_args()

language = args.lang
with open(f'./List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/{language}', 'r') as f:
    bad_words = [ word.strip() for word in f ] + more_bad_words.get(language, [])

def is_bad_word(word):
    for bad_word in bad_words:
        if bad_word in word:
            return True
    return False

try:
    for line in sys.stdin:
        word = line.strip()
        if len(word) < 3:
            continue
        if is_bad_word(word):
            continue
        print(word)
except IOError as e:
    if e.errno != errno.EPIPE:
        raise e
