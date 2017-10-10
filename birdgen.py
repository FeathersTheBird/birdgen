import random

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

	def makeBird(colors, parts, species):
		for i in range(1,10):
			print("- " +(random.choice(colors)) + "" + (random.choice(parts)) + " " + (random.choice(species)))
				
	#selection = int(return input())	

	#print("Hit ENTER to generate NEW BIRDS!!")
	print("CHECK OUT THESE SWEET NEW BIRDS!!!")
	makeBird(colors, parts, species)
	
main()
