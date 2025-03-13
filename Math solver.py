print ("Please enter number of articles:")
article_group_1 = int(input())
print ("Please enter percentage of different articles without percent sign:")
article_group_2 = int(input())

x = article_group_1/100
article_group_3 = article_group_2*x
print ("Number of articles that are identical = ", article_group_1 - article_group_3)


