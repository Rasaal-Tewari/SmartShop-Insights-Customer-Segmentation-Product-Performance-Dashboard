#---------------------------------------------------------
# SmartShop Insights: Complete Customer Behavior Analysis
#---------------------------------------------------------


import kagglehub
import pandas as pd    # clean, process, and analyze the sales data
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Downloading Dataset
path = kagglehub.dataset_download("iamsouravbanerjee/customer-shopping-trends-dataset")

# Finding required file in folder
print("Files in dataset folder:", os.listdir(path))

# Creating the full path
file_path = os.path.join(path, "shopping_trends_updated.csv")

# Loading Dataset
df = pd.read_csv(file_path, encoding='utf-8')

# Viewing Details of the Dataset (Structure of Data)
df.info()

#----------------------------
# Customer Behavior Analysis
#----------------------------

#--------------------------
# Demographics Analysis
#--------------------------

sns.set_style("whitegrid")

# Gender Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.show()

# Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()

# Top Locations by Frequency
plt.figure(figsize=(10, 6))
sns.countplot(y='Location', data=df, order=df['Location'].value_counts().index[:10])
plt.title("Top 10 Locations by Number of Transactions")
plt.xlabel("Transaction Count")
plt.ylabel("Location")
plt.show()

#--------------------------------------
# Purchase Behavior Analysis
#--------------------------------------

# Spending per Customer
monetary = df.groupby('Customer ID')['Purchase Amount (USD)'].sum()
print("\nTop 5 Customers by Spending:")
print(monetary.sort_values(ascending=False).head())

# Frequency per Customer (current purchases + previous purchases)
df['Total Purchases'] = 1 + df['Previous Purchases']
total_frequency = df.groupby('Customer ID')['Total Purchases'].sum()

# Top 5 customers by total number of purchases
top_total_frequency = total_frequency.sort_values(ascending=False).head(5)
print("\nTop 5 Buyers by Total Number of Purchases (Current + Previous):")
for cid, total in top_total_frequency.items():
    print(f"Customer ID: {cid} | Total Number of Purchases: {total}")

#------------------------------
# Product Preferences
#------------------------------

# Top Categories
plt.figure(figsize=(10, 6))
sns.countplot(y='Category', data=df, order=df['Category'].value_counts().index[:10])
plt.title("Top 4 Product Categories")
plt.xlabel("Count")
plt.ylabel("Category")
plt.tight_layout()
plt.show()

# Top Items
plt.figure(figsize=(10, 6))
sns.countplot(y='Item Purchased', data=df, order=df['Item Purchased'].value_counts().index[:10])
plt.title("Top 10 Purchased Items")
plt.xlabel("Count")
plt.ylabel("Item")
plt.tight_layout()
plt.show()

#--------------------------------------
# Customer Loyalty Indicators
#--------------------------------------

# Previous Purchases Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Previous Purchases'], bins=15)
plt.title("Distribution of Previous Purchases")
plt.xlabel("Previous Purchases")
plt.show()

# Frequency Labels
plt.figure(figsize=(10, 6))
sns.countplot(y='Frequency of Purchases', data=df)
plt.title("Purchase Frequency Labels")
plt.xlabel("Count")
plt.ylabel("Frequency Category")
plt.show()

#------------------------------------
# Promotion Responsiveness
#------------------------------------

# Promo Code Usage
plt.figure(figsize=(10, 6))
sns.countplot(x='Promo Code Used', data=df)
plt.title("Promo Code Usage")
plt.show()

# Discount Applied
plt.figure(figsize=(10, 6))
sns.countplot(x='Discount Applied', data=df)
plt.title("Discount Applied")
plt.show()

# Subscription Status
plt.figure(figsize=(10, 6))
sns.countplot(x='Subscription Status', data=df)
plt.title("Subscription Status")
plt.show()

#-------------------------------------------------
# Customer Satisfaction (Review Ratings)
#-------------------------------------------------

plt.figure(figsize=(10, 6))
sns.histplot(df['Review Rating'], bins=10, kde=True)
plt.title("Customer Review Ratings Distribution")
plt.xlabel("Rating (out of 5)")
plt.show()