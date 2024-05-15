import pandas as pd
import json

# data = pd.read_csv("demo_pjanbroad__custom_11371472_linear.csv")
# data = data.drop(columns=['DATAFLOW', "LAST UPDATE", "freq", "unit", "OBS_FLAG"])
# print(data.isna().sum())
# data = data.dropna()
# print(data.info())
# data.to_csv("data.csv", index=False)

data = pd.read_csv("data.csv")

years = data["TIME_PERIOD"].unique().tolist()
countries = data["geo"].unique().tolist()
ages = data["age"].unique().tolist()
sexes = data["sex"].unique().tolist()
years.sort()

jsonData = {}

for year in years:
    print(year)
    jsonData[year] = {}
    for country in countries:
        jsonData[year][country] = {}
        for age in ages:
            jsonData[year][country][age] = {}
            for sex in sexes:
                values = data[(data["age"] == age) & (data["geo"] == country) & (data["sex"] == sex) & (data["TIME_PERIOD"] == year)]["OBS_VALUE"].values
                if(values.size > 0):
                    jsonData[year][country][age][sex] = values[0]
                else:
                    jsonData[year][country][age][sex] = "N/A"


dumpedJson = json.dumps(jsonData)

file = open("data.json", "w")
file.write(dumpedJson)
file.close()