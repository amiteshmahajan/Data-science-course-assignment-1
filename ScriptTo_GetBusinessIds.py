import json
import pandas as pd
import string
Dt =	{
		'business_id': [], 
		'name': [],
		'city': [],
		'stars': [],
		'review_count': [],
		'categories': [],
		'latitude': [],
		'longitude': [],
		}
with open('yelp_academic_dataset_business.json') as f:
	for data in f:
		j_content = json.loads(data)
		categoriesArray = str(j_content['categories'])
		if categoriesArray.find("Chinese"):
			if j_content['city'] == 'Charlotte' or j_content['city'] == 'Pittsburgh':
				if categoriesArray.find('Restaurants') != -1:
					print(j_content['city'])
					Dt['business_id'].append(j_content['business_id'])
					Dt['name'].append(j_content['name'])
					Dt['city'].append(j_content['city'])
df = pd.DataFrame(Dt)
df.to_csv('businessIds.csv',sep =',',encoding = 'utf-8')