# DataCrawl
# Author: joy_bian
# Created on Tue Feb 11 2020 00:29:26

1. Create a list of movies
2. Create the movie url
3. Create an output file: for each page url out of the page number pages you want to parse, tell user which page you are parsing
4. Initialize html file to None
5. Set url to get proper link
6. Use function range to define scrape times
7. Get url content and html
8. If we got the page, parse the html file
9. Use BeautifulSoup function to turn the object into beautiful soup object
10. Grab the information for each review
11. Initialize critic, rating, source, text, date
12. If there is rating,text, critic, source, date information, get them
13. Use fw.write function to write everything into the file
