from function_token_PAL21 import *
from datetime import date
import requests
import pandas as pd
import json
import math
import config

url = config.url
datum = str(date.today())

header = token()

query = '''
query files{
  allFiles(where:{createdAt:{lteq:"''' + datum + '''T00:00:00+02:00"}} take:200 sort:{field:createdAt order:DESC}){
    results{
      createdAt
      createdAtDay
      fileLink
      id
      typeFile
      updatedAt
      file{
        name
        url
      }
      multifiles{
        name
        url
      }
      multiImages{
        name
        url
        resized{
          name
        	url
          size{
            width
            height
          }
        }
      }
    }
  }
}
'''
response = requests.post(url, json={'query': query}, headers=header)
allFiles = pd.json_normalize(
    response.json()['data']['allFiles']['results']
)
allFiles.to_csv('allFiles.csv', sep=',', index=False, encoding='utf-8')
