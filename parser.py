import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from config import DATABASE, SITE_NAME, SITE_PROTOCOL
from model import create_connection, create_table, select_all_links, create_link
from sql import sql_create_links_table

import os
from os import listdir
from os.path import isfile, join
import os.path
from os import path

import sys
from unicodedata import category

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.hello
words = db.words

priority = {"h1": 10, "h2": 9, "h3": 8, "h4": 7, "h5": 6, "h6": 5, "p": 2}


def get_content(url):
    data = requests.get(url)
    # Checking status code
    status = data.status_code
    if not str(status).startswith("2"):
        sys.exit("This page is not available!")
    else:
        soup = BeautifulSoup(data.text, 'html.parser')
        return soup


def get_page_links(soup, conn):
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
                create_link(conn, (o.scheme, o.netloc, o.path))
    return links


def collect_link(d):
    params = list(d.values())
    param = params[0] + '://' + "/".join(params[1:])
    return param


def recollect_links(links):
    l = []
    for i in links:
        l.append(collect_link(i))
    return l


def create_html_files(l):
    p = os.path.join("/home/monika/parser/python_parser", f"{SITE_NAME}")
    if path.exists(f'{p}') == False:
        os.mkdir(p)
        num = 1
        for i in l:
            if i.startswith(f'{SITE_PROTOCOL + SITE_NAME}'):
                response = requests.get(i)
                with open(os.path.join(p, f"{num}.html"), 'w') as file:
                    file.write(response.text)
                    num += 1
                    print('done')
    else:
        print('directory already exists')


def get_main_words_of_html(url):
    html_doc = get_content(url)
    text_data = word_tokenize(html_doc.get_text())

    porter = PorterStemmer()
    stop_words = stopwords.words('english')

    def delete_punctuations(text: str):
        to_delete = [""]
        incomplate = ''.join(n for n in text if not category(n).startswith('P'))
        almost = ''.join(n for n in incomplate if not category(n).startswith('S'))
        comlate = [x for x in almost if x not in to_delete]
        return comlate

    for i in range(len(text_data)):
        text_data[i] = delete_punctuations(text_data[i])

    data_with_stem_words = [porter.stem(i) for i in text_data]
    data_without_stop_words = [x for x in data_with_stem_words if x not in stop_words]
    data_without_short_words = [x for x in data_without_stop_words if len(x)>2]
    filtered_text_data = list(dict.fromkeys(data_without_short_words))
    return filtered_text_data


def get_the_word_list(arr, path):
    word_list = []
    for i in arr:
        count = arr.count(i)
        l = {"word": f"{i}", "count": f"{count}", "path": f"{path}"}
        if l not in word_list:
            word_list.append(l)
    return word_list


def write_db(file_path):
    filtered = get_main_words_of_html(file_path)
    word_list = get_the_word_list(filtered, file_path)
    words.insert_many(word_list)


def main():
    conn = create_connection(DATABASE)

    if conn is not None:
        create_table(conn, sql_create_links_table)

        soup = get_content(SITE_PROTOCOL + SITE_NAME)
        links = get_page_links(soup, conn)
        select_all_links(conn)
        l = recollect_links(links)
        create_html_files(l)

        onlyfiles = [join("/home/monika/parser/python_parser/foodtime.am", f)
                     for f in listdir("/home/monika/parser/python_parser/foodtime.am")
                     if isfile(join("/home/monika/parser/python_parser/foodtime.am", f))]

        for i in onlyfiles:
            write_db(i)


if __name__ == "__main__":
    main()
