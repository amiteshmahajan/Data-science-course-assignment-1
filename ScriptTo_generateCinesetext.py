import json
import pandas as pd
dataframe = pd.read_csv('ChineseID.csv')
businessIds= []
for index, row in dataframe.iterrows():
		businessIds.append(row['business_id'])
review = open('yelp_academic_dataset_review.json')
review_text = []
for r in review:
	rj = json.loads(r)
	if rj['business_id'] in businessIds:
			review_text.append(rj['text'])
print(review_text)  