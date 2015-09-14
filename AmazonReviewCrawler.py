import urllib2
import json
from xml.dom import minidom
from util.html_parser import ReviewPageNumberParser
from util.html_parser import ReviewParser

class AmazonReviewCrawler:

	@staticmethod
	def retrieveLastReviewsPageNumber(product_name, product_code):
		firstReviewPageURL = "http://www.amazon.com/%s/product-reviews/%s/ref=cm_cr_pr_btm_link_4?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber=1" % (product_name, product_code)
		firstReviewPage = urllib2.urlopen(firstReviewPageURL)
		firstReviewPage_raw_content = firstReviewPage.read()
		
		pageNumberParser = ReviewPageNumberParser()
		pageNumberParser.feed(firstReviewPage_raw_content)

		return pageNumberParser.last_review_page_number

	@staticmethod
	def downloadReviewsInJsonByProductNameAndPageRange(product_name, product_code, start_page_number, end_page_number):
		for page_number in range(start_page_number, end_page_number+1):
			print("Downloading for " + product_name + " Review Page " + str(page_number))
			reviews_page_url = "http://www.amazon.com/%s/product-reviews/%s/ref=cm_cr_pr_btm_link_4?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber=%d" % (product_name, product_code, page_number)
			
			retry = True
			while(retry):
				try:
					reviews_page = urllib2.urlopen(reviews_page_url)
					reviews_page_raw_content = reviews_page.read()
					review = ReviewParser.parse(reviews_page_raw_content)

					f = open('raw_data/%s-%d.json' % (product_code, page_number),'w')
					f.write(json.dumps(review))
					f.close()

					retry = False
				except Exception as e:
					print("Retrying")
					print(e)