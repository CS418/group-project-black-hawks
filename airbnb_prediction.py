import pandas as pd
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
