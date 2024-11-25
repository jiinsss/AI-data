from testsql import insert_data1,insert_data2,create_connection

from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.oliveyoung',
    sleep_milliseconds=0, # defaults to 0
    lang='ko', # defaults to 'en'
    country='kr', # defaults to 'us'
)

import pandas as pd
df=pd.DataFrame(result)
df=df[['at','userName','content', 'score', 'thumbsUpCount']]
df.columns = ['시간','유저네임','리뷰','점수','추천수']



#insert
for i in range(len(df)):
    insert_data2(df[df.columns[0]][i],df[df.columns[1]][i],df[df.columns[2]][i],df[df.columns[3]][i],df[df.columns[4]][i])