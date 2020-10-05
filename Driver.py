from fanfiction import Scraper
import time, re, requests
from bs4 import BeautifulSoup

def getStories(URL, FicsToParse):
    f = open(FicsToParse,"a+")
    url = URL
    result = requests.get(url)
    html = result.content
    soup = BeautifulSoup(html, "html.parser")
    strSoup = str(soup) + " "
    indicies = [m.end() for m in re.finditer("href=\"/s/", strSoup)]
    indicies = indicies[::2]
    Stories = [strSoup[m:m+8].replace("/","") for m in indicies]
    for story in Stories:
        f.write(story)
        f.write("\n")
    f.close()
    
def scrape_reviews(story_id, num_chapters):
    total_chapter_reviews = []
    currentNum = 0
    for chapter_id in range(1,num_chapters+1):
        chapter_reviews = scraper.scrape_reviews_for_chapter(story_id,chapter_id)
        total_chapter_reviews.append(chapter_reviews)
        if(len(total_chapter_reviews)>=currentNum):
            print(len(total_chapter_reviews))
            currentNum+=20
    return total_chapter_reviews

def getReviewsOfChapter(story_id, Fics, Reviews):
    f= open(Fics,"a+")
    f1= open(Reviews,"a+")
    storyID = story_id
    metadata = scraper.scrape_story_metadata(storyID)
    print(metadata)
    print("Title: "+metadata['title']+ "; ID: "+str(metadata['id'])+"; num_reviews:"+str(metadata['num_reviews']))
    reviews = scrape_reviews(storyID,metadata['num_chapters'])
    theReviews = set([])
    for list in reviews:
        for item in list:
            if item is not None:
                theReviews.add(item)
    f.write("Title: "+metadata['title']+ "; ID: "+str(metadata['id'])+"; num_reviews:"+str(metadata['num_reviews']))
    f.write("\n")
    f1.write(str(theReviews))
    f1.write("\n")

    f.close()
    f1.close()
    print("Finished")

scraper = Scraper()
with open("FicsToParse.txt") as f:
    for line in f:
        print(int(line))
        try:
            getReviewsOfChapter(int(line), "Fics", "Reviews")
        except:
            print("Line: "+line+" Failed")
