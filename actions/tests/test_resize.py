from PIL import Image

from actions.resize import *


def test_weight():
    image = Image.open("imgs/resize/python.jpg")
    print(image.size)    
    assert resize(image) == 10
