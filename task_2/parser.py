#!/usr/bin/python3
# -*- coding: utf-8 -*-

#импорты
import requests

#глобальные переменные: аутентификция
token = "fcf784d2fcf784d2fcf784d206ffe7472fffcf7fcf784d29fdf12d1cff39e144bbbaa42"
version = 5.131
domain = "welltex_perm"
response = requests.get ("https://api.vk.com/method/wall.get", 
params={
'access_token': token,
'v': version,
'domain': domain
} 
)
