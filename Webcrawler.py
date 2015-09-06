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

    verifiedStrip = authorSplit.split("Verified Purchase")
    if len(verifiedStrip) == 2:
        verified = "true"
    else:
        verified = "false"

    reviewTemp = authorSplit.split('<span class="a-size-base review-text">')
    reviewFrontStripped = reviewTemp[1]
    reviewStrip = reviewFrontStripped.split('</span></div>')
    review = reviewStrip[0]

    file.write('{"author":"'+author+'","rating":'+rating+',"verified":'+verified+',"review":"'+review+'","helpfulness":"'+helpful+'"},')
    return
##----------------------------------------------------DEFINING LINE---------------------------------------------------------------##
pageNo = 0
url = raw_input('Enter URL : ')
url = url.split("ref=cm")
urlPartOne = "ref=cm_cr_pr_btm_link_"
urlPartTwo = "?ie=UTF8&showViewpoints=1&sortBy=recent&reviewerType=all_reviews&filterByStar=all_stars&pageNumber="
fileNameToSave = "theReviews.txt"
try:
    file = open(fileNameToSave,"w")
    file.write('{"reviews" : [')
    file.close()
except:
    print "Error creating file"

##note this pageNo != 5 is to make data set smaller for testing
while(pageNo != 5):
    pageNo = pageNo + 1
    try:
        reviewURL = url[0] + urlPartOne + str(pageNo) + urlPartTwo + str(pageNo)
        response = urllib2.urlopen(reviewURL)
        source = response.read()
        sourceBreak = source.split('<div id="cm_cr-review_list"')
        reviewPart = sourceBreak[1]
        big8Reviews = reviewPart.split('class="a-section review">')
        small8Reviews = []
        for i in range(0,8):
            try:
                oneReviewChunk = big8Reviews[i+1]
                splitEndingChunk = oneReviewChunk.split('</span></div><div class="a-row a-spacing-top-small review-comments">')
                small8Reviews.append(splitEndingChunk[0])
            except:
                print "Error going next review"
        file = open(fileNameToSave,"a")        
        for review in small8Reviews:
            extractInfoAndWrite(review)
        file.close()
    except:
        print "Error going next page"

with open(fileNameToSave, 'r+') as f:
    f.seek(-1,2) # end of file
    size=f.tell() # the size...
    f.write("")
    f.write(']}')
    

    
