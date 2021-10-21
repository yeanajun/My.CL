import json
import os.path
import pandas as pd

file_list = []
#json 파일 로딩 부분
def file_loading():
    json_file = os.listdir("C:\workspace\SanhakProject\data")
    #for i in range(len(json_file)):                #경로내의 데이터 수만큼 반복
    #for i in range(0, 1):
    file_list.append(json_file[0])
    return tuple(file_exist(json_file[0]))


# json파일 존재여부 확인 참일시 데이터 open
def file_exist(file):
    tech_title_list = []
    if os.path.isfile('data/' + file):
        with open('data/' + file) as f:
            crawling_data = json.load(f)
            teacher_list = teacher_searching(crawling_data)
            for i in range(len(teacher_list)):
                tech_title_list.append({teacher_list[i]: title_searching(crawling_data, teacher_list[i])})
        with open('data/test2.json','w') as f:
            json.dump(tech_title_list, f)
        return tech_title_list


#json 파일내에서 title부분 추출
def title_searching(file, teacher_index):
    title_list = []
    title_dict = {}
    for i in range(len(file)):
        if file[i]["teacher"] == teacher_index:
            title_dict[i] = {char_convertion(file[i]["title"]): {}}
            title_list.append(title_dict[i])
    return title_list


#json 파일내에서 teacher 부분 추출 후 tuple(set())으로 변환 return
def teacher_searching(file):
    teacher_list = []
    for i in range(len(file)):
        teacher_list.append(char_convertion(file[i]["teacher"]))
    teacher_list = tuple(set(teacher_list))
    return teacher_list


def char_convertion(str):
    str = str.replace("[", "(").replace("]", ")").replace(".","")
    return str


def recursion_key(file, key_dict):
    for key in key_dict:
        dict_store = file[key]
        if type(dict_store) != dict:
            pass
        else:
            print(key)
            recursion_key(dict_store, dict_store.keys())


def file_name_split(file):
    for i in range(len(file)):
        print(file[i].split('_'))


def file_saving(file_name, f_list):
    with open('data/'+file_name, 'w') as f:
        json.dump(f_list, f)




