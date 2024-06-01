#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('BatteryTempCPV6Averaged.csv')

# Convert time column to datetime format
data['time'] = pd.to_datetime(data['time (yyyy-MM-dd HH:mm:ss.SSS)'])

# Convert temperature column to numeric
data['TCPV6T (C)'] = pd.to_numeric(data['TCPV6T (C)'], errors='coerce')

# Drop rows with missing values
data.dropna(inplace=True)

# Feature scaling
scaler = StandardScaler()
data[['TCPV6T (C)']] = scaler.fit_transform(data[['TCPV6T (C)']])

# Train Isolation Forest model
model = IsolationForest(contamination=0.05)
model.fit(data[['TCPV6T (C)']])

# Predict outliers
data['anomaly'] = model.predict(data[['TCPV6T (C)']])
data['anomaly'] = data['anomaly'].apply(lambda x: 1 if x == -1 else 0)

# Visualize anomalies
plt.figure(figsize=(15, 6))
plt.plot(data['time'], data['TCPV6T (C)'], color='blue', label='Temperature')
plt.scatter(data[data['anomaly'] == 1]['time'], data[data['anomaly'] == 1]['TCPV6T (C)'], color='red', label='Anomaly')
plt.title('Battery Temperature Anomaly Detection')
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.legend()
plt.show()


# In[ ]:




