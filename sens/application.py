import argparse
import sys
import sens.image
import sens.status

def main():
    parser = argparse.ArgumentParser(description='Generate twitch status image')
    parser.add_argument('channel_name', metavar='channel-name', help='Channel to pull data from')
    parser.add_argument('file', help='File to write image to')
    args = parser.parse_args()
    img = build_image(args.channel_name)
    img.save(args.file, format='png')

def build_image(channel_name):
    s = sens.status.get_status(channel_name)
    return sens.image.build_image(s)
