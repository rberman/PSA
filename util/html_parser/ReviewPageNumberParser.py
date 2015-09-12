import locale
from HTMLParser import HTMLParser

class ReviewPageNumberParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		locale.setlocale(locale.LC_ALL, 'en_US')
		self.is_ul_class_pagination_started = False
		self.last_review_page_number = 0

	def handle_starttag(self, tag, attrs):
		if tag == "ul" and ("class", "a-pagination") in attrs:
			self.is_ul_class_pagination_started = True

	def handle_data(self, data):
		if(self.is_ul_class_pagination_started):
			try:
				self.last_review_page_number = locale.atoi(data)
			except ValueError:
				pass

	def handle_endtag(self, tag):
		if(tag == "ul" and self.is_ul_class_pagination_started):
			self.is_ul_class_pagination_started = False

	def getLastReveiwPageNumber(self):
		return self.last_review_page_number