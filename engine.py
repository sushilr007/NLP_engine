import pandas as pd
from fuzzywuzzy import fuzz


df = pd.read_csv("pathto/csvfile/.csv")


a = df['Description '].values
b = df['Article_description'].values
c = df['Article Code '].values

for i in range(len(b)):
    for j in range(len(a)):
        ratio = fuzz.token_sort_ratio(a[i], b[j]) #Will compare two strings for matching will return ratio
        if ratio >= 90:
            print(c[i],a[i],ratio)
