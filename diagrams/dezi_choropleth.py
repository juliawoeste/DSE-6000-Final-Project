import plotly.express as px 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('Data/cleaned_data.csv') 

df_filter = df[(df['demographic'] == 'Mental Health') 
               & (df['comparing_focus_group'] == 'Severe Mental Distress') 
                & (df['to_reference_group'] == 'No Mental Distress')] 


final_df = df_filter[['year','state', 'disparity_value_num']] 


state_to_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

final_df['state_code'] = final_df['state'].map(state_to_abbrev) 

fig = px.choropleth(data_frame=final_df, locations='state_code', locationmode='USA-states', 
                    color='disparity_value_num', scope='usa', color_continuous_scale='Reds', animation_frame='year', animation_group='state_code',
                    labels={'disparity_value_num': 'Smoking Disparity Between Severe Distress and No Distress'}, 
                    title='Smoke Disparities of Heavy Stress Vs No Stress Levels From 2011-2023') 

fig.show() 

