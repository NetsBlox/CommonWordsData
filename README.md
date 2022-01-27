# CommonWords Data (and scripts!)
This repository contains the word lists used by the CommonWords service in NetsBlox.

Special thanks to the authors of:
- https://github.com/hermitdave/FrequencyWords (for the ranked word lists)
- https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/ (for lists of profane words to filter out)

## Usage
First, install the python dependencies, hunspell (and the en_US, en_GB, es, hu_HU dictionaries):

```
python -m pip install -r requirements.txt
```

Then generate the datasets:
```
bash create_wordlists.sh
```

Finally, move the word lists in `words/` to `src/server/services/procedures/common-words/words/` in the NetsBlox repository!
