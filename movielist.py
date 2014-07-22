#!/usr/bin/env python

"""Movie List, list and play movies.

Usage:
  movielist.py list
  movielist.py play (<movie_name>|<movie_id>) [--quality=<quality>] [--player=<player_command>]
  movielist.py download <movie_name> [PATH] [--quality=<quality>]
  movielist.py update
  movielist.py (-h | --help)
  movielist.py --version
  
Arguments:
  PATH  Download path. [default: ./]

Options:
  --quality=(360p|480p|720p)            Quality [default: 480p].
  --player=<player_command>             Your favourite media player. [default: vlc]
  -h --help                             Show this screen.
  --version                             Show version.

"""
#  --sort=(rating|name|date_added|year)  Sorting. [default: date_added]
#  --filter=<filter_by>                  Filter list of movies by name
try:
    #from schema import Schema, And, Or, Use, SchemaError
    import urllib,zipfile,os.path,json, requests
    from docopt import docopt
    from pprint import pprint
except ImportError:
    exit('Folowing libraries needs to be installed:\n'
         'schema\n'
         'docopt\n'
         'requests\n')

def list_movies(args):
    with open('tmp/movies_lite.json') as data_file:    
	movies = json.load(data_file)
	data_file.close()
    #movie_list = sorted(movies, key=lambda k: k['title'])
    print "ID\tIMDB\tTitle"
    for movie in movies:
	print "{}\t{}\t{}".format(movie['id'], movie['imdb_rating'], movie['title'].encode('utf-8'))
    
def play_movie(args):
    print "Playing\n"
    
def download_movie(args):
    print "Downloading\n"

def update_database(args):
    r = requests.head("http://mobapps.cc/data/data_en.zip")
    last_modified = r.headers['last-modified']
    
    #TODO Update only if we have old data
    
    resp, header = urllib.urlretrieve("http://mobapps.cc/data/data_en.zip", "data.zip")
    
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
    
    print "Done."

def main(args):
    if args["list"]:
	list_movies(args)
    elif args["play"]:
	play_movie(args)
    elif args['download']:
	download_movie(args)
    elif args['update']:
	update_database(args)
    else:
	print("nonono")


if __name__ == '__main__':
    docopt_args = docopt(__doc__, version='Movie List 0.1')
    #pprint(docopt_args)
    main(docopt_args)