#!/usr/bin/env python

import sys
import urllib,zipfile,os.path,json
from pprint import pprint
from httplib2 import Http

urllib.urlretrieve ("http://mobapps.cc/data/data_en.zip", "data.zip")

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)
            
unzip("data.zip", "tmp")

with open('tmp/movies_lite.json') as data_file:    
    movies = json.load(data_file)
    data_file.close()
    
with open('tmp/tv_lite.json') as data_file:    
    shows = json.load(data_file)
    data_file.close()
    
#for movie in movies:
    #print movie['title']

#for show in shows:
    #print show['id'], show['title']



movie_id = int(sys.argv[1])


h = Http()
headers = {'Connection': 'close',
	   'Proxy-Connection': 'close',
	   'User-Agent': 'Movie Box 2.6 (iPad; iPhone OS 6.1; en_GB)',
	   'X-Newrelic-Id': 'UAAOV1ZRGwEHVllSBAM=',
	   'Accept-Encoding': 'gzip'}

resp, content = h.request("http://mobapps.cc/api/serials/get_movie_data/?id={}".format(movie_id), "GET", headers=headers)
#pprint(resp)
#pprint(content)

movie_info_json = json.loads(content)
magic_number = movie_id + 537

for lang in movie_info_json['langs']:
    if lang['active'] == "1":
	url_oid = int(lang['apple']) + magic_number
	url_id = int(lang['google']) + magic_number
	url_hash = lang['microsoft']
	
	url = "http://vk.com/video_ext.php?oid={oid}&id={id}&hash={hash}".format(oid=url_oid, id=url_id, hash=url_hash)
	print url


#pprint(movie_info_json)
