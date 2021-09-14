from googleapiclient.discovery import build
#import pandas as pd

#Canal 1

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)
snippets = youtube.search().list(part='snippet', type='channel', q='TheGrefg').execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: TheGrefg')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 1er canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

#-----------------------------------------------------------------------------------------------------------

#Canal 2

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)
snippets = youtube.search().list(part='snippet', type='channel', q='Luisito Comunica').execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Luisito Comunica')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 2do canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

#-----------------------------------------------------------------------------------------------------------

#Canal 3

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)
snippets = youtube.search().list(part='snippet', type='channel', q='Ubaman').execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Uabman')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 3er canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

#-----------------------------------------------------------------------------------------------------------

#Canal 4

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)
snippets = youtube.search().list(part='snippet', type='channel', q='Coreano Vlogs').execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Coreano Vlogs')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 4to canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')

#-----------------------------------------------------------------------------------------------------------

#Canal 5

api_key = 'AIzaSyBKe0n9tKUtFh7Bja5DUXab3mT-ZDUe4Ww'
youtube = build('youtube', 'v3', developerKey=api_key)
snippets = youtube.search().list(part='snippet', type='channel', q='Auron').execute()

channelId = snippets['items'][0]['snippet']['channelId']
stats = youtube.channels().list(part='statistics', id=channelId).execute()
subscribers = stats['items'][0]['statistics']['subscriberCount']
contVistas = stats['items'][0]['statistics']['viewCount']
cantVideos = stats['items'][0]['statistics']['videoCount']
print(f'Nombre del Canal: Auron')
print(f'Subscritores: {int(subscribers).__format__(",")}')
print(f'Vistas del canal: {int(contVistas).__format__(",")}')
print(f'Total de videos: {int(cantVideos).__format__(",")}')
print(f'ID del 5to canal: {channelId}')
print('Descripcion del canal: ')
print(snippets['items'][0]['snippet']['description'] + '\n')