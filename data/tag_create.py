from pymongo import MongoClient
import random

conn = MongoClient("mongodb+srv://mycl:0102@lecture.ks2gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = conn["lecture"]

for tag in ['tag_jobdam', 'tag_pilgi', 'tag_jindo']:
  tag_table = db[tag]

  for brand in ['data_ebsi', 'data_etoos', 'data_megastudy']:

    brand_table = db[brand]

    cls = brand_table.find()

    for x in cls:

      # 각 태그 count 랜덤 값
      low = random.randrange(0, 101)
      medium = random.randrange(0, 101)
      high = random.randrange(0, 101)

      tag_table.insert_one({'_id': x['_id'], 'low': low, 'medium': medium, 'high': high})