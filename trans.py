import pandas as pd
import json
df=pd.read_csv('beatCount.csv')
print(df)
# print(list(df['doc']))
# print(list(df['topic']))
x=list(df['Beat'])
y=list(df['counts'])
dict={}
for i in range(0,len(x)):
    x[i]=str(x[i])
    if len(x[i])==3:
         x[i]='0'+x[i]
    dict[str(x[i])]=int(y[i])
dict['3100']=int(307)
print(dict)
f2 = open('count.json', 'w', encoding='utf-8')
# # print(dict_new)
# # print(type(dict_new))
jsObj = json.dumps(dict)
f2.write(jsObj)
f2.close()