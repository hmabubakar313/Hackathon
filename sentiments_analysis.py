import sqlite3
import tweepy
import time
import sqlite3
from sqlite3 import Error
from textblob import TextBlob

# # Step 1 - Authenticate
consumer_key= '6wjBbpuQBKTCbHcNYl6CD4UdZ'
consumer_secret= '79x2ZZM1aLuVyZ3nG2Xl6SZAvINVM3moCbJnsXQYxvXy3tWAPa' 

access_token='930155901666971648-mwlIrY7EEzNESyrTPeeO2JqYZz0jqSG'
access_token_secret='u92KSrAaJX2ZjeGhni4szJiKfVTcyfJAuow5jikbp0x5f'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# #Step 3 - Retrieve Tweets




# #CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# #and label each one as either 'positive' or 'negative', depending on the sentiment 
# #You can decide the sentiment polarity      threshold yourself

arr1 = []
# while(True):

 



def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT  tag from app1_client_tag"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row)
            INSERT INTO app1_tweets (id polarity subjectivit client_tag_id)
        """     print("Name: ", row[1]) 
            print("Email: ", row[2])
            print("JoiningDate: ", row[3])
            print("Salary: ", row[4])
            print("\n")
 """
   

        

# Values(120,'AutoCAD',50);

        cursor.close()  
        
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()

public_tweets = api.search('row')
for tweet in public_tweets:
        analysis = TextBlob(tweet.text)    
        print(analysis.sentiment)
        if (analysis.sentiment.subjectivity>0):
            arr1.append(analysis.sentiment.polarity)
        print("polarity is ====")
        print(analysis.sentiment.polarity)
        length_arr1=len(arr1)    
        total = sum(arr1)
        print (arr1)
if (analysis.sentiment.polarity>0   and  analysis.sentiment.subjectivity>0):
    print("positive")
else:
        print("negative")

# time.sleep(60)       