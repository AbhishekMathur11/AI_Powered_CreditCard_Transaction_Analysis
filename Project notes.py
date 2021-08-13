#IMPORTING AND USING LIBRARIES

import pandas as pd

creditcard_df = pd.read_csv('Marketing_data.csv')

creditcard_df

#MINI CHALLENGE 1

print("Average of the balance =",creditcard_df['BALANCE'].mean())
print("Maximum of the balance =",creditcard_df['BALANCE'].max())
print("Minimum of the balance =",creditcard_df['BALANCE'].min())


#DESCRIBING THE DATABASE STATISTICALLY

creditcard_df.describe()

#MINI CHALLENGE 2
#To find customer details of who has maximum one off credit purchase
creditcard_df[creditcard_df['ONEOFF_PURCHASE']== creditcard_df['ONEOFF_PURCHASE'].max()]

#To find details of customer who has maximum cash advance

creditcard_df[creditcard_df['CASH_ADVANCE']==creditcard_df['CASH_ADVANCE'].max()]

#Visualising and exploring datasets
import seaborn as sns
sns.heatmap(creditcard_df.isnull(), yticklabels = False, cbar = False, cmap="Blues")

creditcard_df.isnull().sum()#displays total number of missing elements in each coulumn

#to replace the missing values with mean value in minimum payments

creditcard_df.loc[(creditcard_df['MINIMUM_VALUES'].isnull()==True),'MINIMUM_PAYMENTS']=creditcard_df['MINIMUM_PAYMENTS'].mean()

# MINI CHALLENGE 3
creditcard_df.loc[(creditcard_df['CREDIT_LIMIT'].isnull()==True),'CREDIT_LIMIT']=creditcard_df['CREDIT_LIMIT'].mean()
#check
creditcard_df.isnull().sum()

#Checking duplicated entries in dataset
creditcard_df.duplicated().sum()

#MINI CHALLENGE 4
#TO DROP VALUES OF A SINGLE COLUMN CUST_ID FROM THE DATA'
#METHOD 1
for i in creditcard_df['CUST_ID']:
    print(i)

#METHOD 2
creditcard_df.drop('CUST_ID',axis=1,inplace=True)
creditcard_df
#To check total columns in database
creditcard_df.columns()

#Creating a KDE plot for the data

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,50))
for i in range(len(creditcard_df.columns)):
  plt.subplot(17, 1, i+1)
  sns.distplot(creditcard_df[creditcard_df.columns[i]], kde_kws={"color": "b", "lw": 3, "label": "KDE"}, hist_kws={"color": "g"})
  plt.title(creditcard_df.columns[i])

plt.tight_layout()

plt.show()
#MINI CHALLENGE 5
#Plotting the correlation matrix
plt.matshow(creditcard_df.corr())
#or
correlations=creditcard_df.corr()
f,ax=plt.subplots(figsize=(20,10))
sns.heatmap(correlations,annot = True)

#Important points about K means clustering
#K-means terminates after a fixed number of iterations is reached
#K-means terminates when the centroid locations do not change between iterations


#STEP ONE IS TO FIND OUT THE OPTIMAL NUMBER OF CLUSTERS REQUIRED FOR THE DATA(VALUE OF K)
#THE PROCESS IS ITERATIVE WITH A EW CENTROID FORMED AND SUM OF SQUARES OF DISTANCES FROM EACH POINT FROM ITS CENTROID IS CALCULATED
#ELBOW METHOD IS USED FOR THIS. THE SUM OF SQUARE OF DISTANCES IS PLOTTED WITH NUMBER OF CLUSTERS K
import sklearn
from sklearn.preprocessing import StandardScaler, normalize

scaler= StandardScaler()
creditcard_df_scaled.shape
creditcard_df_scaled
#Plotting the required graph
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler,normalize
scaler = StandardScaler()
creditcard_df_scaled = scaler.fit_transform(creditcard_df)
scores_1=[]
range_values=range(1,20)
for i in range_values:
    kmeans= KMeans(n_clusters = i)
    kmeans.fit(creditcard_df_scaled)
    scores_1.append(kmeans.inertia_)

plt.plot(scores_1,'bx-')
#MINI CHALLENGE
#FOR RUNNING ONLY THE FIRST SEVEN COLUMNS
creditcard_df_scaled[:,:7]
scores_1=[]
range_values=range(1,20)
for i in range_values:
    kmeans= KMeans(n_clusters = i)
    kmeans.fit(creditcard_df_scaled[:,:7])
    scores_1.append(kmeans.inertia_)


#Forming clusters based on four groups
# First Customers cluster (Transactors): Those are customers who pay least amount of intrerest charges and careful with their money, Cluster with lowest balance ($104) and cash advance ($303), Percentage of full payment = 23%
# Second customers cluster (revolvers) who use credit card as a loan (most lucrative sector): highest balance ($5000) and cash advance (~$5000), low purchase frequency, high cash advance frequency (0.5), high cash advance transactions (16) and low percentage of full payment (3%)
# Third customer cluster (VIP/Prime): high credit limit $16K and highest percentage of full payment, target for increase credit limit and increase spending habits
# Fourth customer cluster (low tenure): these are customers with low tenure (7 years), low balance 

kmeans=KMeans(7)#Number of clusters here are 7
kmeans.fit(creditcard_df_scaled)
labels=kmeans.labels_

kmeans.clusters_centers_.shape
cluster_centers=pd.DataFrame(data=kemans.cluster_centers_,columns=[creditcard_df_scaled])
cluster_centers

cluster_centers = scaler.inverse_transform(cluster_centers)

#Labels
labels.shape() #to check the total labels

labels.max()

labels.min()
#Plotting histogram of clusters
for i in creditcard_df.columns:
    plt.figure(figsize=(35,5))
    for j in range(7):
        plt.subplot(1,7,j+1)
        cluster=creditcard_df_cluster[creditcard_df_cluster['cluster']==j]
        cluster[i].hist(bins=20)
        plt.title('{} \nCluster {}'.format(i,j))
    plt.show()
#PRINCIPAL COMPONENT ANALYSIS(PCA)
#Creates a 2d outline from a 3d distribution of data and distributes data in terms of components

# Create a dataframe with the two components
pca_df = pd.DataFrame(data = principal_comp, columns =['pca1','pca2'])
pca_df.head()

pca_df = pd.concat([pca_df,pd.DataFrame({'cluster':labels})], axis = 1)
pca_df.head()

plt.figure(figsize=(10,10))
ax = sns.scatterplot(x="pca1", y="pca2", hue = "cluster", data = pca_df, palette =['red','green','blue','pink','yellow','gray','purple', 'black'])
plt.show()
#Number of colours need to be as many as there are clusters
