# trivial client for talking over http to sonoshack.py service

import requests

def play_thing(sourcetype, title):
    put('source', {'type':sourcetype, 'title': title})

def set_mode(command):
    put('mode', {'command':command})

def set_volume(volume):
    put('volume', {'level':volume})

def put(command, payload):
    response = requests.put("http://localhost:5000/" + command, json=payload)
    print(response.status_code, response.reason)

def parse(request):
    params = request.split('~')
    if params[0] == 'source':
        if len(params) != 3:
            print("ERROR: 3 parameters required for source")
        else:
            play_thing(params[1], params[2])
    elif params[0] == 'command':
        if len(params) != 2:
            print("ERROR: 2 parameters required for command(/mode)")
        else:
            set_mode(params[1])
    elif params[0] == 'volume':
        if len(params != 2):
            print("ERROR: 2 parameters required for volume")
        else:
            set_volume(params[1])
    else:
        print("ERROR: unrecognized command")

#parse("source~album~play")