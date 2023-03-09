import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.title('Iris Dashboard')
df = pd.read_csv('iris.csv')
st.dataframe(df)

fig1,ax = plt.subplots()
ax.scatter(df.iloc[:,0],df.iloc[:,1])
st.pyplot(fig1)

fig2,ax = plt.subplots()
ax.scatter(df.iloc[:,2],df.iloc[:,3])
st.pyplot(fig2)

fig3,ax = plt.subplots()
ax.hist(df.iloc[:,-1])
st.pyplot(fig3)

fig4,ax = plt.subplots()
ax.hist(df.iloc[:,0])
st.pyplot(fig4)

fig5,ax = plt.subplots()
ax.boxplot(df.iloc[:,3])
st.pyplot(fig5)

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.line_chart(df.iloc[:,0])

with col2:
    st.line_chart(df.iloc[:,1])

with col3:
    st.line_chart(df.iloc[:,2])
with col4:
    st.line_chart(df.iloc[:,3])


st.bar_chart(df.iloc[:,0])

col1,col2 = st.columns(2)
with col1:
    st.dataframe(df['sepal_length','sepal_width'])
    fig1,ax = plt.subplots()
    ax.scatter(df.iloc[:,0],df.iloc[:,1])
    st.pyplot(fig1)

with col2:
    st.dataframe(df['petal_length','petal_width'])
    fig2,ax = plt.subplots()
    ax.scatter(df.iloc[:,2],df.iloc[:,3])
    st.pyplot(fig2)
