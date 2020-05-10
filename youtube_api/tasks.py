from background_task import background
import requests,json
from .utilities import keys,db_store         #Make sure to populate your keys array

latest_time = '2000-01-01T00:00:00.0Z'
q=[]
for key in keys:
    q.append(key)

@background()
def api_fetch():
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
        else:
            results = results.json()
            latest_time = max(latest_time,results["items"][0]['snippet']['publishedAt'])
            db_store(results)
            return