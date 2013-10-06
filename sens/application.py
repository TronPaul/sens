import argparse
import sys
from sens import image
from sens import status

def main():
    parser = argparse.ArgumentParser(description='Generate twitch status image')
    parser.add_argument('channel_name', metavar='channel-name', help='Channel to pull data from')
    parser.add_argument('file', help='File to write image to')
    args = parser.parse_args()
    s = status.get_status(args.channel_name)
    img = image.build_image(s)
    img.save(args.file, format='png')
