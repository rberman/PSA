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

CreateVectors:
    - Creates file "text_phrases.txt" which replaces common multi-word phrases that should be together with a one word version.
    For example San Francisco -> San_Francisco

    - Creates file "vectors.bin" with vectors trained on data in the "review_text.txt" file.

    - Creates file "clusters.txt" which clusters vectors from "vectors.bin" and "review_text.txt" to find similar words.

Predictions:
    - Creates models of "vectors.bin" and "GoogleNews_vectors.bin" (GoogleNews_vectors not included on GitHub)
    - For each model takes 5 words and finds 10 similar words using each dataset
    - Finds three linguistic regularity examples (examples not yet implemented)
