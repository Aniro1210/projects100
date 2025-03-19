from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model=AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

tokens=tokenizer.encode('I loved it',return_tensors='pt')

result=model(tokens)

r=requests.get('https://www.trustpilot.com/review/www.dugood.org')
soup=BeautifulSoup(r.text,'html.parser')
regex = re.compile(r'.*typography_body-l__KUYFJ.*typography_appearance-default__AAY17.*typography_color-black__5LYEn.*')
results=soup.find_all('p',{'class':regex})
reviews=[result.text for result in results]

df=pd.DataFrame(np.array(reviews),columns=['review'])

def sentiment_score(review):
    tokens=tokenizer.encode(review,return_tensors='pt')
    result=model(tokens)
    return int(torch.argmax(result.logits))+1

df['sentiment']=df['review'].apply(lambda x:sentiment_score(x[:512]))

df
