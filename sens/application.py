import argparse
import sys
import sens.image
import sens.status

def main():
    parser = argparse.ArgumentParser(description='Generate twitch status image')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
    parser.add_argument('channel_name', metavar='channel-name', help='Channel to pull data from')
    parser.add_argument('file', help='File to write image to')
    args = parser.parse_args()
    try:
        img = build_image(args.channel_name)
        img.save(args.file, format='png')
    except sens.status.TwitchError as e:
        print('Error retrieving channel data from Twitch.tv')
        if args.verbose:
            print('Response: {json}'.format(json=e.json), sys.stderr)

def build_image(channel_name):
    s = sens.status.get_status(channel_name)
    return sens.image.build_image(s)
