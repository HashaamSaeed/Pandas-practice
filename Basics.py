import pandas as pd

import matplotlib.pyplot as plt

"""
df = pd.read_csv("avocado.csv") ## definition of a dataframe which is the objext with colums and rows 

# print(df) ## prints the whole dataframe contents

# print(df.head(10)) ## prints the required number of rows from the top
# print(df.tail(2))  ## prints the required number of rows from the bottom 

# print(df["AveragePrice"]) ## prints a specific column

# print(df["AveragePrice"].head(10)) ## prints 10 from top of AveragePrice

albany_df = df[ df['region'] == "Albany" ]   ## We're just saying that the albany_df is the df, where the df['region'] column is equal to Albany. The result is a new dataframe
# print(albany_df)

# print(albany_df.index)   ## gives us the way its indexed but its meaningless

# print(albany_df.set_index("Date"))  ## sets the date column as our index but there is no order 

albany_df = albany_df.set_index("Date") ## thats why we do this and assign the index directly to the albany dataframe
# print(albany_df.head())

# albany_df.set_index("Date", inplace=True) ## this is used if you dont wanna reassign using inplace

# print(albany_df.plot())  ## plotting rthe graph in a bad way 
# print(albany_df["AveragePrice"].plot())  ## plots specific column

# plt.show()

############################################################################################################


df['Date'] = pd.to_datetime(df['Date']) ## basically this tells the pandas that this column is now assigned as the data object

albany_df = df[df['region']=="Albany"]
albany_df.set_index("Date", inplace=True)

# albany_df["AveragePrice"].plot()   ## now it gives a better looking graph 
# plt.show()

# albany_df["AveragePrice"].rolling(25).mean().plot()  ## takes avergae of the 25 rows and condenses them into a mean and then plots it 

albany_df.sort_index(inplace=True)  ## basically our index DATE is now sorted and the new order is replaced in the dataframe

albany_df["AveragePrice"].rolling(25).mean().plot() ## nice smooth graoh that makes sense now 

# plt.show()

albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean() ##  if we want to save our new, smoother, data like above? We can give it a new column in our dataframe

albany_df.dropna().head(3) ## dropna drops the NaN values and removes them to show us  

albany_df = df.copy()[df['region']=="Albany"]  ## the copy command assures that we dont get the stupid warning from pandas
## after the above command do all the stuff that you did before like reassignmetns to make sure you dont get that stupid error again 
albany_df.set_index('Date', inplace=True)
albany_df["price25ma"] = albany_df["AveragePrice"].rolling(25).mean()

print(df['region'].unique())  ## gives us all the unique values in the column


graph_df = pd.DataFrame()  ## initializing a new dataframe

for region in df['region'].unique()[:16]:
    print(region)
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets that are used to refer to not a single val but the whole Datafram
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])  ## join just two dataframe on their index

"""        


df = pd.read_csv("avocado.csv")
df = df.copy()[df['type']=='organic']

df["Date"] = pd.to_datetime(df["Date"])

df.sort_values(by="Date", ascending=True, inplace=True)
df.head()

graph_df = pd.DataFrame()

for region in df['region'].unique():
    region_df = df.copy()[df['region']==region]
    region_df.set_index('Date', inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

    if graph_df.empty:
        graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets! (so df rather than series)
    else:
        graph_df = graph_df.join(region_df[f"{region}_price25ma"])

graph_df.plot()
plt.show()
print(graph_df.tail())