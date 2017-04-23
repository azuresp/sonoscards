# trivial client for talking over http to sonoshack.py service

import requests

def play_thing(sourcetype, title):
    put('source', {'type':sourcetype, 'title': title})

def set_mode(command):
    put('mode', {'command':command})

def set_volume(volume):
    put('volume', {'level':volume})

def put(command, payload):
    response = requests.put("http://127.0.0.1:5000/" + command, json=payload)
    print(response.status_code, response.reason)


play_thing('album', 'Abba Gold')
set_volume(4)
set_mode('play')
