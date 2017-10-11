import random
from PIL import Image

def main():
	
	colors = [
		"Iridescent",
		"White",
		"Pale",
		"Rainbow",
		"Red",
		"Rosy",
		"Orange",
		"Sunny",
		"Yellow",
		"Golden",
		"Green",
		"Verdant",
		"Blue",
		"Aqua",
		"Steel",
		"Indigo",
		"Violet"
	]
	
	parts = [
		"-capped",
		"-beaked",
		"-cheeked",
		"-breasted",
		"-footed",
		"-eyed",
		"-tongued",
		"-tailed",
		"-winged",
		"-crested",
		"-ringed",
		"-striped",
		"-spotted"
	]
		
	species = [
		"Hawk",
		"Eagle",
		"Falcon",
		"Jay",
		"Junco",
		"Finch",
		"Osprey",
		"Swallow",
		"Duck",
		"Swan",
		"Goose",
		"Chickadee",
		"Sparrow",
		"Conure",
		"Dove",
		"Ibis",
		"Owl",
		"Gull"
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

	def makeBird(colors, parts, species):
		for i in range(1,10):
			print("- " +(random.choice(colors)) + "" + (random.choice(parts)) + " " + (random.choice(species)))
			
	def nameBird(names, colors, species):
		for i in range(1,10):
			print("- " +(random.choice(names)) + "'s " + (random.choice(colors)) + " " + (random.choice(species)))
				

	print("CHECK OUT THESE SWEET NEW BIRDS!!!")
	makeBird(colors, parts, species)
	print(" ")
	print("CHECK OUT THESE OTHER AND EQUALLY SWEET NEW BIRDS!!!")
	nameBird(names, colors, species)
	
	img = Image.open('tstbird.jpg')
	img.show()
	
main()
