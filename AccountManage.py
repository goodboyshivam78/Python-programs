import pandas as pd

df = pd.read_csv("Account_creating_Details.csv")

df.to_csv("Bank_Project\Account_creating_Details.csv",mode='a',index=False,header=False)

df_empty = df.head(0)
#df_empty = df[0:0]
df_empty.to_csv("Account_creating_Details.csv",index=False)