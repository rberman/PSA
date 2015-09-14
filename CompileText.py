__author__ = 'rberman'

"""
This program takes all the JSON formatted data
and compiles one big document containing just all text from reviews.
Text is stored in file review_text.txt in the same location as this program.
"""

import json

def get_reviews(file):
    reviews = json.load(open("reviews_data.json"))
    for review in reviews:
      file.write(review["review"] + "\n")


def main():
    review_text = open("review_text.txt", "w")
    get_reviews(review_text)
    review_text.close()

main()