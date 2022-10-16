#!/usr/bin/python3
# -*- coding: utf-8 -*-

# вводим глобальные переменные для вычисления er, все переменные - целые числа 
likes = int(input('Введите число лайков'))
comments = int(input('Введите число комментариев'))
reposts = int(input('Введите число репостов'))
subscribers = int(input('Введите число подписчиков'))
views = int(input('Введите число основного охвата'))

#вычисляем 2 типа ER
def er_per_post():
    (likes + comments + reposts) / subscribers

def er_per_reach():
    (likes + comments + reposts) / views

#опредеяем тип er и выводим результат
def er_result():
    er_type = str(input('Вам нужно вычислить er или err? Введите нужный тип для вычисления: ER или ERR'))
    if er_type == "ER" or "er":
        print(f"{er_per_post():.1%}")
    elif  er_type == "ERR" or "err":
        print(f"{er_per_reach():.1%}")
    else:
        print('error')

def main():
    er_result()