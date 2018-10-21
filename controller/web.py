from flask import Flask
from flask import request
from soco import SoCo
import sonoshack

app = Flask(__name__)
player = SoCo('192.168.0.110')
current_type = ''
current_title = ''
current_volume = player.volume

@app.route('/')
def index():
    return 'Hello world'

@app.route('/source', methods=['PUT'])
def setsource():
    global current_type
    global current_title
    global player
    if not request.json or not 'title' in request.json or not 'type' in request.json:
        return('missing title or type', 400)
    new_type = request.json['type']
    new_title = request.json['title']
    if new_type != current_type or new_title != current_title:
        if new_type == 'favorite':
            print('playing favorite')
            sonoshack.play_favorite(player, new_title)
        elif new_type == 'album':
            print('playing album')
            sonoshack.play_album(player, new_title)
        else:
            print('bad type:', new_type)
            return ('bad type', 400)
        current_type = new_type
        current_title = new_title
        return ('', 204)
    else:
        sonoshack.play()
        print('already playing this')
        return ('', 204)

@app.route('/volume', methods=['PUT'])
def setvolume():
    global current_volume
    global player
    new_volume = request.json['level']
    if new_volume != current_volume:
        print('updating volume to ', new_volume)
        player.volume = new_volume
        current_volume = new_volume
    return ('', 204)

@app.route('/mode', methods=['PUT'])
def setmode():
    global player
    new_mode = request.json['command']
    if new_mode == 'play':
        sonoshack.play()
    elif new_mode == 'pause':
        sonoshack.pause()
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

