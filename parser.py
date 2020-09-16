import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

import sqlite3
from sqlite3 import Error

DATABASE = "/Users/voskan/Desktop/python_parser/parser.db"
SITE_NAME = "nodejs.org"
SITE_PROTOCOL = "https://"

sql_create_links_table = ''' CREATE TABLE IF NOT EXISTS links (
    id integer PRIMARY KEY,
    path text NOT NULL,
    domain text,
    protocol text
) '''

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_link(conn, link_data):
    sql = ''' INSERT INTO links(path, domain, protocol)
                VALUES(?,?,?) '''
    
    c = conn.cursor()
    c.execute(sql, link_data)
    conn.commit()
    return c.lastrowid

def select_all_links(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM links")
    
    rows = c.fetchall()

    for row in rows:
        print(row)

def get_content(url):
    data = requests.get(url)
    # Ստուգումներ անել ստատուս կոդ և այլն...
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup

def get_page_links(soup):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        o = urlparse(href)
        
        if o.path:
            flag = False
            if o.netloc == SITE_NAME or not o.netloc:
                flag = True
                if len(links) > 0:
                    # այս մասում տունը մտածել այլ տարբերակ
                    for data in links:
                        if data.get('path') == o.path:
                            flag = False
            
            if flag:
                links.append({'protocol': o.scheme, 'domain': o.netloc, 'path': o.path})

    return links

def main():
    conn = create_connection(DATABASE)

    if conn is not None:
        create_table(conn, sql_create_links_table)

        select_all_links(conn)

        # soup = get_content(SITE_PROTOCOL + SITE_NAME)
        # links = get_page_links(soup)

        # for data in links:
        #     link_data = (data.get('path'), data.get('domain'), data.get('protocol'))
        #     lastrowid = create_link(conn, link_data)
        #     print(lastrowid)

if __name__ == "__main__":
    main()