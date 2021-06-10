import requests
from imgurpython import ImgurClient
from secrets import client_id, client_secret, access_token, refresh_token

client = ImgurClient(client_id, client_secret, access_token, refresh_token)

# Extracts the items (images) on the front page of Imgur:
items = client.gallery(section='hot', sort='viral', page=2, window='week', show_viral=False)
for item in items:
    print(item.link)
    # print(item.title)
    # print(items)
    # jinja for loop to iterate through each one to make a card

# Find the image on the front page that has the highest number of views 
# items = client.gallery()
# max_item = None
# max_views = 0
# for item in items:
#     if item.views > max_views:
#         max_item = item
#         max_views = item.views
# print(max_item.title)
# print(max_views)






# url = "https://api.imgur.com/3/album/300"

# headers = {'Authorization': 'Bearer 3af336150a146a8d15fb0f2717ae78a26a2793fe', 'Content-type': 'application/json'}

# response = requests.request("GET", url, headers=headers)

# print(response)


# from os import path
# from imgur_python import Imgur

# from flask import Flask
# from models import connect_db

# app = Flask(__name__)
# connect_db(app)

# API_BASE_URL ="https://api.imgur.com/3"

# imgur_client = Imgur({'client_id': '9b315a3d4a73278'})


# @app.route('{API_BASE_URL}/gallery/search', 
#                                 params={'q': 'cats'})
# def user_search():
#     """User search queries."""


# @app.route('{API_BASE_URL}/gallery/image', 
#                                 params={'title': 'cats'})
# def post_image():
#     """Post image to gallery."""


# from os import path
# from imgur_python import Imgur
# import requests

# # API_BASE_URL ="https://api.imgur.com/3"

# imgur_client = Imgur({'client_id': '9b315a3d4a73278'})
# image = imgur_client.image_upload(path.realpath('https://static8.depositphotos.com/1007254/986/i/950/depositphotos_9866977-stock-photo-flower-pots.jpg'), 'Untitled', 'My first image upload')
# image_id = image['response']['data']['id']
# album =  imgur_client.album_create([image_id], 'My first album', 'Something funny', 'public')
# album_id = album['response']['data']['id']
# response = imgur_client.gallery_album(album_id, 'This is going down on the sub', 0, 'funny,midly_interesting')
# print(response)











# # from imgurpython import ImgurClient

# # If you already have an access/refresh pair in hand
# client_id = '9b315a3d4a73278'
# client_secret = '6ea5304b64c0ce2d995277b3a125f752a059ca1c'
# refresh_token = 'f586b4ace231ec863edcf3e92c7cc54be6da54bd'

# # Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
# client = ImgurClient(client_id, client_secret, refresh_token)




# import configparser
# from imgurpython import ImgurClient

# config = configparser.ConfigParser()
# config.read('auth.ini')

# client_id = config.get('credentials', 'client_id')
# client_secret = config.get('credentials', 'client_secret')

# client = ImgurClient(client_id, client_secret)

# items = client.gallery(section='top', sort='time', page=3, window='week', show_viral=False)
# for item in items:
#     print(item.link)



# @app.route('{API_BASE_URL}/gallery/search', 
#                                 params={'sort': 'time', 'window': 'month', 'page': '1', 'q': 'cats'})
# def user_search():
# """User's search."""
#     sort = request.args['sort']

# @app.route('https://api.imgur.com/3/gallery/image/{{imageHash}}')



# import webbrowser
# from imgur_python import Imgur

# imgur_client = Imgur({'client_id': '9b3......'})
# auth_url = imgur_client.authorize()
# webbrowser.open(auth_url)

# access_token = imgur_client.access_token()
# print(access_token)

















# import requests

# # res = requests.get('https://imgur.com/search', params={'q': 'cats'})
# res = requests.get('https://imgur.com/t/dogs_in_sweaters/jBQkwee')


# # data = {
# #     'username': 'chickens'
# # }

# # requests.post('https://enmztqi8a89vgh4.m.pipedream.net', json=data)


# key = 'e5261d5a2af201ef8029fc111c8dd1e9946f43de'

# response = requests.get('https://api.imgur.com/3/tags', params={'key': key})
