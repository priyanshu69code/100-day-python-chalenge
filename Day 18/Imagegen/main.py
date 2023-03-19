import colorgram as co

colours = co.extract(
    "F:\\100 day python chalenge\\100 day python chalenge\\Day 18\\Imagegen\\plate.png", 150)

colours_list = []
for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.r
    b = colour.rgb.b
    colours_list.append((r, g, b))

print(len(colours_list))
