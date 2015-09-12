import json
from AmazonReviewCrawler import AmazonReviewCrawler
from CrawlerThread import CrawlerThread

AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Certified-Refurbished-Fire-TV-Stick", "B00LO29KXQ", 1, 6181)
AmazonReviewCrawler.downloadReviewsInJsonByProductNameAndPageRange("Google-Chromecast-Streaming-Media-Player", "B00DR0PDNE", 1, 3664)