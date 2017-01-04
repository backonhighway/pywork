# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import sqlite3
from time import sleep
import page_getter
import page_parser

first_url_list = [
    "http://db.netkeiba.com/race/sum/01/20140726/",
    "http://db.netkeiba.com/race/sum/02/20140614/",
    "http://db.netkeiba.com/race/sum/03/20140412/",
    "http://db.netkeiba.com/race/sum/04/20140503/",
    "http://db.netkeiba.com/race/sum/05/20140201/",
    "http://db.netkeiba.com/race/sum/06/20140105/",
    "http://db.netkeiba.com/race/sum/07/20140118/",
    "http://db.netkeiba.com/race/sum/08/20140105/",
    "http://db.netkeiba.com/race/sum/09/20140301/",
    "http://db.netkeiba.com/race/sum/10/20140208/"
    ]
#page_getter = page_getter.PageGetter()

#page_getter.get_pages_to_db("http://db.netkeiba.com/race/sum/06/20161225/")

page_parser = page_parser.PageParser()
page_parser.put_race_info_to_db("http://db.netkeiba.com/race/201606050903/")

