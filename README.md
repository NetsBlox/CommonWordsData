# CommonWords Data (and scripts!)
This repository contains the word lists used by the CommonWords service in NetsBlox.

## Usage
First, install the python dependencies:

```
python -m pip install -r requirements.txt
```

Then generate the datasets:
```
python create_wordlists.py
```

Finally, move the word lists in `words/` to `src/server/services/procedures/common-words/words/` in the NetsBlox repository!
