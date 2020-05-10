from .serializers import CricketSerializer
from .models import Cricket
from datetime import datetime

keys=[
"AIzaSyC3KbXEXt7Ft5aTfiPCtTrT64oSvXKsEyc",
"AIzaSyBgpbpPFfpJaHMPHxzELJwUiR2CEL5UABk",
"AIzaSyAwUMUQuz1zg6qMCsNKbDndC3zNQAHYdSo"
]

def db_store(results):
    for res in results["items"]:
        data={
            'videoId': res["id"]['videoId'],
            'title': res['snippet']['title'],
            'description': res['snippet']['description'],
            'publishedAt': res['snippet']['publishedAt'],
            'thumbUrl': res['snippet']['thumbnails']['default']['url']
            }
        try:
            data['publishedAt'] = datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
        except:
            data['publishedAt'] = datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        serializer = CricketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return