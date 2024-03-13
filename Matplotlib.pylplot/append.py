import pandas as pd
df = pd.DataFrame(columns =['name', 'age', 'gender','mobile'])

print(df)

df1 = df.loc[0,"name"] = 1
print(df)


#append columns as a list
df.loc[1] = ['Ashoka','25','male','9053189901']
print(df)

#append columns as a dictionary
df.loc[2] = ['Ashoka','25','male','77654654647']
print(df)