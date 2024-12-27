import pandas as pd
import numpy as nm
path="D:\\215179\\z\\medical_students_dataset.csv"

print("Pandas version:", pd.__version__)


data = pd.read_csv(path)


print( data.info())


data = data.dropna()

print(" data after removing NaN rows:")
print(data)

Student_ID=215000
def update_id(row):
    global Student_ID
    Student_ID+=1
    return Student_ID
data['Student ID']=data.apply(update_id,axis=1)
print(data)


data.loc[data["Smoking"] == "Yes", "Smoking"] = "Yes, Their lungs will damage"


gender_counts = data["Gender"].value_counts()
print(gender_counts)


age_ranges = [(10, 20), (21, 30), (31, 40), (41, float("inf"))]
for age_range in age_ranges:
    condition = (data["Age"] >= age_range[0]) & (data["Age"] <= age_range[1])
    count = len(data.loc[condition])
    print(f"Number of students between {age_range[0]} and {age_range[1]} years old:", count)


data["Height"] = round(data["Height"], 2)
data["Weight"] = round(data["Weight"], 2)


blood_counts = data["Blood Type"].value_counts()
print(blood_counts)

data.loc[data['Diabetes']=="Yes","Diabetes"]=" Has a Good Health and Must be cured"


def suitable_Fun(height, weight):
    if abs(height - weight) == 10:
        return "Suitable"
    else:
        return "Not Suitable"


data["Suitability"] = data.apply(lambda row: suitable_Fun(row["Height"], row["Weight"]), axis=1)


print("Data with suitability:")
print(data)