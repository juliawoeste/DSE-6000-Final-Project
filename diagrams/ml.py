import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error 
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv('data/cleaned_data.csv') 
#print(df.head())
focus_encoder = OrdinalEncoder() 
df['focus_encoded'] = focus_encoder.fit_transform(df[['comparing_focus_group']]) 

ref_encoder = OrdinalEncoder() 
df['reference_encoded'] = ref_encoder.fit_transform(df[['to_reference_group']])  


x = df[['focus_encoded', 'reference_encoded', 'focus_prevalence_num', 'reference_prevalence_num']] 
y = df['disparity_value_num'] 

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size= .2, random_state=42)  

#Linear Regression 
model_lr = LinearRegression() 
model_lr.fit(x_train, y_train) 
pred_lr = model_lr.predict(x_test) 
mse_lr = mean_squared_error(y_test, pred_lr) 

#Random Forest 
model_rf = RandomForestRegressor() 
model_rf.fit(x_train, y_train) 
pred_rf = model_rf.predict(x_test) 
mse_rf = mean_squared_error(y_test, pred_rf)  

print(f"Linear Regression MSE: {mse_lr}")
print(f"Random Forest MSE: {mse_rf}")

best_model = model_rf 

focus_groups = sorted(df['comparing_focus_group'].unique()) 
reference_groups = sorted(df['to_reference_group'].unique()) 
