import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import sys
import json
from matplotlib import pyplot as plt
from urllib.request import urlretrieve
import requests

page = 100

link = f'https://server.solatioenergialivre.com.br/Customers?page={page}'

parametros = {'Authorization':'Bearer cea967db-1da2-4762-856b-147999094816'}

requests = requests.get(link, headers=parametros)

print(requests.json())




