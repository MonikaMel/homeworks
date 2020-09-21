import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from config import DATABASE, SITE_NAME, SITE_PROTOCOL
from model import create_connection, create_table, select_all_links, create_link
from sql import sql_create_links_table

import os
from os import listdir
from os.path import isfile, join
import sys

import re

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

import csv


def get_content(url):
    data = requests.get(url)
    # Checking status code
    status = data.status_code
    if status == 404:
        sys.exit('This page is not available!')
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
    path = os.path.join("/home/monika/parser/python_parser", f"{SITE_NAME}")
    try:
        os.mkdir(path)
    except:
        print('directory already exists')
    finally:
        num = 1
        for i in l:
            if i.startswith(f'{SITE_PROTOCOL + SITE_NAME}'):
                response = requests.get(i)
                with open(os.path.join(path, f"{num}.html"), 'w') as file:
                    file.write(response.text)
                    num += 1
                    print('done')


def get_main_words_of_html(url):
    html_doc = get_content(url)

    text_data = word_tokenize(html_doc.get_text())

    def delete_punctuations(text: str):
        from unicodedata import category
        incomplate = ''.join(n for n in text if not category(n).startswith('P'))
        text_without_punct = ''.join(n for n in incomplate if not category(n).startswith('S'))
        return text_without_punct

    for i in range(len(text_data)):
        text_data[i] = delete_punctuations(text_data[i])

    to_delete = [""]

    text_data_without_punct = [x for x in text_data if x not in to_delete]

    porter = PorterStemmer()
    text_data_with_stem_words = [porter.stem(i) for i in text_data_without_punct]

    stop_words = stopwords.words('english')
    text_data_without_stop_words = [x for x in text_data_with_stem_words if x not in stop_words]
    text_data_without_short_words = [x for x in text_data_without_stop_words if len(x)>2]
    filtered_text_data = list(dict.fromkeys(text_data_without_short_words))
    return filtered_text_data


def get_the_word_matrix(arr):
    matrix = []
    for i in arr:
        l = [i, arr.count(i)]
        if l not in matrix:
            matrix.append(l)
    return matrix


def write_csv_file(file_path):
    filtered = get_main_words_of_html(file_path)
    matrix = get_the_word_matrix(filtered)

    num = 1

    with open(f'{num}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(matrix)
        num += 1
        print('done csv')


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
            write_csv_file(i)


if __name__ == "__main__":
    main()
