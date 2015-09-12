from threading import Thread
from AmazonReviewCrawler import AmazonReviewCrawler

class CrawlerThread (Thread):
    def __init__(self, threadID, urls):
        Thread.__init__(self)
        self.threadID = threadID
        self.urls = urls

    def run(self):
        reviews = AmazonReviewCrawler.getAllReviewsInJsonByURLs(self.urls)