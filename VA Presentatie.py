#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import streamlit as st
#!pip list


# In[2]:


df = pd.read_csv('BigmacPrice.csv')


# In[3]:


#datum omzetten naar echte datum
#df['date'] = pd.to_datetime(df['date'])
df.info()


# In[4]:


df.head()


# In[5]:


#dataset controleren op NaN values
df.isna().sum()


# In[6]:


#alle unieke waardes van de landen ophalen
df['name'].unique()


# In[7]:


#alle verschillende landen groeperen in de behorende continenten
df['europe'] = df['name'].isin(['Britain', 'Czech Republic', 'Denmark', 'Euro area', 'Hungary', 'Poland', 'Sweden',
                         'Switzerland', 'Norway', 'Ukraine', 'Austria', 'Belgium', 'Estonia', 'Finland', 'France',
                         'Germany', 'Greece', 'Ireland', 'Italy', 'Netherlands', 'Portugal', 'Spain', 'Lithuania',
                         'Croatia', 'Latvia', 'Moldova', 'Romania', 'Slovakia', 'Slovenia'])

df['africa'] = df['name'].isin(['South Africa', 'Egypt'])

df['northamerica'] = df['name'].isin(['Canada', 'Mexico', 'United States', 'Costa Rica', 'Guatemala', 'Honduras', 'Nicaragua'])

df['southamerica'] = df['name'].isin(['Argentina', 'Brazil', 'Chile', 'Peru', 'Venezuela', 'Colombia', 'Uruguay'])

df['asia'] = df['name'].isin(['China', 'Hong Kong', 'Indonesia', 'Israel', 'Japan', 'Malaysia', 'Russia', 'Singapore',
                       'South Korea', 'Taiwan', 'Thailand', 'Philippines', 'Turkey', 'Pakistan', 'Saudi Arabia',
                       'Sri Lanka', 'UAE', 'India', 'Vietnam', 'Azerbaijan', 'Bahrain', 'Jordan', 'Kuwait',
                       'Lebanon', 'Oman', 'Qatar', 'United Arab Emirates'])

df['australia'] = df['name'].isin(['Australia', 'New Zealand'])


# In[8]:


df


# In[9]:


#alle continenten eigen dataframe geven voor 2021 en 2022
df_eur = df[((df['europe'] == True) & (df['date'] == '2022-07-01')) | ((df['europe'] == True) & (df['date'] == '2021-07-01'))]

df_afr = df[((df['africa'] == True) & (df['date'] == '2022-07-01')) | ((df['africa'] == True) & (df['date'] == '2021-07-01'))]

df_nam = df[((df['northamerica'] == True) & (df['date'] == '2022-07-01')) | ((df['northamerica'] == True) & (df['date'] == '2021-07-01'))]

df_sam = df[((df['southamerica'] == True) & (df['date'] == '2022-07-01')) | ((df['southamerica'] == True) & (df['date'] == '2021-07-01'))]

df_asi = df[((df['asia'] == True) & (df['date'] == '2022-07-01')) | ((df['asia'] == True) & (df['date'] == '2021-07-01'))]

df_aus = df[((df['australia'] == True) & (df['date'] == '2022-07-01')) | ((df['australia'] == True) & (df['date'] == '2021-07-01'))]


# In[10]:


#van alle landen alleen de jaren 2021 en 2022 pakken en eigen dataframe voor geven
df_2122 = df[(df['date'] == '2022-07-01') | (df['date'] == '2021-07-01')]

#2021 en 2022 splitsen in eigen dataframe per jaar
df_21 = df[df['date'] == '2021-07-01']
df_22 = df[df['date'] == '2022-07-01']


# In[11]:


#voor elk continent figuur aanmaken die de gemiddelde prijs van de landen laat zien
fig1 = px.histogram(df_eur, x='name', y='dollar_price', histfunc='avg', color='date', barmode='group', #color_discrete_sequence=['#1f77b4'],
                   title='Gemiddelde prijs van een BigMac in Europa in 2021 en 2022')
fig1.update_xaxes(categoryorder='category ascending', tickmode='linear')
fig1.update_layout(width=900, height=500)
fig1.update_layout({'xaxis': {'title': {'text': 'Land'}},
                   'yaxis': {'title':{'text': 'Gemiddelde prijs in dollar'}},
                   'legend': {'title':{'text': 'Datum'}}})

fig2 = px.histogram(df_afr, x='name', y='dollar_price', histfunc='avg', color='date', barmode='group', #color_discrete_sequence=['#ff7f0e'],
                   title='Gemiddelde prijs van een BigMac in Afrika in 2021 en 2022')
fig2.update_xaxes(categoryorder='category ascending', tickmode='linear')
fig2.update_layout(width=900, height=500)
fig2.update_layout({'xaxis': {'title': {'text': 'Land'}},
                   'yaxis': {'title':{'text': 'Gemiddelde prijs in dollar'}},
                   'legend': {'title':{'text': 'Datum'}}})

fig3 = px.histogram(df_nam, x='name', y='dollar_price', histfunc='avg', color='date', barmode='group', #color_discrete_sequence=['#2ca02c'],
                   title='Gemiddelde prijs van een BigMac in Noord- en Midden-Amerika in 2021 en 2022')
fig3.update_xaxes(categoryorder='category ascending', tickmode='linear')
fig3.update_layout(width=900, height=500)
fig3.update_layout({'xaxis': {'title': {'text': 'Land'}},
                   'yaxis': {'title':{'text': 'Gemiddelde prijs in dollar'}},
                   'legend': {'title':{'text': 'Datum'}}})

fig4 = px.histogram(df_sam, x='name', y='dollar_price', histfunc='avg', color='date', barmode='group', #color_discrete_sequence=['#d62728'],
                   title='Gemiddelde prijs van een BigMac in Zuid-Amerika in 2021 en 2022')
fig4.update_xaxes(categoryorder='category ascending', tickmode='linear')
fig4.update_layout(width=900, height=500)
fig4.update_layout({'xaxis': {'title': {'text': 'Land'}},
                   'yaxis': {'title':{'text': 'Gemiddelde prijs in dollar'}},
                   'legend': {'title':{'text': 'Datum'}}})

fig5 = px.histogram(df_asi, x='name', y='dollar_price', histfunc='avg', color='date', barmode='group', #color_discrete_sequence=['#9467bd'],
                   title='Gemiddelde prijs van een BigMac in Azië in 2021 en 2022')
fig5.update_xaxes(categoryorder='category ascending', tickmode='linear')
fig5.update_layout(width=900, height=500)
fig5.update_layout({'xaxis': {'title': {'text': 'Land'}},
                   'yaxis': {'title':{'text': 'Gemiddelde prijs in dollar'}},
                   'legend': {'title':{'text': 'Datum'}}})

fig6 = px.histogram(df_aus, x='name', y='dollar_price', histfunc='avg', color='date', barmode='group', #color_discrete_sequence=['#7f7f7f'],
                   title='Gemiddelde prijs van een BigMac in Australië in 2021 en 2022')
fig6.update_xaxes(categoryorder='category ascending', tickmode='linear')
fig6.update_layout(width=900, height=500)
fig6.update_layout({'xaxis': {'title': {'text': 'Land'}},
                   'yaxis': {'title':{'text': 'Gemiddelde prijs in dollar'}},
                   'legend': {'title':{'text': 'Datum'}}})


fig1.show()
st.plotly_chart(fig1)
fig2.show()
st.plotly_chart(fig2)
fig3.show()
st.plotly_chart(fig3)
fig4.show()
st.plotly_chart(fig4)
fig5.show()
st.plotly_chart(fig5)
fig6.show()
st.plotly_chart(fig6)


# In[12]:


#boxplot in violinvorm met scatter die de verdeling van de prijs weergeeft
fig = px.violin(df_2122, y='dollar_price', box=True, points='all', color='date',
                title='De verdeling van de prijs van de BigMac over de wereld in 2021 en 2022')
fig.update_layout({'xaxis': {'title': {'text': 'Alle landen samen'}},
                   'yaxis': {'title':{'text': 'Prijs in dollar'}},
                  'legend': {'title':{'text': 'Datum'}}})
fig.show()
st.plotly_chart(fig)


# In[13]:


#boxplotten in violinvorm per continent in 1 figuur om het verschil in prijsverdeling te zien in 2021
fig1 = go.Figure()

fig1.add_trace(go.Violin(x=df_21['europe'][df_21['europe']==True], y=df_21['dollar_price'], name="Europa"))
fig1.add_trace(go.Violin(x=df_21['africa'][df_21['africa']==True], y=df_21['dollar_price'], name="Afrika"))
fig1.add_trace(go.Violin(x=df_21['northamerica'][df_21['northamerica']==True], y=df_21['dollar_price'], name="Noord- en Midden-Amerika"))
fig1.add_trace(go.Violin(x=df_21['southamerica'][df_21['southamerica']==True], y=df_21['dollar_price'], name="Zuid-Amerika"))
fig1.add_trace(go.Violin(x=df_21['asia'][df_21['asia']==True], y=df_21['dollar_price'], name="Azië"))
fig1.add_trace(go.Violin(x=df_21['australia'][df_21['australia']==True], y=df_21['dollar_price'], name="Australië"))

fig1.update_traces(box_visible=True, meanline_visible=True)
fig1.update_layout(violinmode='group', title_text='De verdeling van de prijs van de BigMac over de continenten in 2021')
fig1.update_layout({'xaxis': {'title': {'text': 'De verschillende continenten'}},
                   'yaxis': {'title':{'text': 'Prijs in dollar'}},
                  'legend': {'title':{'text': 'Continenten'}}})

#boxplotten in violinvorm per continent in 1 figuur om het verschil in prijsverdeling te zien in 2022
fig2 = go.Figure()

fig2.add_trace(go.Violin(x=df_22['europe'][df_22['europe']==True], y=df_22['dollar_price'], name="Europa"))
fig2.add_trace(go.Violin(x=df_22['africa'][df_22['africa']==True], y=df_22['dollar_price'], name="Afrika"))
fig2.add_trace(go.Violin(x=df_22['northamerica'][df_22['northamerica']==True], y=df_22['dollar_price'], name="Noord- en Midden-Amerika"))
fig2.add_trace(go.Violin(x=df_22['southamerica'][df_22['southamerica']==True], y=df_22['dollar_price'], name="Zuid-Amerika"))
fig2.add_trace(go.Violin(x=df_22['asia'][df_22['asia']==True], y=df_22['dollar_price'], name="Azië"))
fig2.add_trace(go.Violin(x=df_22['australia'][df_22['australia']==True], y=df_22['dollar_price'], name="Australië"))

fig2.update_traces(box_visible=True, meanline_visible=True)
fig2.update_layout(violinmode='group', title_text='De verdeling van de prijs van de BigMac over de continenten in 2022')
fig2.update_layout({'xaxis': {'title': {'text': 'De verschillende continenten'}},
                   'yaxis': {'title':{'text': 'Prijs in dollar'}},
                  'legend': {'title':{'text': 'Continenten'}}})

fig1.show()
st.plotly_chart(fig1)
fig2.show()
st.plotly_chart(fig2)

