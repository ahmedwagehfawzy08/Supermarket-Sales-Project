#Importing the pandas library
import pandas as pd
import numpy as np

#Check the version of the pandas and numpy libraries.
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

#Reading the data of the supermarket sales from the csv file

data = pd.read_csv("supermarket_sales_dataset.csv")

#Display the data and the details of it as (no. of rows, no. of columns, 
#memory usage, …, etc.).

print(data)
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
print("Memory usage:\n", data.info())

#Removing all the rows that have NaN data from the csv file and 
#display the updated data

data_cleaned = data.dropna()


#-----------------------------------------------------------------------------------------------
# Calculate the total cost for each quantity before the tax cost of 5% 
# and display the Invoice ID inside to the total cost that calculated.

# data_cleaned.loc[:, 'Total_Cost_Before_Tax'] = data_cleaned['Total'] / 1.05
# data_cleaned.loc[:, 'Total_Cost_Before_Tax'] = data_cleaned['Total_Cost_Before_Tax'].apply(lambda x: round(x, 1))
#total_cost_before_tax = []


# data_cleaned['Final_cost_Before_tax'] = data_cleaned['Total'] *5/100
# print(data_cleaned[['Invoice ID', 'Final_cost_Before_tax']])

# for row in data_cleaned:
#     total_cost = float(row[10])
#     total_cost_before_tax.append([row[0], round(total_cost / 1.05, 1)])

#-----------------------------------------------------------------------------------------------
#Display all the supermarkets that found in A and C branches

desired_branches = ["A", "C"]
desired_rows = data[data["Branch"].isin(desired_branches)]
print("Invoices for Branches A and C:")
print(desired_rows["Invoice ID"].tolist())


#Computing the maximum and the minimum cost of the Total column

max_total = data_cleaned['Total'].max()
min_total = data_cleaned['Total'].min()
print("Maximum Total cost:", max_total)
print("Minimum Total cost:", min_total)

#Display the number of Product line that has the value of: - Electronic accessories. Sports and travel. Health and beauty. Home and lifestyle. Food and beverages. Fashion accessories

product_lines = ['Electronic accessories', 'Sports and travel', 'Health and beauty', 'Home and lifestyle', 'Food and beverages', 'Fashion accessories']
for line in product_lines:
    count = data_cleaned[data_cleaned['Product line'] == line].shape[0]
    print("Number of", line, "products:", count)

#- Replacing all Female and Male with F and M

for i in data.index:
    if data.loc[i,"Gender"]=="Female":
        data.loc[i,"Gender"]="F"
    elif data.loc[i,"Gender"]=="Male":
        data.loc[i,"Gender"]="M"    
print(data.to_string())

#data_cleaned['Gender'] = data_cleaned['Gender'].replace({'Female': 'F', 'Male': 'M'})
#-------------
#Counting and display the Invoice ID for all purchases that the  customers are payed with: - o Ewallet o Casho Credit card

payment_counts = data_cleaned['Payment'].value_counts()
print("Payment method counts:\n", payment_counts)


#Calculating the final cost of all purchases after 5% tax in the Total Column.

data_cleaned['Final_cost_after_tax'] = data_cleaned['Total'] /1.05
print(data_cleaned[['Invoice ID', 'Final_cost_after_tax']])

#Computing and display the quantity (number of purchases) that are sold from the three branches A, B and C, in addition to the final cost achieved by each branch.


branch_stats = {}
for index, row in data_cleaned.iterrows():
    branch = row['Branch']
    quantity = row['Quantity']
    cost = row['Final_cost_after_tax']

    if branch in branch_stats:
        branch_stats[branch]['Quantity'] += quantity
        branch_stats[branch]['Final_cost_after_tax'] += cost
    else:
        branch_stats[branch] = {'Quantity': quantity, 'Final_cost_after_tax': cost}

print("Branch statistics:")
for branch, stats in branch_stats.items():
    print("Branch:", branch)
    print("Quantity:", stats['Quantity'])
    print("Final_cost_after_tax:", stats['Final_cost_after_tax'])

#Displaying the number of customers recorded by Member for customers using member card and Normal for without member card.
customer_counts = data_cleaned['Customer type'].value_counts()
print("Customer type counts:\n", customer_counts)


#---------------------------------------------------


#Creating a function called added_Tax_Fun() to calculate the added tax percentage that equals 3% to the Total column then display the final cost of bill.


def added_Tax_Fun(total):
    added_tax_percentage = 0.03
    final_cost = total * (1 + added_tax_percentage)
    return final_cost

data_cleaned['Final_cost_with_added_tax'] = data_cleaned['Total'].apply(added_Tax_Fun)
print(data_cleaned[['Invoice ID', 'Final_cost_with_added_tax']])

#Converting the data to a numerical data using the library that do it

data_numerical = data_cleaned.apply(pd.to_numeric, errors='ignore')
print(data_numerical.info())

