import re
from bs4 import BeautifulSoup

class ReviewParser:

	@staticmethod
	def parse(raw_html):
		reviews = []
		soup = BeautifulSoup(raw_html, "html.parser")
		raw_reviews = soup.findAll("div", { "class" : "a-section review" })
		
		for raw_review in raw_reviews:
			review = {}

			review["author"] = raw_review.findAll("a", { "class" : "a-size-base a-link-normal author" })[0].text
			review["rating"] = float(raw_review.findAll("span", { "class" : "a-icon-alt" })[0].text.split(" ")[0])
			review["review"] = raw_review.findAll("span", { "class" : "a-size-base review-text" })[0].text

			if raw_review.find(string=re.compile("Verified Purchase")) is None:
				review["verified"] = False
			else:
				review["verified"] = True

			if len(raw_review.findAll("span", { "class" : "a-size-small a-color-secondary review-votes" })) > 0:
				helpfulness = raw_review.findAll("span", { "class" : "a-size-small a-color-secondary review-votes" })[0].text
				splited_helpfulness = re.findall('[\d]+', helpfulness)
				review["helpfulness"] = "%s/%s" % (splited_helpfulness[0], splited_helpfulness[1])
			else:
				review["helpfulness"] = "0/0"

			reviews.append(review)

		return reviews
