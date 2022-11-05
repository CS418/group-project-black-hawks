import pandas as pd
import matplotlib.pyplot as plt

airbnb_listings = pd.read_csv("listings.csv")
airbnb_listings.head(5)
airbnb_listings.info()
airbnb_listings.shape
airbnb_listings.describe()
airbnb_reviews = pd.read_csv("reviews.csv")
airbnb_reviews.head(5)
airbnb_reviews.info()
airbnb_reviews.shape
airbnb_reviews.describe()
airbnb_calendar = pd.read_csv("calendar.csv")
airbnb_calendar.head(5)
airbnb_calendar.info()
airbnb_calendar.shape
airbnb_calendar.describe()
null = airbnb_listings.isna().sum()
null.sort_values(ascending=False)
airbnb_listings.columns
null = airbnb_reviews.isna().sum()
null.sort_values(ascending=False)
airbnb_reviews.columns
null = airbnb_calendar.isna().sum()
null.sort_values(ascending=False)
airbnb_calendar.columns
# Data cleaning
airbnb_listings.isna().sum().sort_values(ascending=False)
def dropping_column(data, col_name): 
    new_data = data.drop(col_name, axis=1)
    print('Dropping {}...'.format(col_name))
    return new_data
airbnb_listings_clean = dropping_column(airbnb_listings, 'host_verifications') 
for col_name in airbnb_listings_clean.columns:
    if 'id' in col_name:
        airbnb_listings_clean=dropping_column(airbnb_listings_clean, col_name)
    if 'url' in col_name:
        airbnb_listings_clean=dropping_column(airbnb_listings_clean, col_name)
    if 'name' in col_name:
        airbnb_listings_clean=dropping_column(airbnb_listings_clean, col_name)
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'host_listings_count')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'host_total_listings_count')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'description')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'neighborhood_overview')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'host_about')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'neighbourhood')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'latitude')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'longitude')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'host_location')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'host_neighbourhood') 
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'license')
airbnb_listings_clean = dropping_column(airbnb_listings_clean,'last_scraped')
airbnb_listings_clean = airbnb_listings_clean.loc[:,~airbnb_listings_clean.T.duplicated(keep='first')]
airbnb_listings_clean.drop_duplicates()
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'availability_30')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'availability_60')
airbnb_listings_clean = dropping_column(airbnb_listings_clean, 'availability_90')
for column_name in airbnb_listings_clean.columns:
    if len(airbnb_listings_clean[column_name].value_counts()) <= 1:
        airbnb_listings_clean = dropping_column(airbnb_listings_clean, column_name)
for col_name in airbnb_listings_clean.columns:
    if 'review' in col_name:
        airbnb_listings_clean = dropping_column(airbnb_listings_clean, col_name)
airbnb_listings_clean.hist(figsize=(20,20));
null_values_percentage = airbnb_listings_clean.isnull().sum().sort_values(ascending=False) / len(airbnb_listings_clean)
x = range(len(null_values_percentage[null_values_percentage != 0]))
y = null_values_percentage[null_values_percentage != 0]

plt.figure(figsize=(10,20))
ax = plt.subplot()

plt.gca().invert_yaxis()
ax.set_yticks(range(len(null_values_percentage)))
ax.set_yticklabels(null_values_percentage.index)

plt.barh(x, y, color='y')
plt.show()
airbnb_listings_clean['Missing_num'] = airbnb_listings_clean.isnull().sum(axis=1)
print('{:.2f}% rows have no missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']==0]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 1 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=1]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 2 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=2]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 3 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=3]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 4 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=4]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 5 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=5]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 6 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=6]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 7 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=7]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 8 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=8]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 9 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=9]) / len(airbnb_listings_clean) * 100))
print('{:.2f}% rows have less than 10 missing data.'.format(len(airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=10]) / len(airbnb_listings_clean) * 100))
plt.figure(figsize=(16,8))
plt.xticks(range(50))
airbnb_listings_clean['Missing_num'].plot.hist(color='b', alpha=0.5, bins=50)
plt.show()
missing_threshold = 4
airbnb_listings_clean.shape
airbnb_listings_clean = airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=missing_threshold].drop('Missing_num', axis = 1)
airbnb_listings_clean.shape
missing_threshold = 4
airbnb_listings_clean = airbnb_listings_clean[airbnb_listings_clean['Missing_num']<=missing_threshold].drop('Missing_num', axis = 1)
airbnb_listings_clean.shape
airbnb_listings_clean.isnull().sum().sum()
airbnb_listings_clean.isnull().sum()
airbnb_listings_clean.info()
airbnb_listings_clean['host_response_rate'] = airbnb_listings_clean['host_response_rate'].map(lambda rate: np.float(rate[:-1]) / 100, na_action='ignore')
airbnb_listings_clean['host_acceptance_rate'] = airbnb_listings_clean['host_acceptance_rate'].map(lambda rate: np.float(rate[:-1]) / 100, na_action='ignore')
airbnb_listings_clean['host_response_rate'].fillna(airbnb_listings_clean['host_response_rate'].median(), inplace=True)
airbnb_listings_clean['bedrooms'].fillna(airbnb_listings_clean['bedrooms'].median(), inplace=True)
airbnb_listings_clean['beds'].fillna(airbnb_listings_clean['beds'].median(), inplace=True)
airbnb_listings_clean['host_acceptance_rate'].fillna(airbnb_listings_clean['host_acceptance_rate'].median(), inplace=True)
airbnb_listings_clean.isnull().sum()
airbnb_listings_clean.isnull().sum()
def oneHot(feat, data):
    print('Ecoding {} as one-hot..'.format(feat))
    cur_dummies = pd.get_dummies(data[feat], prefix=feat)
    data.drop(feat, axis=1, inplace=True)
    data = pd.concat([data, cur_dummies], axis=1)
    return data
features = []
conts = []
for col_name in airbnb_listings_clean.columns:
    if airbnb_listings_clean[col_name].dtype == np.float:
        print('{} is a continous varibale'.format(col_name))
        # 
        conts.append(col_name)
    elif len(airbnb_listings_clean[col_name].value_counts()) <= 5:
        data_clean = oneHot(col_name, airbnb_listings_clean)
    else:
        features.append(col_name)
print(conts)
print(features)
airbnb_listings_clean['host_since'].head()
airbnb_listings_clean['host_since'] = airbnb_listings_clean['host_since'].map(lambda date: 2022- int(date[-4:]), na_action='ignore')
airbnb_listings_clean['host_since'].value_counts()
airbnb_listings_clean = oneHot('host_since', airbnb_listings_clean)
airbnb_listings_clean['neighbourhood_cleansed'].value_counts()
airbnb_listings_clean = oneHot('neighbourhood_cleansed', airbnb_listings_clean)
airbnb_listings_clean['property_type'].value_counts()
airbnb_listings_clean = oneHot('property_type', airbnb_listings_clean)
airbnb_listings_clean['accommodates'].value_counts()
airbnb_listings_clean = oneHot('accommodates', airbnb_listings_clean)
airbnb_listings_clean['amenities'][0]
amenities_list = list(data_clean.amenities)
amenities_list_string = " ".join(amenities_list)
amenities_list_string = amenities_list_string.replace('{', '')
amenities_list_string = amenities_list_string.replace('}', ',')
amenities_list_string = amenities_list_string.replace('[', '')
amenities_list_string = amenities_list_string.replace(']', ',')
amenities_list_string = amenities_list_string.replace('"', '')
amenities_list_string = amenities_list_string.replace("'", "")
amenities_set = [x.strip() for x in amenities_list_string.split(',')]
amenities_set
mydict = {}
for word in amenities_set:
    if word in mydict:
        mydict[word] += 1
    else:
        mydict[word] = 1       
print(mydict)
threshold = 500
A = {k:v for (k,v) in mydict.items() if v > threshold }
A = list(A.keys())

for a in A:
    airbnb_listings_clean[a] = airbnb_listings_clean['amenities'].apply(lambda A: 1 if a in A else 0)
airbnb_listings_clean = airbnb_listings_clean.drop(['amenities'],axis=1)
airbnb_listings_clean.describe()
airbnb_reviews.isna().sum().sort_values(ascending=False)
airbnb_calendar.isna().sum().sort_values(ascending=False)
