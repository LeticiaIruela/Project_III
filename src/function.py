from pymongo import MongoClient
import pandas as pd
import time

def mongo(name, collection):
    client = MongoClient("localhost:27017")
    db=client["Ironhack"]
    c= db.get_collection("companies")
    return c

def mongo_query(c)
    condition_1 = {"total_money_raised": {"$regex": "[MB]$"}}
    condition_2 = {"category_code": {"$in": ["games_video"]}}
    condition_3 = {"$or": [{"tag_list": {"$regex": "design.|.tech.|.game"}},{"category_code": "games_video"},{"description": {"$regex": "game"}}]}
    query = {"$and": [condition_1, condition_2, condition_3]}
    projection = {"_id": 0, "name": 1, "offices": 1, "description": 1, "number_of_employees": 1, "total_money_raised": 1, "category_code": 1, "tag_list":1}
    selected_companies2 = list(c.find(query, projection))
    df=pd.DataFrame(selected_companies2)
    return df

def mongo_address(df):
    track = []
    for index, row in df2.iterrows():
        name = row['name']
        description=row['description']
        number_of_employees=row['number_of_employees']
        total_money_raised = row['total_money_raised']
        category_code = row['category_code']
        tag_list = row['tag_list']
        for office in row['offices']:
            x = {
                'name':name,
                'description':description,
                'number_of_employees':number_of_employees,
                'total_money_raised': total_money_raised,
                'category_code': category_code,
                'tag_list': tag_list,
                'description': office['description'],
                'address1': office['address1'],
                'address2': office['address2'],
                'zip_code': office['zip_code'],
                'city': office['city'],
                'state_code': office['state_code'],
                'country_code': office['country_code'],
                'latitude': office['latitude'],
                'longitude': office['longitude']
            }
            track.append(x)
    df = pd.DataFrame(track)
    return df

def cleaning_mongo(df):
    import numpy as np
    df['city'].replace('',np.nan,inplace=True)
    df.dropna(subset=["city"], inplace=True)
    df.to_csv('./data/df3.csv')
    return df


