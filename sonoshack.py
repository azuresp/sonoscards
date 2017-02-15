from soco import SoCo
import soco
import urllib
from soco.music_services import MusicService
import spotify_add_album

def play_favorite(player, title):
    favorites = x.get_sonos_favorites()['favorites']
    for favorite in favorites:
        if favorite['title'] == title:
            uri = favorite['uri']
            if uri.startswith('x-rincon-cpcontainer') and 'spotify' in uri:
                play_spotify_album(player, uri)
            else:
                play_uri(player, favorite['uri'], favorite['meta'], favorite['title'])
            break

def play_uri(player, uri, meta, title):
    print('playing %s' % uri)
    player.clear_queue()
    try:
        player.play_uri(uri, meta, title)
    except soco.exceptions.SoCoUPnPException as ex:
        if ex.error_code == '801':
            player.play()
        else:
            pass

def play_album(player, title):
    lib = soco.music_library.MusicLibrary(player)
    albums = lib.get_music_library_information(search_type='albums', search_term=title)
    album = albums[0]
    tracks = lib.get_tracks_for_album(album.creator, album.title)
    player.clear_queue()
    for track in tracks:
        player.add_to_queue(track)
    player.play_from_queue(0)

def list_favorites(player):
    favorites = x.get_sonos_favorites()['favorites']
    for favorite in favorites:
        print(favorite)
        # print('{} : {}'.format(favorite['title'], favorite['uri']))

def play_spotify_album(player, uri):
    # need to convert from x-rincon-cpcontainer:1004206cspotify%3aalbum%3a2pbkqNS3aQJfEgm20nUe5P
    # to spotify:album:2pbkqNS3aQJfEgm20nUe5P
    print('playing spotify album')
    spotify = MusicService('Spotify')
    spotid = urllib.parse.unquote(uri[21::])
    start = spotid.find('spotify:')
    spotid = spotid[start::]

    # x.stop()
    x.clear_queue()
    spotify_add_album.spotify_add_album(x, spotify, spotid)
    x.play_from_queue(0)

x = SoCo('192.168.0.10')

# to play:
print(x.player_name)
# play_favorite(x, 'Toddler Radio')
# play_favorite(x, 'Choo Choo Soul')
# play_favorite(x, 'Bat out of Hell [Bonus Tracks]')
play_album(x, 'Frozen (Soundtrack)')
# list_favorites(x)
