from django.conf import settings
from .serializers import CricketSerializer
from .models import Cricket
from background_task import background
import requests,json
from datetime import datetime
from .keys import keys          #Make sure to populate your keys array

latest_time = '2000-01-01T00:00:00.0Z'
q=[]
for key in keys:
    q.append(key)

@background()
def db_store():
    global latest_time
    print('---Running---')
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    while 1:
        # Query paramas
        params ={
            'part': 'snippet',
            'q': 'cricket',
            'type': 'video',
            'key': q[0],
            'publishedAfter': latest_time,
            'maxResults': 50,
            'order':'date'
            }
        results = requests.get(search_url,params=params)
        # If key fails, push the key to the back of the queue
        if results.status_code==403:
            print('----Request failed----')
            q.append(q.pop(0))
            continue
        results = results.json()
        for res in results["items"]:
            res = res
            data={
                'videoId': res["id"]['videoId'],
                'title': res['snippet']['title'],
                'description': res['snippet']['description'],
                'publishedAt': res['snippet']['publishedAt'],
                'thumbUrl': res['snippet']['thumbnails']['default']['url']
                }
            latest_time = max(latest_time,data['publishedAt'])
            try:
                data['publishedAt'] = datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
            except:
                data['publishedAt'] = datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            serializer = CricketSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        return