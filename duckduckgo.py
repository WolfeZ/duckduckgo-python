#duckduckgo python
import json
import urllib.request
get_ddg = urllib.request.urlopen("http://api.duckduckgo.com/?q=tweakers.net&format=json&pretty=1")
ddg_read = get_ddg.read()
ddg_read_decode = json.loads(ddg_read.decode('utf-8'))
ddg_read = ddg_read_decode
json_string = json.dumps(ddg_read,sort_keys=True,indent=2)
print(json_string)
ddg_topics = ddg_read['RelatedTopics']
for item in ddg_topics:
    print(item['FirstURL'])
