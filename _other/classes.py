import requests as rq
import datetime
import pandas as pd

VERSION = 5.131
TOKEN = 'fcf784d2fcf784d2fcf784d206ffe7472fffcf7fcf784d29fdf12d1cff39e144bbbaa42'
TIME_NOW = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')


class VkGroup:
    group_id = None
    posts = []

    def __init__(self, group_id) -> None:
        self.group_id = group_id
        request = rq.get('https://api.vk.com/method/groups.getById',
                         params={
                             'access_token': TOKEN,
                             'v': VERSION,
                             'group_id': group_id,
                             'fields': 'members_count'
                         }).json().get('response', None)
        response = request[0]
        self.screen_name = response['screen_name']
        self.name = response['name']
        self.members = response['members_count']

    def __str__(self):
        return f'ID: {self.group_id}\n' \
               f'Domain: {self.screen_name}\n' \
               f'Name: {self.name}\n' \
               f'Members: {self.members}\n'

    def __repr__(self):
        return f'VkGroup(group_id={self.group_id}, ' \
               f'domain="{self.screen_name}", ' \
               f'name="{self.name}", ' \
               f'members={self.members})\n'

    def get_posts(self):
        count = int(input('count'))
        offset = int(input('offset'))
        request = rq.get("https://api.vk.com/method/wall.get",
                         params={
                             'access_token': TOKEN,
                             'v': VERSION,
                             'owner_id': -self.group_id,
                             'count': count,
                             'offset': offset
                         })
        response = request.json()['response']['items']
        self.posts.extend(response)
        return self.posts

    def get_report(self):
        self.posts = pd.DataFrame()
        return self.posts


group = VkGroup(1)
print(group.__str__())
print(group.__repr__())
group.get_posts()
print(group.get_report())
