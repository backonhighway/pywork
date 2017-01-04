# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import sqlite3
from time import sleep
import mydao

class PageParser:
    def __init__(self):
        self.base_url = "http://db.netkeiba.com"
    
    def getConnection(self):
        dbname = 'main_database.db'
        conn = sqlite3.connect(dbname)
        return conn.cursor()

    def get_race_info(self, soup, url):
        race_title = soup.find("h1").text
        race_condition = soup.find("diary_snap_cut").find("span").text
        race_base_info = soup.find("p", {"class":"smalltxt"}).text
        race_url = url.split("/")[-2]
        place_id = race_url[4:6]

        return (race_url, race_title, place_id, race_condition, race_base_info)

    def get_race_by_horse_info(self, soup, url):
        main_table = soup.find("table", {"class":"race_table_01"})
        tr_list = main_table.find_all("tr")
        race_url = url.split("/")[-2]

        row_list = []

        for i, tr in enumerate(tr_list):
            if i == 0:
                continue
            td_list = tr.findAll("td")
            finished = td_list[0].text
            waku_ban= td_list[1].text
            uma_ban = td_list[2].text
            horse_id = td_list[3].find("a")["href"].split("/")[2]
            sex_age = td_list[4].text
            sex = list(sex_age)[0]
            age = list(sex_age)[1]
            jockey_weight = td_list[5].text
            jockey_id = td_list[6].find("a")["href"].split("/")[2]
            time = td_list[7].text
            #diff, timeindex, passed, halftime is skipped
            odds = td_list[12].text
            popularity = td_list[13].text
            weight= td_list[14].text.split("(")[0]    
            row = (horse_id, race_url, finished, waku_ban, uma_ban, sex, age,
                  jockey_weight, jockey_id, unicode(time), odds, popularity, weight, 0)
            row_list.append(row)
            
            #for r in row:
            #   print r
        return row_list

    def put_race_info_to_db(self, url):
        soup = BeautifulSoup(urllib2.urlopen(url), "html.parser")
        race_info = self.get_race_info(soup, url)
        race_by_horse_info = self.get_race_by_horse_info(soup, url)

        c = self.getConnection()
        r_dao = mydao.RaceDao()
        r_dao.insert(c, race_info)
        rbh_dao = mydao.RaceByHorseDao()
        rbh_dao.insert(c, race_by_horse_info)

        r_dao.select(c)
        rbh_dao.select(c)
        
        c.close()

        print "parsed page"

        
    
