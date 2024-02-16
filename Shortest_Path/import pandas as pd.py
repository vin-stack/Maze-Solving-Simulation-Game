import pandas as pd
df=pd.read_csv("E:\Downloads\MLP PROJECT RELAY DATASET SAMPLE ADRAFRUIT IO (RELAY1).csv")
print(df)
startTime = df.created_at.loc[0]
endTime = df.created_at.loc[1]
c=endTime-startTime
print(c)