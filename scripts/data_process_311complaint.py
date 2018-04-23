import pandas as pd
import numpy as np
from sodapy import Socrata
import os
import time

client = Socrata("data.cityofnewyork.us", os.getenv("apptoken"))

results = client.get("fhrw-4uyv",
                     select = "created_date, complaint_type",
                     where="created_date > '2010-01-01T00:00:12.000' and created_date < '2011-01-01T00:00:12.000'",
                     limit=670000)
df = pd.DataFrame.from_records(results)
df.dropna(inplace=True)

countgroup = df.groupby(by='complaint_type').count()
countgroup.reset_index(inplace=True)
countgroup.sort_values('created_date', ascending=False, inplace=True)

top = countgroup.head(21)
top_ = top.drop([57])
top_.columns = ['complaint_type', 'total_2010']
top_.head()

top20list = top_.complaint_type.tolist()

#initial
results = client.get("fhrw-4uyv",
                     select = "incident_zip, created_date, complaint_type",
                     where="created_date > '2010-01-01T00:00:12.000' and created_date < '2011-01-01T00:00:12.000' " +
                     "and complaint_type = 'Water System'",
                     limit=670000)
df = pd.DataFrame.from_records(results)
df.dropna(inplace=True)

countgroup = df.groupby(by='incident_zip').count()
countgroup.reset_index(inplace=True)
countgroup.sort_values('created_date', ascending=False, inplace=True)
countgroup.reset_index(inplace=True, drop=True)
countgroup.drop("complaint_type", inplace=True, axis=1)
countgroup.columns = ['incident_zip', 'Water System']

for i,name in enumerate (top20list[1:]):    
    randtime = np.random.random(98) + np.random.randint(2,8,98)
    time.sleep(randtime[i-2])   
    results = client.get("fhrw-4uyv",
                     select = "incident_zip, created_date, complaint_type",
                     where="created_date > '2010-01-01T00:00:12.000' and created_date < '2011-01-01T00:00:12.000' " +
                     "and complaint_type = '" + str(name) + "' ",
                     limit=670000)
    df = pd.DataFrame.from_records(results)
    df.dropna(inplace=True)
    countgr = df.groupby(by='incident_zip').count()
    countgr.reset_index(inplace=True)
    countgr.sort_values('created_date', ascending=False, inplace=True)
    countgr.reset_index(inplace=True, drop=True)
    countgr.drop("complaint_type", inplace=True, axis=1)
    countgr.columns = ['incident_zip', name]
    countgroup = pd.merge(countgroup, countgr, how='outer', on='incident_zip')
    
call2010 = countgroup.fillna(0.5)
col2010 = call2010.columns.tolist()

newname2010 = []
for i in col2010:
    if i=='incident_zip':
        newname2010.append(i)
    else:
        temp = i+'2010'
        newname2010.append(temp)

call2010.columns = newname2010
call2010['sum2010'] = call2010.iloc[:, 1:21].T.sum()

#initial
results = client.get("fhrw-4uyv",
                     select = "incident_zip, created_date, complaint_type",
                     where="created_date > '2015-01-01T00:00:12.000' and created_date < '2016-01-01T00:00:12.000' " +
                     "and complaint_type = 'Water System'",
                     limit=670000)
df = pd.DataFrame.from_records(results)
df.dropna(inplace=True)

countgroup15 = df.groupby(by='incident_zip').count()
countgroup15.reset_index(inplace=True)
countgroup15.sort_values('created_date', ascending=False, inplace=True)
countgroup15.reset_index(inplace=True, drop=True)
countgroup15.drop("complaint_type", inplace=True, axis=1)
countgroup15.columns = ['incident_zip', 'Water System']

for i,name in enumerate (top20list[1:]):
    randtime = np.random.random(98) + np.random.randint(2,8,98)
    time.sleep(randtime[i-2])
    
    results = client.get("fhrw-4uyv",
                     select = "incident_zip, created_date, complaint_type",
                     where="created_date > '2015-01-01T00:00:12.000' and created_date < '2016-01-01T00:00:12.000' " +
                     "and complaint_type = '" + str(name) + "' ",
                     limit=670000)
    df = pd.DataFrame.from_records(results)
    df.dropna(inplace=True)
    countgr = df.groupby(by='incident_zip').count()
    countgr.reset_index(inplace=True)
    countgr.sort_values('created_date', ascending=False, inplace=True)
    countgr.reset_index(inplace=True, drop=True)
    countgr.drop("complaint_type", inplace=True, axis=1)
    countgr.columns = ['incident_zip', name]

    countgroup15 = pd.merge(countgroup15, countgr, how='outer', on='incident_zip')
    
call2015 = countgroup15.fillna(0.5)
col2015 = call2015.columns.tolist()

newname2015 = []
for i in col2015:
    if i=='incident_zip':
        newname2015.append(i)
    else:
        temp = i+'2015'
        newname2015.append(temp)

call2015.columns = newname2015
call2015['sum2015'] = call2015.iloc[:, 1:21].T.sum()

df_10_15 = pd.merge(call2010, call2015, on='incident_zip')

df_10_15.to_csv("df_10_15.csv")

