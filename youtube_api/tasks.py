from django.conf import settings
from .serializers import CricketSerializer
from .models import Cricket
from background_task import background
import requests,json
from datetime import datetime

latest_time = '2000-01-01T00:00:00.0Z'
q=[]
q.append('AIzaSyC3KbXEXt7Ft5aTfiPCtTrT64oSvXKsEyc')
q.append('AIzaSyBgpbpPFfpJaHMPHxzELJwUiR2CEL5UABk')

@background()
def dbStore():
    global latest_time
    print('---Running---')
    searchUrl = 'https://www.googleapis.com/youtube/v3/search'
    flag=True
    while 1:
        print(latest_time)
        params ={
            'part': 'snippet',
            'q': 'cricket',
            'type': 'video',
            'key': q[0],
            'publishedAfter': latest_time,
            'maxResults': 50,
            'order':'date'
            }
        results = requests.get(searchUrl,params=params)
        # If key fails, push the key to the back of the queue
        if results.status_code==403:
            print('----Key failed----')
            q.append(q.pop(0))
            continue
        results = results.json()
        for res in results["items"]:
            res = res
            data = {
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
            obj = Cricket.objects.filter(videoId=data['videoId']).first()
            if not obj and serializer.is_valid():
                serializer.save()
        return




