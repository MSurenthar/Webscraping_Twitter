import streamlit as st
import snscrape.modules.twitter as sns
import pandas as pd

st.sidebar.title("Tweets on a click")
pd.set_option('display.max_columns', None)
Searc_Key_Word = st.sidebar.text_input("Enter a key word for search")
start_Date=st.sidebar.date_input("Search from Date")
End_Date=st.sidebar.date_input("Search till Date")
range=st.sidebar.slider("Slide the Count of data to extract",0,1000,1)
val=st.sidebar.title(range)
butt=st.sidebar.button("Submit")

data_scrap=f'{Searc_Key_Word} since:{start_Date} until:{End_Date}'
if butt==True:
    st.title("#Tweet's for You")
    for i,tweet in enumerate(sns.TwitterSearchScraper(data_scrap).get_items()):
        if i>range:
            break
        st.write("User : ", tweet.username)
        st.write("Likes : ", tweet.likeCount)
        st.write("Date : ", tweet.date.date())
        st.write("Tweet : ", tweet.renderedContent)
        st.write("ReTweet Count : ", tweet.retweetCount)
        st.write("Tweet Link : ", tweet.url)

        st.write()
        st.write("*"*50)
        st.write()
else:
    st.title("#TWEET's FROM TWITTER")
    st.balloons()