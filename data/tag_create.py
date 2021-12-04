from pymongo import MongoClient
import random
import os, json

secret_file = os.path.join("../client", 'secrets.json')
with open(secret_file) as f:
  secrets = json.loads(f.read())

conn = MongoClient("mongodb+srv://mycl:{}@lecture.ks2gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(secrets['MONGO_PW']))

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

tag_table = db['tag_achivement']

for brand in ['data_ebsi', 'data_etoos', 'data_megastudy']:

  brand_table = db[brand]

  cls = brand_table.find()

  for x in cls:

    # 각 태그 count 랜덤 값
    onetotwo = random.randrange(0, 101)
    threetofour = random.randrange(0, 101)
    fivetosix = random.randrange(0, 101)
    seventonine = random.randrange(0,101)

    tag_table.insert_one({'_id': x['_id'], 'onetotwo': onetotwo, 'threetofour': threetofour, 'fivetosix': fivetosix, 'seventonine': seventonine})