from googleapiclient.discovery import build
api_key = 'AIzaSyCytYniTsTOWwhMZPJSj27bH7WdAD9tJBU'
youtube = build('youtube', 'v3', developerKey = api_key)

request = youtube.channels().list(
    part='statistics',
    id = 'UCxqDIXlqSU1ksBuIJNk3Aog'
)
request2 = youtube.channels().list(
    part='statistics',
    forUsername = 'francoescamilla'
      
)
response = request.execute()
response2 = request2.execute()
print(response)
print(response2)
