from pystray import Icon , Menu, MenuItem
import pystray

from PIL import Image, ImageDraw, ImageColor

#托盘程序
def create_image(width, height, color1, color2):
  # Generate an image and draw a pattern
  image = Image.new('RGB', (width, height), color1)
  dc = ImageDraw.Draw(image)
  dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
  dc.rectangle((0, height // 2, width // 2, height), fill=color2)

  return image

def on_click(icon:Icon,item:MenuItem):
  item.text='changed'

Icon('test',
     create_image(200, 200, 'black', 'blue'),
     menu=Menu(
         MenuItem(
             'With submenu',
             Menu(MenuItem('Show message', on_click),
                  MenuItem('Submenu item 2', lambda icon, item: icon.remove_notification()))))).run()
