#!/usr/bin/env python
# coding: utf-8

# In[14]:


import psycopg2
import time
import requests
import json

conn = psycopg2.connect(host='pg.pg4e.com',
        port='5432',
        database='pg4e_4b5009906e',
        user='pg4e_4b5009906e',
        password='pg4e_p_4c160cb47372904',
        connect_timeout=3)

cur = conn.cursor()

defaulturl = 'https://pokeapi.co/api/v2/pokemon/'

sql = 'CREATE TABLE IF NOT EXISTS pokeapi (id INTEGER, body JSONB);'

cur.execute(sql)

for i in range(1, 101):
    int_val = i
    response = requests.get(defaulturl+str(i))
    text = response.text
    sql = 'INSERT INTO pokeapi (id, body) VALUES (%s, %s);'
    cur.execute(sql, (int_val,text))
    conn.commit()

