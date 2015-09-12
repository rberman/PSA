import re
import json
import urllib2

def extractInfoAndWrite(reviewChunk):



    helpfulStrip = reviewChunk.split('people found the following review helpful')
    if len(helpfulStrip) == 2:
        helpfulFront = helpfulStrip[0]
        helpfulFrontStrip = helpfulFront.split('class="a-size-small a-color-secondary review-votes">')
        helpfulText = helpfulFrontStrip[1]
        helpfulSplit = helpfulText.split(" ")
        helpful = helpfulSplit[0] + "/" + helpfulSplit[2]
    else:
        helpful = "0/0"
    
    ratingSplit = reviewChunk.split('<i class="a-icon a-icon-star a-star-')
    rating = ratingSplit[1][0]
    
    authorTemp = ratingSplit[1]
    authorFrontSplit = authorTemp.split('<a class="a-size-base a-link-normal author"')
    authorSplit = authorFrontSplit[1]
    authorFrontStrip = authorSplit.split('">')
    authorTempSplit = authorFrontStrip[1]
    authorBackStrip = authorTempSplit.split('</a>')
    author = authorBackStrip[0]
    author = author.replace("\"","\\\"")

    verifiedStrip = authorSplit.split("Verified Purchase")
    if len(verifiedStrip) == 2:
        verified = "true"
    else:
        verified = "false"

    reviewTemp = authorSplit.split('<span class="a-size-base review-text">')
    reviewFrontStripped = reviewTemp[1]
    reviewStrip = reviewFrontStripped.split('</span></div>')
    review = reviewStrip[0]
    review = review.replace("\"","\\\"")

    extractedInfoInJson = '{"author":"'+author+'","rating":'+rating+',"verified":'+verified+',"review":"'+review+'","helpfulness":"'+helpful+'"},'
    file.write(extractedInfoInJson)

    return
##----------------------------------------------------DEFINING LINE---------------------------------------------------------------##
pageNo = 0
# url = raw_input('Enter URL : ')
url = "http://www.amazon.com/Google-Chromecast-Streaming-Media-Player/product-reviews/B00DR0PDNE/ref=cm_cr_dp_see_all_btm?ie=UTF8&showViewpoints=1&sortBy=bySubmissionDateDescending"
url = url.split("ref=cm")
urlPartOne = "ref=cm_cr_pr_btm_link_"
urlPartTwo = "?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&formatType=all_formats&filterByStar=all_stars&pageNumber="
fileNameToSave = "theReviews.txt"
try:
    file = open(fileNameToSave,"w")
    file.write('{"reviews" : [')
    file.close()
except:
    print "Error creating file"

##note this pageNo != 5 is to make data set smaller for testing
errorCount = 0
while(pageNo != 3665):
    pageNo = pageNo + 1
    try:
        reviewURL = url[0] + urlPartOne + str(pageNo) + urlPartTwo + str(pageNo)
        response = urllib2.urlopen(reviewURL)
        source = response.read()
        sourceBreak = source.split('<div id="cm_cr-review_list"')
        reviewPart = sourceBreak[1]
        big8Reviews = reviewPart.split('class="a-section review">')
        small8Reviews = []
        i=0
        while(1):
            try:
                oneReviewChunk = big8Reviews[i+1]
                splitEndingChunk = oneReviewChunk.split('</span></div><div class="a-row a-spacing-top-small review-comments">')
                small8Reviews.append(splitEndingChunk[0])
                i = i+1
            except:
                print "Error going next review"
                break
        file = open(fileNameToSave,"a")
        for review in small8Reviews:
            extractInfoAndWrite(review)
        file.close()
        errorCount = 0
    except:
        print "Error going next page"
        if errorCount < 5:
            errorCount = errorCount + 1
        else:
            break

with open(fileNameToSave, 'r+') as f:
    f.seek(-1,2) # end of file
    size=f.tell() # the size...
    f.write("")
    f.write(']}')
    

    
