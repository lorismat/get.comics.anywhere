#! /usr/bin/env python

"""Downloading scans, image per image based on the name of a comics. Connecting to: www.comicextra.com
First, get a list of all the comic's pages and then download them with wget

Selenium is being used to fetch every page's url:
Seleninum Python client API Docs: https://selenium.dev/selenium/docs/api/py/index.html"""

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import json
import sys
import argparse

# prevent firefox window to open
os.environ['MOZ_HEADLESS'] = '1'

# fetch the library.txt file
dirname = os.path.dirname(__file__) 
library_txt = os.path.join(dirname, 'library.txt')

def main():
    parser = argparse.ArgumentParser(description='Download comics from www.comicextra.com -- Default command with no option ask for your inputs')
    
    # set the CLI arguments
    parser.add_argument('-c', '--comic', metavar='"Comic Title"',
                            help='download "Comic Title", or ask to input specific chapters if many')

    parser.add_argument('-a', '--all', action='store_true',
                            help='list all comics available')

    parser.add_argument('-l', '--list', metavar='<>',
                            help='list all comics starting by <LETTER>')

    args = parser.parse_args()

    try:
        with open(library_txt,'r') as f:
            comic_list = f.read()
            f.close()
        library = comic_list.replace("'", "\"")
        library = json.loads(library)

    # below exception recreate the library.txt file
    except:
        list_urls = []
        library = {}
        browser = webdriver.Firefox()
        browser.get('https://www.comicextra.com/comic-list?__cf_chl_jschl_tk__=2a48a8885d09237e694aa3c4856c3949930d45d1-1580650375-0-AXLNTHBRzNOsJ8lIYw80tFvXwAfMl5InUdwpouGtJAW1Mnrm_BOcHdNu7bEP8TJRcRjVB_eSo-KnYuFrNjBpzSaxGQeHqnsv8eiwE0NnGSPj4RPhc-2mv0ORDtMbHB0uEe4EFcOC__4dX4acnyVt8p269KXnG3Xu4sKykbndCSmfaCAr5Zj_LQ-iWuLj5ewBwX5SI7zmj_d3vtK_TYAidHoWCxmTeGIkY67VjDakdCJps2SyhNqahKz-8D2WqUyYq08J0XhWj01zBYpLBklMC3I')

        links = browser.find_elements_by_xpath('//a')
        for link in links:
            list_urls.append(link.get_attribute('href'))
        browser.quit()
        comic_urls = [x for x in list_urls if 'https://www.comicextra.com/comic/' in x]
        for x in comic_urls:
            library[x] = x.split('/')[4]
        with open(library_txt,'w') as f:
            f.write(str(library))

    def pretty_values(dictionnary):
        for key, value in dictionnary.items():
            dictionnary[key] = value.replace('-',' ').title()
        dictionnary = {v: k for k, v in dictionnary.items()}
        return dictionnary

    library = pretty_values(library)

    if len(sys.argv)>1 and (sys.argv[1] == '-a' or sys.argv[1] == '--all'):
        print('\n'.join(library.keys()))
        sys.exit("\n### End Of Library ###\n")

    if len(sys.argv)>1 and (sys.argv[1] == '-l' or sys.argv[1] == '--list'):
        restrict_list = [name for name in library.keys() if name[0] == sys.argv[2]]
        print('\n'.join(restrict_list))
        sys.exit("\n### End Of List ###\n")

    if len(sys.argv)>1 and (sys.argv[1] == '-c' or sys.argv[1] == '--comic'):
        print(str(sys.argv[2]))
        user_input = str(sys.argv[2])

    else:
        user_input = input("Which comic would you like to download?\n")

    url_home_page = library[user_input]

    print("Processing...")
    library[user_input]

    browser = webdriver.Firefox()
    browser.get(url_home_page)
    WebDriverWait(browser, timeout=10).until(lambda d: d.find_element_by_id("list"))
    nb_chapters = browser.find_elements_by_xpath("//tbody/tr")

    if len(nb_chapters)>1:
        print('\nDetected several chapters...')
        input_chapter = input("Please specify which one of the following you would like to download.\nFor example: #2\n\n")
        input_chapter = input_chapter.split('#')[1]
    else:
        input_chapter = "TPB"

    print("...")

    url_chapter = url_home_page.replace('comicextra.com/comic','comicextra.com')+'/chapter-'+input_chapter
    folder_to_create = '-'.join(url_chapter.split('/')[-2:])

    browser.get(url_chapter)
    WebDriverWait(browser, timeout=20).until(lambda d: d.find_element_by_class_name('label1'))

    page_number = int(browser.find_element_by_class_name('label1').text.split(' ')[1])

    list_pages = []

    os.system("mkdir %s"%folder_to_create)

    for i in range(1,page_number+1):
        if i==1:
            browser.get(url_chapter)
            WebDriverWait(browser, timeout=10).until(lambda d: d.find_element_by_id('main_img'))
            page = browser.find_element_by_id('main_img').get_attribute('src')
            list_pages.append(page)
            print("Downloading %s: page %i/%i"%(folder_to_create,i,page_number))
            os.system("wget -q '%s' -O %s/%i.jpeg &> /dev/null"%(page,folder_to_create,i))
        else:
            browser.get(url_chapter+'/%i'%i)
            WebDriverWait(browser, timeout=10).until(lambda d: d.find_element_by_id('main_img'))
            page = browser.find_element_by_id('main_img').get_attribute('src')
            list_pages.append(page)
            print("Downloading %s: page %i/%i"%(folder_to_create,i,page_number))
            os.system("wget -q '%s' -O %s/%i.jpeg &> /dev/null"%(page,folder_to_create,i))

    browser.quit()
    os.system("zip -qr %s.zip %s"%(folder_to_create,folder_to_create))
    os.system("rm -rf geckodriver.log %s/"%folder_to_create)
    print("Download complete - File created: %s.zip"%folder_to_create)

if __name__ == '__main__':
    main()
