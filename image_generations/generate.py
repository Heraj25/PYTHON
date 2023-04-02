from PIL import Image, ImageDraw, ImageFont

def generate_image(prompt, image_size=(512, 512)):
    image = Image.new('RGB', image_size, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=32)
    draw.text((10, 10), prompt, fill=(0, 0, 0), font=font)
    return image

prompt = "A cat sitting on a cloud"
image = generate_image(prompt)
image.show()