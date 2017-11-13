import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageChops
import os

os.system("title BirdGen 2000")

def main():
	
	f = open('birdgen.txt','a')
	
	colors = [
		"White",
		"Red",
		"Crimson",
		"Mistyrose",
		"Pink",
		"Orange",
		"Yellow",
		"Gold",
		"Green",
		"Olive",
		"Teal",
		"Blue",
		"Aqua",
		"Steelblue",
		"Indigo",
		"Violet",
		"Maroon",
		"Brown",
		"Sienna"
	]
	
	parts = [
		#"-capped",
		#"-beaked",
		#"-cheeked",
		#"-breasted",
		#"-footed",
		#"-eyed",
		#"-tailed",
		#"-winged",
		#"-crested",
		"-ringed",
		"-striped",
		"-spotted"
	]
		
	species = [
		"Hawk",
		"Eagle",
		#/"Finch",
		#/"Swallow",
		#/"Duck",
		"Conure",
		#/"Dove",
		"Ibis",
		"Owl"
	]
	
	names = [
		"Jane",
		"Marie",
		"Nova",
		"Hal",
		"Ash",
		"Hayley",
		"Harrison Ford",
		"Disney",
		"Katie",
		"Mario & Luigi",
		"Michelle"
	]

	spe = random.choice(species)
	col = random.choice(colors)
	prt = random.choice(parts)
	nme = random.choice(names)
	
	chance = (random.randint(1,100))
	if chance <= 5:
		spe = "Furby"
	
	anname = str(col + prt + " " + spe)

	def makeBird(colors, parts, species):
		for i in range(1,10):
			stringA = ((random.choice(colors)) + (random.choice(parts)) + " " + (random.choice(species)))
			print(stringA)
			f.write(str("- " + stringA + '\n'))
			
	def nameBird(names, colors, species):
		f.write('\n')
		for i in range(1,10):
			stringB = ((random.choice(names)) + "'s " + (random.choice(colors)) + " " + (random.choice(species)))
			print(stringB)
			f.write(str("- " + stringB + '\n'))	
		f.write('\n')

	print("---> CHECK OUT THESE SWEET NEW BIRDS!!! <---")
	makeBird(colors, parts, species)
	print(" ")
	print("---> CHECK OUT THESE OTHER AND EQUALLY SWEET NEW BIRDS!!! <---")
	nameBird(names, colors, species)
	print(" ")
	print("Pictured: " + anname)
	
	backdrop = Image.open("parts/backdrop.png")
	body = Image.open("parts/" + spe + "/basecolor.png")
	lines = Image.open("parts/" + spe + "/lines.png")
	spots = Image.open("parts/" + spe + "/spots.png")
	rings = Image.open("parts/" + spe + "/rings.png")
	stripes = Image.open("parts/" + spe + "/stripes.png")
	
	tmp = Image.new('RGBA', spots.size, (0,0,0,0))
	draw = ImageDraw.Draw(tmp)
	draw.rectangle(((0, 0), spots.size), fill=(col))
	
	tmp2 = Image.new('RGBA', spots.size, (0,0,0,1))
	draw = ImageDraw.Draw(tmp2)
	draw.rectangle(((0, 0), spots.size), fill=(col))
	
	body2 = ImageChops.multiply(body, tmp2)
	
	Image.alpha_composite(backdrop, body2).save("BIRDS/test2.png")
	test2 = Image.open("BIRDS/test2.png")
	
	if prt == "-ringed":
		rings2 = ImageChops.multiply(rings, tmp)
		Image.alpha_composite(test2, rings2).save("BIRDS/test3.png")
	elif prt == "-spotted":
		spots2 = ImageChops.multiply(spots, tmp)
		Image.alpha_composite(test2, spots2).save("BIRDS/test3.png")
	elif prt == "-striped":
		stripes2 = ImageChops.multiply(stripes, tmp)
		Image.alpha_composite(test2, stripes2).save("BIRDS/test3.png")
	else:
		Image.alpha_composite(test2, lines).save("BIRDS/test3.png")
		
	test3 = Image.open("BIRDS/test3.png")
	Image.alpha_composite(test3, lines).save("BIRDS/" + str(anname + ".png"))
		
	os.remove("BIRDS/test2.png")
	os.remove("BIRDS/test3.png")
	imeg = Image.open("BIRDS/" + str(anname + ".png"))
	imeg.show()
	
	f.close()
	
main()
