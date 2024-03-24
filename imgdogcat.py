import warnings
warnings.filterwarnings("ignore")
import requests
import argparse
import sys
from PIL import Image, ImageDraw
import io
import random
from subprocess import run
from tempfile import NamedTemporaryFile
import os

parser = argparse.ArgumentParser(description='Fetch a random dog or cat image.')
parser.add_argument('-d', '--dog', action='store_true', help='Fetch a random dog image.')
parser.add_argument('-c', '--cat', action='store_true', help='Fetch a random cat image.')
parser.add_argument('-g', '--gif', action='store_true', help='Fetch a random gif image.')
args = parser.parse_args()

script_directory = os.path.dirname(os.path.realpath(__file__))
imgcat_path = os.path.join(script_directory, 'imgcat.sh')
print(imgcat_path)

if args.gif:
    # tags = ["new+jeans", "twice", "ive", "black+pink", "red+velvet", "itzy", "aespa", "LE+SSERAFIM"]
    tags = ["new+jeans", "aespa", "LE+SSERAFIM"]
    url = "https://api.giphy.com/v1/gifs/random?api_key=qYBdjc9BCKh4NLmuVgWiCakpWT3OraDz&tag=" + random.choice(tags) + "+Kpop"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        url = data.get('data', {}).get('images', {}).get('original', {}).get('url')
        if not url:
            print('Error fetching gif URL')
        else:
            run(["echo"])
            run([imgcat_path, "-u", "-W", "50%", url])
    else:
        print('Error fetching gif')
    sys.exit()

if args.dog:
    url = "https://dog.ceo/api/breeds/image/random"
    json_key = 'message'
elif args.cat:
    url = "https://api.thecatapi.com/v1/images/search"
    json_key = 'url'
else:
    if bool(random.getrandbits(1)):
        url = "https://dog.ceo/api/breeds/image/random"
        json_key = 'message'
    else:   
        url = "https://api.thecatapi.com/v1/images/search"
        json_key = 'url'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if isinstance(data, list):
        data = data[0]
    image_url = data.get(json_key, 'No image URL found')
else:
    image_url = 'Error fetching image'
    print(image_url)
    sys.exit()

response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content)).convert("RGBA")

max_width, max_height = 800, 600
image.thumbnail((max_width, max_height))

mask = Image.new('L', (image.width, image.height), 0)
draw = ImageDraw.Draw(mask)
radius = 50
draw.rounded_rectangle((0, 0, image.width, image.height), radius=radius, fill=255)

image.putalpha(mask)
# result.show()

with NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
    image.save(tmp_file, format='PNG')
    tmp_file_name = tmp_file.name


run(["echo"])
run([imgcat_path, tmp_file_name])
os.remove(tmp_file_name)
