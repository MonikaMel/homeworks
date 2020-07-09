import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


r = requests.get("https://httpstatuses.com/")
html = r.text
soup = BeautifulSoup(html, 'html.parser')
text_data = word_tokenize(soup.get_text())

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

filtered_text_data = list(dict.fromkeys(text_data_without_stop_words))
