import pymongo
import bson
import os, json

#수기로 입력한 수업title, 수업site, tag_data를 사이트에서 받아와야 함
#사이트 데이터 받아오는 부분 -> 추천 해준 페이지 즉, 추천 이후의 태그 데이터 추가 과정의 코드
# def connect_site():
#     return title, tag_data

#mongoDB서버 연동
def connect_lecture_db():
    secret_file = os.path.join("../client", 'secrets.json')
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    mongodb_uri = "mongodb+srv://mycl:{}@lecture.ks2gr.mongodb.net/mycl?retryWrites=true&w=majority".format(secrets['MONGO_PW'])
    myclient = pymongo.MongoClient(mongodb_uri)
    mydb = myclient.get_database("lecture")
    return mydb


#_id값 찾기 -> connect_lecture_db()와 연결 되어있음
def searching_id(title_name, site_name):
    lecture_id = ""
    column_name = "title"
    mycol = connect_lecture_db().get_collection(site_name)
    for dict in mycol.find({}, {column_name: 1}):
        if dict.get(column_name) == title_name:
            lecture_id = dict.get("_id")

    return(lecture_id)

lecture_id = searching_id("2022 우리들의 기출 분석","data_megastudy")
temp = 0

#tag_data 업데이트
def update_tag_data(lecture_id, tag_name, tag_data):
    column_name = '_id'
    mycol = connect_lecture_db().get_collection(tag_name)
    for dict in mycol.find({}, {column_name: 1, tag_data: 1}):
        temp = dict.get(tag_data) + 1
        if dict.get(column_name) == lecture_id:  # lecture에서 찾은 id값과 tag_ ***의 id값 일치 --> 태그값 수정
            mycol.update_one({"_id": bson.ObjectId(lecture_id)}, {"$set": {tag_data: temp}})
            print(dict)

#update_tag_data(lecture_id, "tag_jindo", "medium")

#_id와 tag_data값으로 dict만들기
def data_make_dict(tag_name, tag_data): #tag_name = "tag_jindo" tag_data = "low"
    id_list = []
    tag_value = []
    mycol = connect_lecture_db().get_collection(tag_name)
    for di in mycol.find({}, {tag_data: 1}):
        id_list.append(di.get("_id"))
        tag_value.append(di.get(tag_data))
    dic = dict(zip(id_list, tag_value))
    return dic

#dic = data_make_dict("tag_jindo", "low")