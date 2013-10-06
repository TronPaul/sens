import http.client
import io
import json

def get_status(channel_name):
    conn = http.client.HTTPSConnection('api.twitch.tv', strict=False)
    base_path = '/kraken/'
    headers = {'Accept':'application/vnd.twitchtv.v3+json'}
    conn.request('GET', '{base}channels/{channel_name}'.format(
        base=base_path, channel_name=channel_name), headers=headers)
    channel_resp = conn.getresponse()
    channel_data = json.load(io.TextIOWrapper(channel_resp))
    conn.request('GET', '{base}streams/{channel_name}'.format(
        base=base_path, channel_name=channel_name), headers=headers)
    stream_resp = conn.getresponse()
    stream_data = json.load(io.TextIOWrapper(stream_resp))
    display_name = channel_data['display_name']
    status = channel_data['status']
    game = channel_data['game']
    logo_url = channel_data['logo']
    online = stream_data['stream'] is not None
    viewers = stream_data['viewers'] if online else None
    preview_url = stream_data['preview']['small'] if online else None
    return TwitchStatus(logo_url, status, display_name, game, online,
                        viewers, preview_url)

class TwitchStatus(object):
    def __init__(self, logo_url, status, display_name, game,
                 online, viewers, preview_url):
        self.logo_url = logo_url
        self.status = status
        self.display_name = display_name
        self.game = game
        self.online = online
        self.viewers = viewers
        self.preview_url = preview_url
