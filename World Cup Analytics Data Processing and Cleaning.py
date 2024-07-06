#!/usr/bin/env python
# coding: utf-8

# In[186]:


import pandas as pd
import numpy as np
import json


# In[187]:


# load the match summary json and convert to df
with open(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\JSON files\t20_wc_match_results.json") as f:
    data = json.load(f)
match = pd.DataFrame(data[0]['matchSummary'])


# In[188]:


# clean match summary df
match.rename({'scorecard':'match_id'},axis=1,inplace = True)


# In[189]:


# load the batting summary json and convert to df
with open(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\JSON files\t20_wc_batting_summary.json") as f:
    data = json.load(f)
all=[]  
for games in data:
    all.extend(games['battingSummary'])
batting = pd.DataFrame(all)


# In[190]:


# clean batting summary
batting['out/notout'] = batting['dismissal'].apply(lambda x: 'out' if len(x)>0 else 'not out')
batting.drop(columns = ['dismissal'],inplace=True)


# In[191]:


# clean batting summary
batting['batsmanName'] = batting['batsmanName'].apply(lambda x: x.replace('â€',''))
batting['batsmanName'] = batting['batsmanName'].apply(lambda x: x.replace('\xa0',''))
batting['batsmanName'] = batting['batsmanName'].apply(lambda x: x.replace('(c)',''))
batting['batsmanName'] = batting['batsmanName'].apply(lambda x: x.replace('(wk)',''))


# In[192]:


# create a dictionary with matchid and teams
ids = {}
for index, row in match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']
    ids[key1] = row['match_id']
    ids[key2] = row['match_id']
# adding the match id to the batting summary table
batting['match_id'] = batting['match'].map(ids)


# In[193]:


# load the bowling summary json and convert to df
with open (r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\JSON files\t20_wc_bowling_summary.json") as f:
    data = json.load(f)
all=[]
for row in data:
    all.extend(row['bowlingSummary'])
bowling = pd.DataFrame(all)
    


# In[194]:


# cleaning the bowling table
bowling['bowlerName'] = bowling['bowlerName'].apply(lambda x: x.replace('â€',''))
bowling['bowlerName'] = bowling['bowlerName'].apply(lambda x: x.replace('\xa0',''))
bowling['bowlerName'] = bowling['bowlerName'].apply(lambda x: x.replace('(c)',''))
bowling['bowlerName'] = bowling['bowlerName'].apply(lambda x: x.replace('(wk)',''))


# In[195]:


# adding match id to the bowling summary
bowling['match_id'] = bowling['match'].map(ids)


# In[196]:


# loading the player info json and convert to df
with open(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\JSON files\t20_wc_player_info.json") as f:
    data = json.load(f)
player = pd.DataFrame(data)


# In[197]:


# cleaning the player summary
player['name'] = player['name'].apply(lambda x: x.replace('â€',''))
player['name'] = player['name'].apply(lambda x: x.replace('\xa0',''))
player['name'] = player['name'].apply(lambda x: x.replace('(c)',''))
player['name'] = player['name'].apply(lambda x: x.replace('(wk)',''))


# In[198]:


# exporting the csv files
match.to_csv(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\CSV files/match.csv",index=False)
batting.to_csv(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\CSV files/batting.csv",index=False)
bowling.to_csv(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\CSV files/bowling.csv",index=False)
player.to_csv(r"C:\Users\nisha\OneDrive\Desktop\World Cup Analytics\CSV files/player.csv",index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




