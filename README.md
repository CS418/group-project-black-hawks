## Table of Contents
1. [Dataset Overview](#dataset)
2. [Author(s)](#author)
3. [Dataset Description](#description)

# Project Overview

Airbnb is one of the most popular ways to find a place to stay in most major cities around the world. It has significantly altered the traditional method of locating accommodations for both short and long-term stays. we'd like to focus on the following issues that have been raised:

• What is the seasonal pattern of Airbnb in Chicago?
• What kinds of Airbnb homes are popular?
• What are the most influential features about the rental price?

This project's results will assist businesses in narrowing their target marketing customer base to the most likely prospective customers, and it will also assist businesses in understanding how various attributes influence the client's decision to accept or reject the Airbnb home.

# Author(s)

1. Mysari Srinikethan
2. Hemanth Pokala
3. Muhammed Adeem Shaik


# Dataset description

Airbnb does not release any data on the listings in its marketplace, but a separate group named Inside Airbnb scrapes 
and compiles publicly available information about many cities Airbnb's listings from the Airbnb website. For this project, 
their data set scraped on September 14, 2022, on the city of Chicago, Illinois is used. It contains information on all Chicago 
Airbnb listings that were live on the site on that date (over 7,400). 
The dataset is publicly available and link to the dataset is: http://insideairbnb.com/get-the-data/
The data has certain limitations. Most noticeable one is that it scrapes the advertised price rather than the actual price paid by 
the previous customer. There are also missing values in many fields w hich needed to be cleaned based on their importance.
From the downloaded dataset we would like to use the following csv datasets.
1) Calender.csv
- I t contains 10,48,575 row s w ith 7 columns.
2) Listings.csv
- I t contains 7,414 row s w ith 75 columns.
3) Review s.csv
- I t contains 3,43,394 row s w ith 6 columns.

Some of the more important features this project will look into the following: accommodates, bedrooms, bathrooms, beds, price, 
minimum_nights, maximum_nights and number_of_reviews
