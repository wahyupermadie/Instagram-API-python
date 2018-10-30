from InstagramAPI import InstagramAPI 
from getpass import getpass
from random import randint
import time

api = InstagramAPI(
        raw_input('username: '),
        getpass('password: ')
)

api.login()

TARGET = {
    'username': '',
    'media': '',
    'media_like': [],
}

TARGET['username'] = raw_input('username target: ')

api.searchUsername(TARGET['username'])

TARGET['user_data'] = api.LastJson['user']

print('Okay! i want check {0} post.\n'.format(
    TARGET['username']
))

api.getUserFeed(TARGET['user_data']['pk'])

media = TARGET['media'] = api.LastJson['items']

print('Total Post @{0}: {1} post.'.format(
    TARGET['username'],
    len(TARGET['media'])
))


for item in media:
    if item['has_liked']:
        print('This media has liked')
    else:
        hasLiked = api.like(item['id'])
        if hasLiked:
            print('Success for like this media')
            TARGET['media_like'].append(item['id'])
            time.sleep(randint(100,150))
