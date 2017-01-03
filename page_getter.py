# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import sqlite3
from time import sleep
import mydao

class PageGetter:
    def __init__(self):
        self.base_url = "http://db.netkeiba.com"
    
    def getConnection():
        dbname = 'main_database.db'
        conn = sqlite3.connect(dbname)
        return conn.cursor()

    def get_race_pages(self, soup):
        main_table = soup.find("table", {"class":"race_table_01"})
        tr_list = main_table.find_all("tr")
        race_list = []

        for i, tr in enumerate(tr_list):
            #header
            if i == 0:
                continue
                
            td_list = tr.findAll("td")
            td = td_list[1]
            link = self.base_url + td.find("a")["href"]
            print link
            race_list.append((link,))
        return race_list

    def get_next_page(self, soup):
        li = soup.find("li", {"class": "next"})
        check = li.find("a")
        if not check:
            return None
        next_page = li.find("a")["href"]
        return self.base_url + next_page

    def get_pages_to_db(self, url):
        soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")
        race_list = self.get_race_pages(soup)
        
        #c = getConnection()
        #race_url_dao = mydao.RaceUrlDao()
        #race_url_dao.insert(c, race_list)
        #race_url_dao.select(c)
        #c.close()

        next_page = self.get_next_page(soup)
        if not next_page:
            print "no more pages, ending..."
            return

        print "done one page, going for next..."
        sleep(5)
        self.get_pages_to_db(next_page)
    
