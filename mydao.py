# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

class RaceByHorseDao:
    def create(self, c):
        create_table = """create table race_by_horse
                           (rbh_id integer PRIMARY KEY,
                            horse_id int,
                            race_id int,
                            finished int,
                            waku_ban int,
                            uma_ban int,
                            sex int,
                            age int,
                            jockey_weight int,
                            jockey_id int,
                            time varchar(64),
                            odds,
                            popularity int,
                            weight int,
                            old_flag int
                            )"""
        c.execute(create_table)
        
    def drop(self, c):
        drop_table = "drop table race_by_horse"
        c.execute(drop_table)

    def insert(self, c, tuple_list):
        insert_sql = """insert into race_by_horse
                   (horse_id,
                    race_id,
                    finished,
                    waku_ban,
                    uma_ban,
                    sex,
                    age,
                    jockey_weight,
                    jockey_id,
                    time,
                    odds,
                    popularity,
                    weight,
                    old_flag)
                    values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        c.executemany(insert_sql, tuple_list)

    def select(self, c):
        param =(1,)
        select_sql ="select * from race_by_horse where finished = ?"
        results = c.execute(select_sql, param)
        for res in results:
            print "-------"
            for r in res:
                print r,
        
class RaceDao:
    def create(self, c):
        create_table = """create table race
                       (race_id int PRIMARY_KEY,
                        title varchar(64),
                        place_id int,
                        condition varchar(64),
                        base_info varchar(64)
                        )"""
        c.execute(create_table)
        
    def drop(self, c):
        drop_table = "drop table race"
        c.execute(drop_table)

    def insert(self, c, tuple_list):
        insert_sql = """insert into race
                       (race_id,
                        title,
                        place_id,
                        condition,
                        base_info)
                        values (?,?,?,?,?)"""
        c.execute(insert_sql, tuple_list)

    def select(self, c):
        select_sql ="select * from race"
        results = c.execute(select_sql)
        for res in results:
            print "-------"
            for r in res:
                print r,
            print "-------"

class HorseUrlDao:
    def create(self, c):
        create_table = "create table horse_url (url varchar(64))"
        c.execute(create_table)
        
    def drop(self, c):
        drop_table = "drop table horse_url"
        c.execute(drop_table)

    def insert(self, c, tuple_list):
        insert_sql = "insert into horse_url (url) values (?)"
        c.executemany(insert_sql, tuple_list)

    def select(self, c):
        select_sql ="select * from horse_url"
        results = c.execute(select_sql)
        for res in results:
            print "-------"
            for r in res:
                print r,

class RaceUrlDao:
    def create(self, c):
        create_table = "create table race_url (url varchar(64))"
        c.execute(create_table)
        
    def drop(self, c):
        drop_table = "drop table race_url"
        c.execute(drop_table)

    def insert(self, c, tuple_list):
        insert_sql = "insert into race_url (url) values (?)"
        c.executemany(insert_sql, tuple_list)

    def select(self, c):
        select_sql ="select * from race_url"
        results = c.execute(select_sql)
        for res in results:
            print "-------"
            for r in res:
                print r,
            print "-------"

