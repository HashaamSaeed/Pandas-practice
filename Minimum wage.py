import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 0: invalid start byte
df = pd.read_csv("Minimum Wage Data.csv", encoding="latin")

df.to_csv("minwage.csv", encoding="utf-8") ## convert it to utf-8

df = pd.read_csv("minwage.csv")

# print(df.head())

gb = df.groupby("State")  ## create groups by unique column values
# print(gb.get_group("Alabama").set_index("Year").head())   

## Aside from getting groups, we can also just iterate over the groups to make a dataframe of the grouped names in column headers and cells as Low.2018 data  
act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):  ## name is the name that is grouped by like "alabama" and group is the dataframe each group makes 
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}) ## rename renames colums and takes in a dict of old lable and new label
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

print(act_min_wage.head()) 

# print(act_min_wage.describe())  ## gives an overview of data like count mean etc on the dataframe 

# print(act_min_wage.corr().head())  ## to get correlation or covariance respectively.

issue_df = df[df['Low.2018']==0]

# print(issue_df.head())  ## gives low.2018 vals with zero values
# print(issue_df["State"].unique())  ## gives states with zero vals

# axis 1 == columns. 0,default, is for rows
min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr() ## replaces zero with NaN

for problem in issue_df['State'].unique():  ## problem is basicallt NaN
    if problem in min_wage_corr.columns:
        print("Missing something here....")


grouped_issues = issue_df.groupby("State")

grouped_issues.get_group("Alabama").head(3)       ## get_group gets the specific group mentioned in the bracket 

grouped_issues.get_group("Alabama")['Low.2018'].sum()

for state, data in grouped_issues:
    if data['Low.2018'].sum() != 0.0:
        print("Some data found for", state)

"""        


# Now we visualise the data
########################################################################


df = pd.read_csv("minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))

act_min_wage.head()

min_wage_corr = act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()

print(min_wage_corr.head())

"""

# plt.matshow(min_wage_corr)  ## mathshow Displays an array as a matrix in a new figure window
# plt.show()


labels = [c[:2] for c in min_wage_corr.columns]  # get abbv state names.

fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix
ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

# plt.show()

"""

##########################################################################
## Not important but this is just for the labels and thier abbreviations for USA states to be represneted on the figure 
import requests

web = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")  ## BS4 maybe
dfs = pd.read_html(web.text)    ## Read HTML tables into a list of DataFrame objects. This is from pandas

for df in dfs:
    print(df.head())  # one is states, the other territory


state_abbv = dfs[0]  ## since we get two instances of web elements we choose the first one here being 0

# print(state_abbv.head())


state_abbv[["State/District", "Postal Code"]].to_csv("state_abbv.csv", index=False)  # index in this case is worthless

state_abbv = pd.read_csv("state_abbv.csv", index_col=0)
state_abbv.head()

abbv_dict = state_abbv.to_dict()

abbv_dict = abbv_dict['Postal Code']  ## using the string "postal code"  cuz we need data of that only 

print(abbv_dict)

abbv_dict['Federal (FLSA)'] = "FLSA"   ## we found out it cant map cuz of this one missing value so we put this in the dict
abbv_dict['Guam'] = "GU"
abbv_dict['Puerto Rico'] = "PR"

labels = [abbv_dict[c] for c in min_wage_corr.columns]  # get abbv state names.


fig = plt.figure(figsize=(12,12))  # figure so we can add axis
ax = fig.add_subplot(111)  # define axis, so we can modify
ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn)  # display the matrix
ax.set_xticks(np.arange(len(labels)))  # show them all!
ax.set_yticks(np.arange(len(labels)))  # show them all!
ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

plt.show()