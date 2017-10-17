import random
from PIL import Image
import os

#os.system("mode con cols=80 lines=28")
os.system("title BirdGen 2000")

def main():
	
	f = open('birdgen.txt','a')
	
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
			stringA = ((random.choice(colors)) + "" + (random.choice(parts)) + " " + (random.choice(species)))
			print(stringA)
			f.write(str("- " + stringA + '\n'))
			
	def nameBird(names, colors, species):
		for i in range(1,10):
			stringB = ((random.choice(names)) + "'s " + (random.choice(colors)) + " " + (random.choice(species)))
			print(stringB)
			f.write(str("- " + stringB + '\n'))	

	print("---> CHECK OUT THESE SWEET NEW BIRDS!!! <---")
	makeBird(colors, parts, species)
	print(" ")
	print("---> CHECK OUT THESE OTHER AND EQUALLY SWEET NEW BIRDS!!! <---")
	nameBird(names, colors, species)
	
	img = Image.open('tstbird.jpg')
	img.show()
	
	f.close()
	
main()
