# python script
import pandas as pd
import re
from fuzzywuzzy import fuzz
df = pd.read_excel("/path/to/excelfile")
dff = df.replace(r'n',' ', regex=True) #removes 'n' from trail
a = dff['Master_Description'].str.lower()
b = dff['Description'].str.lower()
c = dff['Master_Article_Code'].values
acc = [None] * len(b)
dis = [None] * len(b)
po_dis = []
for j in range(len(b)):
    for i in range(len(a)):
        ratio1 = fuzz.token_sort_ratio(a[i], b[j]) #Comparing two string using fuzzy
        if  ratio1 >=90:
#            acc.append(c[j])
#            dis.append(a[j])
            acc.insert(j,c[i])
            dis.insert(j,a[i])
# for x in range(len(acc)):
#     if  acc[x] == None && dis[x] == None:
#         acc.insert(x,"Not Found")
#         dis.insert(x,"Not Found")
if len(acc) == 0:
    acc.append("Not found")
    po_dis.append("Not found")
    dfx= pd.DataFrame(list(zip(acc,po_dis)),columns =['Article code','Master Description'])
    result = pd.concat([dff,dfx], axis=1, sort=True)
    print("WRONG",dfx)
else:
    dfx= pd.DataFrame(list(zip(acc,dis)),columns =['Article code','Master Description'])
    result = pd.concat([dff,dfx], axis=1, sort=True)#appending two dataframes
    print(result)
