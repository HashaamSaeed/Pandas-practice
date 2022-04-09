import pandas as pd
import numpy as np

unemp_county = pd.read_csv("output.csv")
print(unemp_county.head())


df = pd.read_csv("minwage.csv")

act_min_wage = pd.DataFrame()

for name, group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage = group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name})
    else:
        act_min_wage = act_min_wage.join(group.set_index("Year")[["Low.2018"]].rename(columns={"Low.2018":name}))


# print(act_min_wage.head())


act_min_wage = act_min_wage.replace(0, np.NaN).dropna(axis=1)
print(act_min_wage.head())

def get_min_wage(year, state):  ## this function is used later on to extract value from the act_min_wage dataframe to another dataframe 
    try:
        return act_min_wage.loc[year][state]   ## Access a group of rows and columns by label(s) or a boolean array, .loc[] is primarily label based, but may also be used with a boolean array.
    except:
        return np.NaN

# print(get_min_wage(2012, "Colorado"))  ## gives val in speciic cell to the given arguments     


unemp_county['min_wage'] = list(map(get_min_wage, unemp_county['Year'], unemp_county['State'])) ## Map values of Series according to input correspondence. 
                                                                                                ## Used for substituting each value in a Series with another value, that may be derived from a function, a dict or a

## the map() is a weird function because you dont define functions inside of it the usual way and you name it like above without (), and arguments
## are passed seperately after commas                                                                                                

print(unemp_county.head())                   

##  checking the relationship in data
# print(unemp_county[['Rate','min_wage']].corr())  ## corellation 
# print(unemp_county[['Rate','min_wage']].cov())   ## covariance 


pres16 = pd.read_csv("pres16results.csv")

print(pres16.head())

top_candidates = pres16.head(10)['cand'].values ## Let's include the top 10 candidates. To grab their names

county_2015 = unemp_county[ (unemp_county['Year']==2015) & (unemp_county["Month"]=="February")]  ## All data in unemp_county but with month as feb and year as 2015

state_abbv = pd.read_csv("state_abbv.csv", index_col=0)    ## Now, for county_2015, we'd like to convert the State to the all-caps abbreviation that our pres16 is using. We can do that using our abbreviations that we used before

state_abbv_dict = state_abbv.to_dict()['Postal Code']

county_2015['State'] = county_2015['State'].map(state_abbv_dict)   ## another form of map() as seen above 
## In the case of singe-parmeter functions, we can just use a .map. 
 # Or...as you just saw here, if you want to map a key to a value using a dict, you can do the same thing, and just say you want to map the dictionary. 

## checking if their lengths match up 
print(len(county_2015))   ## >> 2802
print(len(pres16))        ## >> 18475


## Since pres16 is longer, we'll map that to county_15, where there are matches. 
 # Instead of a map, however, we'll combine with a join. To do this, let's index both of these. They are indexed by state AND county. 
 # So, we'll name these both the same, and then index as such.

## pres16.columns ## gives the column names
pres16.rename(columns={"county": "County", "st": "State"}, inplace=True) ## renaming columns 
pres16.head()


for df in [county_2015, pres16]:
    df.set_index(["County", "State"], inplace=True)  ## setting double index


pres16 = pres16[pres16['cand']=="Donald Trump"]
pres16 = pres16[['pct']]
pres16.dropna(inplace=True)


all_together = county_2015.merge(pres16, on=["County", "State"])  ## merging two dataframes 
all_together.dropna(inplace=True)
all_together.drop("Year", axis=1, inplace=True)  ## removes Year column , axis =1 cuz we want column gone not rows = 0 

all_together.corr()
all_together.cov()