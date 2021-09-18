# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import sqlite3
from itemadapter import ItemAdapter
from scrapy import settings
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class PlacasScraperPipeline:
    dbfile = settings.get('SQLITE_FILE')
    dbtable = settings.get('SQLITE_TABLE')

    def __init__(self):
        self.setup_db_conn()
        self.create_tables()

    def setup_db_conn(self):
        self.con = sqlite3.connect(self.dbfile)
        self.cur = self.con.cursor()

    def create_tables(self):
        self.drop_db_tables()
        self.create_db_tables()
    
    def drop_db_tables(self):
        print(f"Droping old table: {self.dbtable}")
        self.cur.execute(f"DROP TABLE IF EXISTS {self.dbtable}")

    def close_db(self):
        self.con.close()
    
    def __del__(self):
        self.close_db()

    def create_db_tables(self):
        print(f"Creating new table: {self.dbtable}")
        cols = "produto TEXT, preco REAL, numr_de_fotos INTEGER, url_img TEXT, datahora_pub TEXT"
        sql = f"CREATE TABLE IF NOT EXISTS {self.dbtable} (id INTEGER PRIMARY KEY NOT NULL, {cols})"

    def store_in_db(self, item):
        sql = f"INSERT INTO {self.dbtable} ({','.join(item.keys())}) values ({','.join(item.values())})"
        self.cur.execute(sql) 
        self.con.commit()   
    
    def format_item(self, item):
        datahora_pub = item.get('datahora_pub')
        if (datahora_pub is not None):
            if (len(datahora_pub) > 0):
                nova_datahora_pub = ' '.join(datahora_pub).strip()
                novo_item = item.copy()
                novo_item['datahora_pub'] = nova_datahora_pub
                return novo_item
        return ''

    def process_item(self, item, spider):
        self.store_in_db(self.format_item(item))
        return item
