from streamlit_extras.colored_header import colored_header
from streamlit_card import card
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import pandas as pd
st.set_page_config(page_title="Insights",page_icon=":bar_chart:",layout="wide")

hide_menu_style='''
<style>
#MainMenu {visibility:hidden;}
footer {visibility: hidden;}
</style>
'''
st.markdown(hide_menu_style,unsafe_allow_html=True)
st.sidebar.success("Explore Different pages for more info")

df=pd.read_csv("final_forbes.csv")
def bar_country():
    st.header("Top 10 highest number of companies:")
    data_country={"Country":["United States","China","Japan","South Korea","United Kingdom","Canada","India","France","Hong Kong","Germany"],"Number of Companies":[584,297,196,65,64,64,55,54,54,52]}
    df_country=pd.DataFrame(data_country)
    st.bar_chart(df_country,x="Country",y="Number of Companies")

def show_pairplot():
    st.header("Pairplots:")
    st.write('##')
    sns.pairplot(df,x_vars=['Sales','Profits'],y_vars=['Assets','Market Value'])
    st.pyplot()

def pie_industry():
    st.header("Weightage of Countries:")
    Number_of_companies=[290,146,127,124,118,106,105,83,81,75,744]
    Industry=["Banking","Diversified Financials","Construction","Consumer Durables","Materials","Oil & Gas Operations","Insurance","Utilities","Business Services & Supplies","Chemicals","Others"]
    plt.pie(Number_of_companies,labels=Industry)
    st.pyplot()

def show_corr():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Correlation between the columns:")
    sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="RdBu")
    st.pyplot()

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding1=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_rnbPNXolKz.json")
l1,r1=st.columns((0.4,0.6))
with l1:
    st.title("Finally!!")
    st.title("To The Conclusion of this project!")
    st.title("INSIGHTS✨")
    st.write("This page includes the important insights derived from the Forbes Global 2000 Dataset.")

with r1:
    st_lottie(lottie_coding1,height=480,key="insights7")

l2,r2=st.columns((0.5,0.5))
with l2:
    show_corr()
with r2:
    st.title("INSIGHT#1")
l3,r3=st.columns(2)
with l3:
    st.title("INSIGHT#2")
with r3:
    bar_country()

l4,r4=st.columns(2)
with l4:
    pie_industry()
with r4:
    st.title("INSIGHT#3")

l5,r5=st.columns(2)
with l5:
    st.title("INSIGHT#4")
with r5:
    show_pairplot()