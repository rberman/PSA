# PSA


# Reviews Data
It is stored in `reviews_data.json` and it has the following format.
```json
[
  {
    "rating": 4.0,
    "review": "The product is awesome.",
    "verified": true,
    "helpfulness": "0/0",
    "author": "Soe Lynn"
  },
  ...
]
```

Total Documents : `1061`
Total Tokens    : `589643`

Here is the sample code on how to use the data
```python
import json

reviews = json.load(open("reviews_data.json"))
for review in reviews:
  print(review["review"])
```
