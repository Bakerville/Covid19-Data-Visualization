import string
import requests
import requests_cache
from requests_cache import CachedSession
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
import re
import pandas as pd
from datetime import datetime, timedelta
from requests_html import HTMLSession

index = []
country = []
total_cases = []
new_cases = []
total_deaths = []
new_deaths = []
total_recovered = []
new_recovered = []
active_cases = []
serious = []
tot_cases_per_pop = []
death_per_pop = []
total_test = []
tests_per_pop = []
population = []
region = []

url = "https://www.worldometers.info/coronavirus/#nav-yesterday"
driver = webdriver.Chrome()


driver.get(url)

table = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[6]/div[3]/div/table")

soup = BeautifulSoup(driver.page_source, "html.parser")
odd_class = soup.find_all('tr', class_='odd')

for i in odd_class:
    att = i.find_all('td')
    if len(att)!=16:
        continue
    else:
        if att[0].text == '' or att[1].text == '':
            continue
        else:
            for j in range(16):
                if (j==0):
                    index.append(att[j].text)
                elif(j==1):
                    country.append(att[j].text)
                elif(j==2):
                    total_cases.append(att[j].text)
                elif(j==3):
                    new_cases.append(att[j].text)
                elif(j==4):
                    total_deaths.append(att[j].text)
                elif(j==5):
                    new_deaths.append(att[j].text)
                elif(j==6):
                    total_recovered.append(att[j].text)
                elif(j==7):
                    new_recovered.append(att[j].text)
                elif(j==8):
                    active_cases.append(att[j].text)
                elif(j==9):
                    serious.append(att[j].text)
                elif(j==10):
                    tot_cases_per_pop.append(att[j].text)
                elif(j==11):
                    death_per_pop.append(att[j].text)
                elif(j==12):
                    total_test.append(att[j].text)
                elif(j==13):
                    tests_per_pop.append(att[j].text)
                elif(j == 14):
                    population.append(att[j].text)
                elif(j == 15):
                    region.append(att[j].text)

data ={'Country': country, 'Total Cases': total_cases , 'New Cases': new_cases,
      "Total Deaths": total_deaths, "New Deaths": new_deaths, "Total Recovered": total_recovered,
      "New Recovered": new_recovered, "Active Cases": active_cases, "Serious": serious,
      "Total Cases/1M pop": tot_cases_per_pop, "Death/1M pop": death_per_pop,"Total tests":total_test,
      "Tests/ 1M pop": tests_per_pop, "Population":population, "Region": region}

df = pd.DataFrame(data)

filename = str(datetime.now())[0:11]+"_covid19"+".csv"

df.to_csv(filename)