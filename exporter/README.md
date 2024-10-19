## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Formatting large json files

```sh
# Option 1
cat ugly.json | python -m json.tool > pretty.json

# Option 2
jq '.' uglyFile.json > formattedFile.json
```
