# Python script to add watermarks to images
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def add_watermark(input_path, output_path, watermark_text):
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 36)
    draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128), font=font)
    image.save(output_path)



    


