import pandas as pd
from collections import OrderedDict
import json
dataframe = pd.read_csv('ChineseID.csv')
businessIds = {
	'business_id': [], 
	}
for index, row in dataframe.iterrows():
		businessIds['business_id'].append(row['business_id'])
print (len(businessIds['business_id']))
print(businessIds)

with open('yelp_academic_dataset_review.json') as f:
	for line in f:
		j_content = json.loads(line)
		try:
			indexing = businessIds['business_id'].index(j_content['business_id']);	
			cats = businessIds['categories'][indexing];
			cats = cats.replace("[", "");
			cats = cats.replace("]", "");
			tokens = cats.split(',');
			for elem in tokens:
				elem = elem.strip();
				isFound = CategoriesAndCountsMap.get(elem);
				if isFound == None:
					CategoriesAndCountsMap[elem] = 1;
				else:
					CategoriesAndCountsMap[elem] = isFound + 1;
		except ValueError:
			pass
sortedCategoriesAndCountsMap = OrderedDict(sorted(CategoriesAndCountsMap.items(), key=lambda x: x[1]))
output = open('checkins_count_' + city + '.txt', 'w')
for k,v in sortedCategoriesAndCountsMap.items():
	output.write(k + ":" + str(v) + "\n")
output.close()
