import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import os
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
# Analysis of Climate Patterns
This web-app analyses **Climate Change**!
""")

st.sidebar.header('Slide To Adjust Temperatures')



st.sidebar.write("""**2016**""")
JT_1 = st.sidebar.slider('Jan', -20, 50, 7, key="5")
AT_1 = st.sidebar.slider('April', -20, 50, 12, key="6")
JU_1 = st.sidebar.slider('July', -20, 50, 19, key="7")
OT_1 = st.sidebar.slider('October', -20, 50, 17, key="8")
data_1 = (JT_1,AT_1,JU_1,OT_1)

st.sidebar.write("""**2017**""")
JT_2 = st.sidebar.slider('Jan', -20, 50, 9, key="9")
AT_2 = st.sidebar.slider('April', -20, 50, 15, key="10")
JU_2 = st.sidebar.slider('July', -20, 50, 22, key="11")
OT_2 = st.sidebar.slider('October', -20, 50, 18, key="12")
data_2 = (JT_2,AT_2,JU_2,OT_2)

st.sidebar.write("""**2018**""")
JT_3 = st.sidebar.slider('Jan', -20, 50, 5, key="13")
AT_3 = st.sidebar.slider('April', -20, 50, 17, key="14")
JU_3 = st.sidebar.slider('July', -20, 50, 20, key="15")
OT_3 = st.sidebar.slider('October', -20, 50, 19, key="16")
data_3 = (JT_3,AT_3,JU_3,OT_3)

st.sidebar.write("""**2019**""")
JT_4 = st.sidebar.slider('Jan', -20, 50, 10, key="17")
AT_4 = st.sidebar.slider('April', -20, 50, 19, key="18")
JU_4 = st.sidebar.slider('July', -20, 50, 17, key="19")
OT_4 = st.sidebar.slider('October', -20, 50, 20, key="20")
data_4 = (JT_4,AT_4,JU_4,OT_4)


data = [(data_0),(data_1),(data_2),(data_3),(data_4)]

df = pd.DataFrame(data, columns=['January','April','July','October'],index=['2015','2016','2017','2018','2019'])
st.subheader('Quarterly Temperatures')
st.write(df)

a=st.write(sns.heatmap(df,annot=True))
plt.gcf()
if st.button('Download Temperatures Dataframe',key="1"):
    df.to_csv("C:\\Users\\lenovo\\Desktop\\Python Projects\\Climate.csv")
if st.button('Download Climate Heatmap',key="2"):
    plt.savefig("Climate.png")
st.pyplot()

s=df.values.sum()
if(s<0):
    st.write("# The climate has been cold in this place over 2015-2019")

if(s>0):
    st.write("# The climate has been relatively warm during 2015-2019")
    
st.subheader('Correlation Stats')

dfc = df.corr()

st.write(dfc)

b=st.write(sns.heatmap(dfc,annot=True))
plt.gcf()
if st.button('Download Correlation Dataframe',key="3"):
    dfc.to_csv("C:\\Users\\lenovo\\Desktop\\Python Projects\\climate_corr.csv")
if st.button('Download Correlation Heatmap',key="4"):
    plt.savefig("Climate_Correlation.png")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)


