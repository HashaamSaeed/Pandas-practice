import pandas as pd

df = pd.read_csv("diamonds.csv", index_col=0)
df.head()

df['cut'].unique()

cut_class_dict = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}

# df["cut"].astype("category").cat.codes     ## does what we do above ## this basciallty converts classes into numbers 

df['clarity'].unique()

clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL": 11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}

df['cut'] = df['cut'].map(cut_class_dict)
df['clarity'] = df['clarity'].map(clarity_dict)
df['color'] = df['color'].map(color_dict)
df.head()




## another way to do things above 
import sklearn
from sklearn import svm, preprocessing
from sklearn.linear_model import SGDRegressor

df = sklearn.utils.shuffle(df) # always shuffle your data to avoid any biases that may emerge b/c of some order.

X = df.drop("price", axis=1).values
X = preprocessing.scale(X)
y = df["price"].values

test_size = 200

X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR(kernel="linear")

clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))    ## score 0 is bad 1 is good   ##  The score for these regression models is r-squared/coefficient of determination, 


## for visualization of a few results 
for X,y in list(zip(X_test, y_test))[:10]:
    print(f"model predicts {clf.predict([X])[0]}, real value: {y}")  ## clf.predict passes the vals in the model 


## The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
 # and then the second item in each passed iterator are paired together etc.
 # If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.    


"""
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(x)  >> <zip object at 0x2b338ba13c48>
print(tuple(x))   >> (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))


"""

print('newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww methooooooooooooooooooooddddddddddddddddddddddddddddddddddddddddddd\n')


clf = SGDRegressor(max_iter=1000)
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

for X,y in list(zip(X_test, y_test))[:10]:
    print(f"model predicts {clf.predict([X])[0]}, real value: {y}")





