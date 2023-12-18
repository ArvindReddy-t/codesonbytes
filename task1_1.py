#1.	Create a csv dataset using python , pandas and any public api
import pandas as pd
import requests
url = 'https://disease.sh/v3/covid-19/countries'
response = requests.get(url)
data = response.json()
country_names = []
cases = []
deaths = []
recovered = []
active = []

for country_data in data:
    country_names.append(country_data['country'])
    cases.append(country_data['cases'])
    deaths.append(country_data['deaths'])
    recovered.append(country_data['recovered'])
    active.append(country_data['active'])

covid_data = {
    'Country': country_names,
    'Cases': cases,
    'Deaths': deaths,
    'Recovered': recovered,
    'Active': active
}

df = pd.DataFrame(covid_data)

df.to_csv('covid_data.csv', index=False)
print("CSV file 'covid_data.csv' has been created with COVID-19 data.")
dff = pd.read_csv('covid_data.csv')
print(dff)
