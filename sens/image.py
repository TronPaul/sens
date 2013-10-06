import urllib.request
import io
from PIL import Image, ImageDraw
ONLINE = 'ONLINE'
OFFLINE = 'OFFLINE'
PADDING = 3

def build_image(twitch_status):
    logo_url = twitch_status.logo_url
    status = twitch_status.status
    name = twitch_status.display_name
    game = twitch_status.game
    online = twitch_status.online
    viewers = twitch_status.viewers
    preview_url = twitch_status.preview_url

    img = Image.new('RGB', (400, 50))
    logo_img = get_image_from_url(logo_url)
    logo_img = logo_img.resize((50, 50))
    img.paste(logo_img, (0,0,50,50))

    draw = ImageDraw.Draw(img)

    font = draw.getfont()
    text_left = logo_img.size[0] + PADDING
    draw.text((text_left,3), status, font=font)

    info_text = '{name} streaming {game}'.format(name=name, game=game)
    draw.text((text_left,18), info_text, font=font)

    if online:
        online_width, _ = font.getsize(ONLINE)
        draw.text((text_left, 33), ONLINE, font=font)

        viewers_left = text_left + online_width + PADDING
        viewers_text = '{viewers} viewers'.format(viewers=viewers)
        draw.text((viewers_left, 33), viewers_text)
        viewers_right = font.getsize(viewers_text)[0] + viewers_left

        preview_max_left = viewers_right + PADDING
        preview_max_size = (img.size[0] - preview_max_left, img.size[1])

        preview_img = get_image_from_url(preview_url)
        preview_img_pos = tuple(map(lambda i: i[0] - i[1], zip(img.size,
            preview_img.size)))
        img.paste(preview_img, preview_img_pos)
    else:
        draw.text((text_left, 33), OFFLINE, font=font)
    return img

def get_image_from_url(url):
    resp = urllib.request.urlopen(url)
    resp_bytes = io.BytesIO(resp.read())
    return Image.open(resp_bytes)
