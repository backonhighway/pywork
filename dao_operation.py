# -*- coding: utf-8 -*-

import sqlite3
import mydao

dbname = 'main_database.db'

conn = sqlite3.connect(dbname)
c = conn.cursor()

dao = mydao.RaceUrlDao()
dao.drop(c)
