# Data-linkage-and-classification-system

This project implements and evaluates a data linkage system and a classification system using
sound data science principles. It implements a data linkage on two real-world datasets (Part 1) and
explores different classification algorithms (Part 2).

Part 1 - 

Abt and Buy both have product databases. In order to perform joint market research they
need to link the same products in their databases. Therefore the research team has manually
linked a subset of the data in order to build a linkage algorithm to automate the remaining
items to be linked. The real dataset us unknown.

Naive data linkage without blocking:

For this part, data linkage without blocking is performed on two smaller data sets:
abt small.csv and buy small.csv.

Task - 1A:
1) Using abt small.csv and buy small.csv, implement the linkage between the
two data sets.
2) The code should produce a single csv file task1a.csv containing the following two column headings:
idAbt,idBuy
3) Each row in the datafile must contain a pair of matched products. For example, if the
algorithm only matched product 10102 from the Abt dataset with product
203897877 from the Buy dataset the output task1a.csv would be as follows:

idAbt, idBuy
10102,203897877

4) The performance is evaluated in terms of recall and precision.
recall = tp/(tp + fn)
precision = tp/(tp + f p)
where tp (true-positive) is the number of true positive pairs, f p the number of false positive
pairs, tn the number of true negatives, and fn the number of false negative pairs.


Blocking for efficient data linkage

Blocking is a method to reduce the computational cost for record linkage.

Task - 1B:
1) Implement a blocking method for the linkage of the abt.csv and buy.csv data
sets.
2) The code must produce two csv files abt blocks.csv and buy blocks.csv, each containing the following two column
headings:
block_key, product_id

3)The product id field corresponds to the idAbt and idBuy of the abt.csv and buy.csv files
respectively. Each row in the output files matches a product to a block. For example, if the
algorithm placed product 10102 from the Abt dataset in blocks with block keys x & y, the
abt blocks.csv would be as follows:
block_key, product_id
x,10102
y,10102

4) A block is uniquely identified by the block key. The same block key in the two block-files
(abt blocks.csv and buy blocks.csv) indicates that the corresponding products co-occur
in the same block.
For example, if the algorithm placed the Abt product 10102 in block x and placed Buy
product 203897877 in block x, your abt blocks.csv and buy blocks.csv would be as follows
respectively:

abt_blocks.csv:
block_key, product_id
x,10102

buy_blocks.csv:
block_key, product_id
x,203897877

5) The two products co-occur in the same block x.

6) To measure the quality of blocking, we assume that when comparing a pair of records, the
pair are always 100% similar and are a match. A pair of records are categorised as follows:
 a record-pair is a true positive if the pair are found in the ground truth set and also the
pair co-occur in the same block.
 a record-pair is a false positive if the pair co-occur in some block but are not found in
the ground truth set.
 a record-pair is a false negative if the pair do not co-occur in any block but are found
in the ground truth set
3
 a record-pair is a true negative if the pair do not co-occur in any block and are also not
found in the ground truth set.

7) Then, the quality of blocking can be evaluated using the following two measures:
P C (pair completeness) = tp/(tp + fn)
RR (reduction ratio) = 1 − (tp + fp)/n
where n is the total number of all possible record pairs from the two data sets
(n = f p + fn + tp + tn).

The overall report of Part 2 is included in the file task1c.


Part 2 - Classification 

Each year, the World Bank publishes the World Development Indicators which provide high
quality and international comparable statistics about global development and the fight against
poverty. As data scientists, we wish to understand how the information can be used to
predict average lifespan in different countries. To this end, we have provided the world.csv
file, which contains some of the World Development Indicators for each country and the
life.csv file containing information about the average lifespan for each country (based on
data from the World Health Organization. Each data file also contains a country name,
country code and year as identifiers for each record. These may be used to link the two
datasets but should not be considered features.

Comparing Classification Algorithms

Task - 2A
1) Compare the performance of the following 3 classification algorithms: k-NN (k=3
and k=7) and Decision tree (with a maximum depth of 3) on the provided data
2) Use each classification algorithm to predict the class feature life expectancy at birth(years) of the data (Low, Medium and
High life expectancy) using the remaining features.
3) For each of the algorithms, fit a model with the following processing steps:

 Split the dataset into a training set comprising 70% of the data and a test set comprising
the remaining 30% using the train test split function with a random state of 200.
 Perform the same imputation and scaling to the training set:
– For each feature, perform median imputation to impute missing values.
– Scale each feature by removing the mean and scaling to unit variance.
 Train the classifiers using the training set
 Test the classifiers by applying them to the test set


Feature Engineering and Selection
Task - 2B
1) This task will focus on k-NN with k=3 (from here on referred to as 3-NN).
2) In order to achieve higher prediction accuracy for 3-NN, one can investigate the use of feature
engineering and selection to predict the class feature of the data. Feature generation involves
the creation of additional features. Two possible methods are:

 Interaction term pairs. Given a pair of features f1 and f2, create a new feature f12 =
f1 × f2. All possible pairs can be considered.
 Clustering labels: apply k-means clustering to the data in world and then use the
resulting cluster labels as the values for a new feature fclusterlabel. You will need to
decide how many clusters to use. At test time, a label for a testing instance can be
created by assigning it to its nearest cluster.
Given a set of N features (the original features plus generated features), feature selection
involves selecting a smaller set of n features (n < N).

3)An alternative method of performing feature engineering & selection is to use Principal Component Analysis (PCA). The first n principal components can be used as features.

The task in this question is to evaluate how the above methods for feature engineering and
selection affect the prediction accuracy compared to using 3-NN on a subset of the original
features in world. The code should - 

 Implement feature engineering using interaction term pairs and clustering labels. This
should produce a dataset with 211 features (20 original features, 190 features generated
by interaction term pairs and 1 feature generated by clustering). You should (in some
principled manner) select 4 features from this dataset and perform 3-NN classification.
 Implement feature engineering and selection via PCA by taking the first four principal
components. You should use only these four features to perform 3-NN classification.
 Take the first four features (columns D-G, if the dataset is opened in Excel) from the
original dataset as a sample of the original 20 features. Perform 3-NN classification.

The overall report of Part 2 is included in the file task2c.

