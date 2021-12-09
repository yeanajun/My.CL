import pymongo
import bson
import os, json

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
#title 제목으로 searching 시 _id값 하나 반환
def searching_id(key_name, value_name, site_name):
    lecture_id_list = []
    mycol = connect_lecture_db().get_collection(site_name)
    for di in mycol.find({}, {key_name: 1}):
        if di.get(key_name) == value_name:
            if key_name == "title":
                lecture_id = di.get("_id")
                return lecture_id
            else:
                lecture_id_list.append(di.get("_id"))

    return lecture_id_list


#과목, 학년으로 뽑아낸 list 교집합 ->lecture_id_list
#list2개 교집합 list형태로 반환
def list_intersection(list1, list2):
    li = list(set(list1).intersection(list2))
    return li


#tag값 update
def update_tag_data(lecture_id, tag_name, tag_data):
    column_name = '_id'
    mycol = connect_lecture_db().get_collection(tag_name)
    for di in mycol.find({}, {column_name: 1, tag_data: 1}):
        temp = di.get(tag_data) + 1
        if di.get(column_name) == lecture_id:  # lecture에서 찾은 id값과 tag_ ***의 id값 일치 --> 태그값 +1 후에 수정
            mycol.update_one({"_id": bson.ObjectId(lecture_id)}, {"$set": {tag_data: temp}})

#update_tag_data(lecture_id, "tag_jindo", "medium")


#_id와 tag_data값으로 dict만들기
def data_make_dict(lecture_id_list, tag_name, tag_data):
    id_list = []
    tag_value = []
    mycol = connect_lecture_db().get_collection(tag_name)
    for di in mycol.find({}, {tag_data: 1}):
        for i in range(len(lecture_id_list)):
            if di.get("_id") == lecture_id_list[i]:
                id_list.append(di.get("_id"))
                tag_value.append(di.get(tag_data))
    dic = dict(zip(id_list, tag_value))
    return dic

#dict에서 특정한 수의 max값 추출 하여 list로 반환
def max_filtering(dic_length, dic):
    max_id_data = []
    cnt = 0
    while(cnt < dic_length*9/10):
        if dic_length <= 5:
            return list(dic.keys())                     #5개 이하면 그대로 key값만 반환
        else:
            max_data = max(dic, key=dic.get)
            max_id_data.append(max_data)
            del dic[max_data]
            cnt += 1

    return max_id_data

#결과값 title을 list로 반환
def recommendation_res_title(res_list, tag_name):
    recom_list = []
    mycol = connect_lecture_db().get_collection(tag_name)
    for i in range(len(res_list)):
        for di in mycol.find({}, {"title": 1}):
            if di.get("_id") == res_list[i]:
                recom_list.append(di.get("title"))
    return recom_list


#문자열 부분 사이트에서 데이터 받아와야 함
lecture_id_list1 = searching_id("subject", "국어","data_megastudy")
lecture_id_list2 = searching_id("grade", "고3·N수", "data_megastudy")
intersection_id_list = list_intersection(lecture_id_list1, lecture_id_list2)
dic = data_make_dict(intersection_id_list, "tag_jindo", "low")
dic2 = data_make_dict(max_filtering(len(dic),dic), "tag_jobdam", "low")
dic3 = data_make_dict(max_filtering(len(dic2),dic2), "tag_pilgi", "high")
dic4 = data_make_dict(max_filtering(len(dic3),dic3), "tag_achivement", "onetotwo")
reslist = max_filtering(len(dic4), dic4)
rec_res_list = recommendation_res_title(reslist, "data_megastudy")
#print(dic)
#print(len(dic))
#print(dic2)
#print(len(dic2))
#print(dic3)
#print(len(dic3))
# print(reslist)
# print(len(reslist))
# print(recommendation_res_title(reslist, "data_megastudy"))