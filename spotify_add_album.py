from __future__ import unicode_literals
from soco.compat import quote_url

def spotify_add_album(device, service, service_id, pos=0):
    '''
    Add a spotify album to the queue. Seems to work also with an artist's TopTracks and Radio.

    Parameters:
    device:       a soco device (eg device = list(soco.discover())[0].group.coordinator)
    service:      a spotify music service object (eg soco.music_services.MusicService('Spotify'))
    service_id:   the spotify id of the album to be added (eg 'spotify:album:5qo7iEWkMEaSXEZ7fuPvC3')
    pos:          the desired position in the queue, or 0 for the end of the queue

    Returns:
    The enqueued position of the first item, as returned by device
    '''
    item_id = '0fffffff{0}'.format(quote_url(service_id))
    meta = '''<DIDL-Lite xmlns:dc="http://purl.org/dc/elements/1.1/" \
xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/" \
xmlns:r="urn:schemas-rinconnetworks-com:metadata-1-0/" \
xmlns="urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/">\
<item id="{0}" parentID="DUMMY" restricted="true">\
<dc:title>DUMMY</dc:title>\
<upnp:class>object.container.album.musicAlbum</upnp:class>\
<desc id="cdudn" nameSpace="urn:schemas-rinconnetworks-com:metadata-1-0/">{1}</desc>\
</item></DIDL-Lite>'''.format(item_id, service.desc)

    try:
        response = device.avTransport.AddURIToQueue([
            ('InstanceID', 0),
            ('EnqueuedURI', 'x-rincon-cpcontainer:' + item_id),
            ('EnqueuedURIMetaData', meta),
            ('DesiredFirstTrackNumberEnqueued', pos),
            ('EnqueueAsNext', 1 if pos == 0 else 0)
        ])
        return int(response['FirstTrackNumberEnqueued'])
    except Exception as ex:
        print(ex)
