# -*- coding: utf-8 -*-


import project_scraper as ps
import pandas as pd

path = "C:/Users/hp/Desktop/ds_salary_project/chromedriver"

df = ps.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
