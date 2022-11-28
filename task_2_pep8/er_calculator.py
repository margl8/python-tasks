#!/usr/bin/python3
# -*- coding: utf-8 -*-

#опредеяем тип er и выводим результат
#     #вычисляем 2 типа ER
def er_per_post(likes, comments, reposts, subscribers):
    return float((likes + comments + reposts) / subscribers)

def er_per_reach(likes, comments, reposts, views):
    return float((likes + comments + reposts) / views)
  
if __name__ == '__main__':
    likes = int(input('Введите число лайков'))
    comments = int(input('Введите число комментариев'))
    reposts = int(input('Введите число репостов'))
    subscribers = int(input('Введите число подписчиков'))
    views = int(input('Введите число основного охвата'))
    
    print('Введите нужный тип для вычисления: ER/ERR')
    er_type = input().lower()
    
    if er_type == "er":
        print(f"{er_per_post(likes, comments, reposts, subscribers):.1%}")
    elif  er_type == "err":
        print(f"{er_per_reach(likes, comments, reposts, views):.1%}")
    else:
        print('error')