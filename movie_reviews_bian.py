#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:56:39 2020

@author: joybian
"""

from bs4 import BeautifulSoup
import re
import time
import requests

# parameters of our file
movie   = ('joker_2019','terminator_dark_fate','maleficent_mistress_of_evil','harriet','the_addams_family_2019',
          'zombieland_double_tap','countdown_2019','black_and_blue_2019','motherless_brooklyn','arctic_dogs','parasite_2019',
          'jojo_rabbit','the_lighthouse_2019','gemini_man_2019','the_current_war_directors_cut','downton_abbey','abominable','judy_2019',
          'housefull_4','hustlers_2019','pain_and_glory','it_chapter_two','jay_and_silent_bob_reboot','ad_astra',
          'western_stars','the_lion_king_2019','linda_ronstadt_the_sound_of_my_voice','the_peanut_butter_falcon',
           'once_upon_a_time_in_hollywood','rambo_last_blood','no_safe_spaces','toy_story_4')
name    = 'jingwen_bian' # replace here with your name!
pageNum = 5

# create the movie url
for i in range (0,31):
    url = 'https://www.rottentomatoes.com/m/'+movie[i]+'/reviews/'

# output file
    with open(name + '_' + movie[i]+'.txt','w') as fw:
    
    # for each page out of the pageNum pages you want to parse
        for p in range(1,pageNum+1): 
        
        # tell user which page you're parsing
            print ('Getting page',p)
        
        # initialize html file to None
            html=None        
        
        # set URL to get appropriately
        #   if it is the first page
            if p==1: 
            # url for page 1
                pageLink=url 
        #   if it is not the first page
            else: 
            # url for other pages
                pageLink=url+'?page='+str(p)+'&sort=' # make the page url
            
        # try to scrape times
            for i in range(5): 
                try:
                # get url content
                    response = requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                # get the html
                    html=response.content
                # if we successuflly got the file, break the loop
                    break 
            # requests.get() threw an exception, i.e., the attempt to get the response failed
                except:
                    print ('failed attempt #',i)
                # wait 2 secs before trying again
                    time.sleep(2)

            if not html:
            # couldnt get the page, ignore
                print('could not get page #', p)
                continue 
        
        # if we got the page, parse the html file
        # first, turn it into a beautiful soup object
            soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml')
        
        # then get all the review divs
            reviews=soup.findAll('div', {'class':re.compile('review_table_row')})
        
        # grab the information for each review
            print ('Parsing page',p)
        
        
            for review in reviews:
            
            # initialize critic, rating, source, text, date
                rating,text='NA','NA'

            # 1. if there is rating information, get it
                ratingChunk=review.find('div',{'class':re.compile('review_icon')})
                if ratingChunk:
                    rating=ratingChunk.attrs['class'][3]
            
            # 2. if there is text information, get it
                textChunk=review.find('div',{'class':re.compile('the_review')})
                if textChunk:
                    text=textChunk.text.strip()
            
            #write everything to file    		
                fw.write(rating+'\t'+text+'\n')

print ('Done!')