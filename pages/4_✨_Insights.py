from streamlit_extras.colored_header import colored_header
from streamlit_card import card
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import seaborn as sns
sns.set_style("darkgrid")
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

bright_palette = ["#FF875D", "#FFB386", "#FFE7C2", "#8BD2C1", "#B8C8E3", "#D8C2EA", "#F7E2FD", "#E6E6E6", "#C6C6C6", "#E8E8E8"]

sns.set_palette(bright_palette)

def bar_country():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Top 10 highest number of companies based on Country:")
    data_country={"Country":["United States","China","Japan","South Korea","United Kingdom","Canada","India","France","Hong Kong","Germany"],"Number of Companies":[584,297,196,65,64,64,55,54,54,52]}
    df_country=pd.DataFrame(data_country)
    bright_palette = ["#FF0018", "#FFA52C", "#FFFF41", "#008018", "#0000F9", "#86007D", "#FF007C", "#9A4E00", "#7F7F7F", "#FFFFFF"]
    ax=sns.barplot(df_country,x="Number of Companies",y="Country",width= 1,palette=bright_palette)
    for i in ax.containers:# display values
        ax.bar_label(i,)
    st.pyplot()
df=pd.read_csv("final_forbes.csv")

def show_pairplot():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Pairplots:")
    st.write('##')
    sns.pairplot(df,x_vars=['Sales','Profits'],y_vars=['Assets','Market Value'])
    st.pyplot()


def pie_industry():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Weightage of Industries in the rankings:")
    Number_of_companies=[290,146,127,124,118,106,105,83,81,75,744]
    Industry=["Banking","Diversified Financials","Construction","Consumer Durables","Materials","Oil & Gas Operations","Insurance","Utilities","Business Services & Supplies","Chemicals","Others"]
    pi=plt.pie(Number_of_companies,labels=Industry,autopct='%1.1f%%',pctdistance=0.85)
    for text in pi[2]:
        text.set_color('black')
    st.pyplot()


def show_corr():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Correlation between the columns:")
    st.write("##")
    sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="Blues",vmax=1,vmin=-1)
    st.pyplot()

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding1=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_rnbPNXolKz.json")
st.success("You can sort in the DataFrame Explorer to get the information on maximum and minimum metrics")
l1,r1=st.columns((0.4,0.6))
with l1:
    st.title("Finally!!")
    st.title("To The Conclusion of this project!")
    st.title("INSIGHTS✨")
    st.write("This page includes the important insights derived from the Forbes Global 2000 Dataset.")

with r1:
    st_lottie(lottie_coding1,height=480,key="insights7")
st.write("---")
l2,r2=st.columns((0.5,0.5))
with l2:
    show_corr()
with r2:
    st.title("INSIGHT#1")
    st.write("##")
    st.write('''
    - Correlation coefficients measure how strong and in which direction two variables are linked in a straight line.
    - A high correlation signifies a high collinearity i.e., they are highly proportional. For e.g.,A correlation of 1 signifies they are similar in nature.
    - Negative correlation signifies that if one column is increasing in nature so the correlated column will be decreasing in nature.
    - This implies that investors and market participants believe that higher profitability will lead to a higher valuation of the company.
    ''')
st.write("---")
l3,r3=st.columns(2)
with l3:
    st.title("INSIGHT#2")
    st.write("##")
    st.write('''- This count plot shows the number of companies from the top 10 countries with highest contribution in the rankings.
- Here, the United States stand at the top with highest count which signifies the economical strength of the country in the market.
- India stands at 7th place in top 10.
                ''')
with r3:
    bar_country()
st.write("---")
l4,r4=st.columns(2)
with l4:
    pie_industry()
with r4:
    st.title("INSIGHT#3")
    st.write("##")
    st.write('''- This pie chart represents the proportion of the industries in the rankings.
- Here, Banking industries dominates the global economy.
- "Others" include the industries which couldn't make it to the top 10(You can view them in the dataframe explorer).
    ''')
st.write("---")
l5,r5=st.columns(2)
with l5:
    st.title("INSIGHT#4")
    st.write("##")
    st.write('''- This plot comprises of four scatter plots which are actually combination of the 4 metrics used in the rankings.
- These scatter plots are very helpful in the clustering operation of companies on any 2 factors.
- Per axis, only 2 variables are chosen in order to avoid redundancy.
''')
with r5:
    show_pairplot()
st.write("---")
l6,r6=st.columns(2)
with l6:
    st.header("Line plot for all 4 metrics(Top 20):")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    select=st.selectbox("What metric do you want to see?",["Overall Comparison","Market Value","Profits","Assets","Sales"])
    if select=="Market Value":
        sns.lineplot(df.head(20),x="Company",y="Market Value",color="orange")
        plt.xticks(rotation=90)
        st.pyplot()
    elif select=="Profits":    
        sns.lineplot(df.head(20),x="Company",y="Profits",color="blue")
        plt.xticks(rotation=90)
        st.pyplot()
    elif select=="Assets": 
        sns.lineplot(df.head(20),x="Company",y="Assets",color="grey")
        plt.xticks(rotation=90)
        st.pyplot()
    elif select=="Sales":     
        sns.lineplot(df.head(20),x="Company",y="Sales",color="pink")
        plt.xticks(rotation=90)
        st.pyplot()
    elif select=="Overall Comparison":
        sns.lineplot(df.head(20),x="Company",y="Market Value",color="orange",label="Market Value")
        sns.lineplot(df.head(20),x="Company",y="Profits",color="blue",label="Profits")
        sns.lineplot(df.head(20),x="Company",y="Assets",color="grey",label="Assets")
        sns.lineplot(df.head(20),x="Company",y="Sales",color="pink",label="Sales")
        plt.ylabel("Metrics")
        plt.legend()
        plt.xticks(rotation=90)
        st.pyplot()

with r6:
    st.title("INSIGHT#5")
    st.write('''- The Assets of the banking industries is the highest in the rankings.
- From the line graph, there are some companies whose market value is lower than their assets which indicates that the market does not value the company's assets as highly as their book value suggests.
- The Assets are slowly decreasing as the rank increases where the maxima at 18th rank has decreased a lot.
- Companies with high MV and low assets could suggest that investors have high expectations for the company's future earnings potential, growth prospects, or intangible assets that are not reflected in the book value of its assets.
''')
st.write("---")
st.write("##")
c1,c2=st.columns((0.4,0.6))
with c1:
    lottiecoding2=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_a18slqgx.json")
    st_lottie(lottiecoding2)
with c2:
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.header("This marks the end of this project🌸")
    st.markdown("### Hope you liked it")
    st.title("THANK  YOU!")