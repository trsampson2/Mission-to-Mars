#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


#Set up Splinter, set the executable path and initialze a browser
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#creates an instance of a Splinter browser, preppring the automated browser.  Specifying Chrome as the browser
# **executable_path is unpacking the dictionary we've stored the path in


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)

# Tells the Splinter which site to go to by assigning the link to a URL

# Parse the HTML using BeautifulSoup
html = browser.html
html_soup = soup(html, 'html.parser')

#Beautiful soup is parsing the HTML text then then stores it as an object


# Scrape the Title
title = html_soup.find('h2').text
title

# using find fuction to search for the h2 tag and extracted only the text within the HTML tags by adding .text to the end of the code


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags_box') # creates a new variable tag_box which will be used to store the results of a search. In this case, looking for div elements with a class of tags-box n the HTML parsed earlier and stored in the html_soup variable
# tag_box
tags = tag_box.find_all('a', class_='tag') # the tags variable will hold the results of a find_all but searching through the parsed results stored in our tag_box variable to find a elements with a tag class

for tag in tags:
    word = tag.text
    print(word)

# for loop cycles through each tag in the tags variable, strips the HTML code of it and then prints only the text of each tag


url = 'http://quotes.toscrape.com/'
browser.visit(url)


for x in range(1,6):
    html = browser.html
    quote_soup = soup(html, 'html.parser')
    quotes = quote_soup.find_all('span', class_ = 'text')
    for quote in quotes:
        print('page:', x, '-----------')
        print(quote.text)
    browser.links.find_by_partial_text('Next').click()


for x in range(1,6):
    html = browser.html
    quote_soup = soup(html, 'html.parser')
    quotes = quote_soup.find_all('span', class_ = 'quote')
    for quote in quotes:
        print('page:', x, '-----------')
        print(quote.text)
    browser.links.find_by_partial_text('Next').click()

browser.quit()







