import csv
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier

# Reading the csv files and replacing the unneccassary values like '..' with nan 
world = pd.read_csv("world.csv",encoding='ISO-8859-1', na_values = ['..'])
life = pd.read_csv("life.csv", encoding='ISO-8859-1')

# Merging the two csv files based on the country code 
result = world.merge(life, on = 'Country Code', how = 'inner' )

# Replacing the nan values with the median and sorting the dataframe alphabtically according to the country code 
result.fillna(result.median(), inplace=True)
result.sort_values('Country Code', inplace = True)

# Storing the features and the classlabel separately 
data = result[['Access to electricity (% of population) [EG.ELC.ACCS.ZS]','Adjusted net national income per capita (current US$) [NY.ADJ.NNTY.PC.CD]','Age dependency ratio (% of working-age population) [SP.POP.DPND]','Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total) [SH.DTH.COMM.ZS]','Current health expenditure per capita (current US$) [SH.XPD.CHEX.PC.CD]','Fertility rate, total (births per woman) [SP.DYN.TFRT.IN]','Fixed broadband subscriptions (per 100 people) [IT.NET.BBND.P2]','Fixed telephone subscriptions (per 100 people) [IT.MLT.MAIN.P2]','GDP per capita (constant 2010 US$) [NY.GDP.PCAP.KD]','GNI per capita, Atlas method (current US$) [NY.GNP.PCAP.CD]','Individuals using the Internet (% of population) [IT.NET.USER.ZS]','Lifetime risk of maternal death (%) [SH.MMR.RISK.ZS]','People using at least basic drinking water services (% of population) [SH.H2O.BASW.ZS]','People using at least basic drinking water services, rural (% of rural population) [SH.H2O.BASW.RU.ZS]','People using at least basic drinking water services, urban (% of urban population) [SH.H2O.BASW.UR.ZS]','People using at least basic sanitation services, urban (% of urban population) [SH.STA.BASS.UR.ZS]','Prevalence of anemia among children (% of children under 5) [SH.ANM.CHLD.ZS]','Secure Internet servers (per 1 million people) [IT.NET.SECR.P6]','Self-employed, female (% of female employment) (modeled ILO estimate) [SL.EMP.SELF.FE.ZS]','Wage and salaried workers, female (% of female employment) (modeled ILO estimate) [SL.EMP.WORK.FE.ZS]']].astype(float)
classlabel = result['Life expectancy at birth (years)']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, classlabel, train_size=0.70, test_size=0.30, random_state=200)

# Scaling by removing the mean and scaling to unit variance.
scaler = preprocessing.StandardScaler().fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

# Applying the decision tree classfier and calculating the accuracy scores
dt = DecisionTreeClassifier(random_state=200, max_depth=3)
dt.fit(X_train, y_train)
y_pred=dt.predict(X_test)
print('Accuracy of decision tree: ',round(accuracy_score(y_test, y_pred), 3))

# Applying the knn classfier with n=3 and calculating the accuracy scores
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred=knn.predict(X_test)
print("Accuracy of k-nn (k=3): ",round(accuracy_score(y_test, y_pred), 3))

# Applying the knn classfier with n=7 and calculating the accuracy scores
knn = neighbors.KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred=knn.predict(X_test)
print("Accuracy of k-nn (k=7): ", round(accuracy_score(y_test, y_pred), 3))

# Calulating the median used for imputation of each feature
median = result.mean(axis = 0)

# Calulating the mean and variance for scaling 
mean = result.mean(axis = 0)
variance = result.var(axis=0)

# Storing the values of median, mean and variance of each feature in lists 
medians = [round(row, 3) for row in median[1:-1]]
means = [round(row, 3) for row in mean[1:-1]]
variances = [round(row, 3) for row in variance[1:-1]]

# Getting the feature names
cols = (result.columns)[3:-3]

# Converting the above data to a dataframe 
medians_series = pd.Series(medians)
means_series = pd.Series(means)
variances_series = pd.Series(variances)
cols_series = pd.Series(cols)
df = pd.DataFrame({'feature': cols_series, 'median': medians_series, 'mean': means_series, 'variance':variances_series})

# Converting the above dataframe to a csv file  
df.to_csv('task2a.csv', index = False)
      