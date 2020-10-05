# StoryRecommender
A fanfiction story recommender that used unsupervised clustering and minimum spanning trees to find similar stories.

# Why I made this
I've read many fanfiction stores in the past, and I wanted a better way of finding similar stories to ones I liked than just googling and seeing what would come up. Using both unsuperivsed learning and a minimum spanning tree, I've worked to try and find good recommendations.

# What each file does
AverageVisualization, completeVisualization, and singlVisualization represent the three linkages I used for the agglomerative clustering on my distance matrix.

outfile100 represents the distance matrix I used, but it is only 100 of the stories. Having scraped a few thousand stories, I didn't want to upload such a large file.

unsupervisedSCIPY.py is the code I used to input various items and create the final images. 

tree.py is the code to create the minimum spanning tree.

driver.py is the code to scrape stories off fanfiction.net

# A few notes
All the unsupervised items here only show off the top 100 stories that I scraped. It should be noted that I scraped a few thousand stories, but for the sake of example, I only showed the top 100. 

Furthermore, given that these stories are based off of scraped user like and comment patterns, it should be noted that this changes over time. Given that this data was scraped in 2016, the data is likely very outdated.

Finally, the numbers at the bottom of the graph represent their indexes in an array. In this instance, it was more valuable to visualize with smaller number, rather than the larger values that represent unique fanfiction stories.
