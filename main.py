from PIL import Image, ImageDraw, ImageFont

template = Image.open("template.jpg")
font = ImageFont.truetype("font.ttf", 24)

winners = {
    "Имя_победителя2": "Место_победителя2",
    "Имя_победителя3": "Место_победителя3",
    "Имя_победителя4": "Место_победителя4",
}

x_place = 100
y_place = 100

x_name = 50
y_name = 50

for winner, place in winners.items():
    template = Image.open("template.jpg")

    draw = ImageDraw.Draw(template)

    draw.text((x_place, y_place), winner, font=font, fill=(0, 0, 0))
    draw.text((x_name, y_name), place, font=font, fill=(0, 0, 0))

    template.save("Грамота" + winner + ".jpg")
