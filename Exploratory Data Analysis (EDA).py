# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('superstore_sales.csv')

# Step 2: Data Cleaning
print("Initial Dataset Overview:")
print(df.info())  # Check data types and missing values

# Handle missing values
df.dropna(inplace=True)

# Step 3: Basic Statistics
print("\nSummary Statistics:")
print(df.describe())  # Display summary statistics for numeric columns

# Step 4: Exploratory Data Analysis
# 4.1 Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Sales:")
print(top_products)

# 4.2 Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(sales_by_region)

# Step 5: Data Visualization
plt.figure(figsize=(10, 6))

# Bar plot for Top 10 Products by Sales
plt.subplot(1, 2, 1)
sns.barplot(x=top_products.values, y=top_products.index, palette='Blues_d')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')

# Pie chart for Sales by Region
plt.subplot(1, 2, 2)
sales_by_region.plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set3'))
plt.title('Sales Distribution by Region')

plt.tight_layout()
plt.show()

# Step 6: Correlation Analysis
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()