import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

#Reads in the csv files
df1 = pd.read_csv('data/Mental_Health-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv')
df2 = pd.read_csv('data/Employment-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv')
df3 = pd.read_csv('data/Age-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv')
df4 = pd.read_csv('data/Income-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv')
df5 = pd.read_csv('data/Race_and_Ethnic_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv')

dataframes = {
    "Mental Health": df1,
    "Employment": df2,
    "Age": df3,
    "Income": df4,
    "Race/Ethnic": df5
}

#combine all csv files into one dataframe
df = pd.concat(dataframes.values(), ignore_index=True)

#strip column names, convert them to lowercase, replace spaces with _ and () with nothing
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('(', '', regex=False)
    .str.replace(')', '', regex=False)
)

#Convert year column to numeric
df['year'] = pd.to_numeric(df['year'],errors='coerce')


#Create new column names, convert current columns to numeric and get rid of %
df['focus_prevalence_num'] = pd.to_numeric(df['cigarette_use_prevalence_%_focus_group'].str.replace('%', '', regex=False),errors='coerce')
df['reference_prevalence_num'] = pd.to_numeric(df['cigarette_use_prevalence_%_reference_group'].str.replace('%', '', regex=False),errors='coerce')
df['disparity_value_num'] = pd.to_numeric(df['disparity_value'].str.replace('%', '', regex=False),errors='coerce')


#Drop unnecessary columns
df = df.drop([
    'cigarette_use_prevalence_%_focus_group',
    'cigarette_use_prevalence_%_reference_group',
    'disparity_value'
], axis=1)



#Fills null values with median value
df['focus_prevalence_num'].fillna(df['focus_prevalence_num'].median(), inplace=True)
df['reference_prevalence_num'].fillna(df['reference_prevalence_num'].median(), inplace=True)
df['disparity_value_num'].fillna(df['disparity_value_num'].median(), inplace=True)

#should we get rid of the tobacco use column since its all the same values?? 
#get rid of "age" before the age number 
#split up employed or self and student or homemaker
#Change 65 or older 
#get rid of From and $ in income and less than or above- just make it a number? 
#get rid of non-hispanic in front of other ethnicties 

#creates a new csv file with cleaned data 
output_path = "data/cleaned_data.csv"
df.to_csv(output_path, index=False)

print(f"Cleaned data saved to: {output_path}")
print(df.info())




