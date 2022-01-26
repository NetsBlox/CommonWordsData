from itertools import islice
from spellchecker import SpellChecker
languages = ['en', 'es']
WORD_COUNT = 5000

more_bad_words = {
        'en': ['dammit']
}

def is_allowed(word, bad_words):
    if len(word) < 3:
        return False
    for bad_word in bad_words:
        if bad_word in word:
            return False
    return True

for language in languages:
    checker = SpellChecker(language=language)
    checker.distance = 1
    with open(f'./List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/{language}', 'r') as f:
        bad_words = [ word.strip() for word in f ] + more_bad_words.get(language, [])
    with open(f'./FrequencyWords/content/2018/{language}/{language}_full.txt', 'r') as f:
        words = ( line.split(' ')[0] for line in f )
        valid_words = filter(lambda w: w in checker.known([w]), words)
        safe_words = ( word for word in valid_words if is_allowed(word, bad_words) )
        common_words = list(islice(safe_words, WORD_COUNT))
        with open(f'./words/{language}.txt', 'w') as of:
            of.write('\n'.join(common_words))
