#Jennifer Dooley
#830371622
#Assignment 7

SAMPLES = [0.82,	0.56,	0.08,	0.81,	0.34,	0.22,	0.37,	0.99,	0.55,	0.61,	0.31,	0.66,	0.28,	1.0,	0.95,	
0.71,	0.14,	0.1,	1.0,	0.71,	0.1,	0.6,	0.64,	0.73,	0.39,	0.03,	0.99,	1.0,	0.97,	0.54,	0.8,	
0.97,	0.07,	0.69,	0.43,	0.29,	0.61,	0.03,	0.13,	0.14,	0.13,	0.4,	0.94,	0.19, 	0.6,	0.68,	0.36,	
0.67,	0.12,	0.38,	0.42,	0.81,	0.0,	0.2,	0.85,	0.01,	0.55,	0.3,	0.3,	0.11,	0.83,	0.96,	0.41,	
0.65,	0.29,	0.4,	0.54,	0.23,	0.74,	0.65,	0.38,	0.41,	0.82,	0.08,	0.39,	0.97,	0.95,	0.01,	0.62,	
0.32,	0.56,	0.68,	0.32,	0.27,	0.77,	0.74,	0.79,	0.11,	0.29,	0.69,	0.99,	0.79,	0.21,	0.2,	0.43,	
0.81,	0.9,	0.0,	0.91,	0.01]

SAMPLE_SIZE = 100

class Node:
	def __init__(self, name, prob):
		self.name = name
		self.prob = prob

def createNetwork():
	network = dict()
	network['C'] = Node("Cloudy", .5)
	network['S'] = Node("Sprinkler",{'c':.1, '~c':.5})
	network['R'] = Node("Rain",{'c':.8, '~c':.2})
	network['W'] = Node("Wet grass",{'sr':.99, 's~r':.9,'~sr':.9, '~s~r':.0})
	return network

class Prior:
	def __init__(self, network):
		self.network = network
		self.samples = []
		self.fillSamples(self.samples)
		self.sampleSize = SAMPLE_SIZE/4
		self.values = []
		self.generateValues()

	def fillSamples(self,samples):
		for i in SAMPLES:
			samples.append(i)

	def generateValues(self):
		for i in range(0, self.sampleSize):
			#pops 4 numbers off the beginnning of samples list
			cloudy = self.samples.pop()
			sprinkler = self.samples.pop()
			rain = self.samples.pop()
			wetGrass = self.samples.pop()

			temp = []

			#cloudy = True
			if cloudy < self.network['C'].prob:
				temp.append(True)

				#sprinkler = True
				if sprinkler < self.network['S'].prob['c']:
					temp.append(True)
				#sprinkler = False
				else:
					temp.append(False)

				#rain = True
				if rain < self.network['R'].prob['c']:
					temp.append(True)
				#rain = False
				else:
					temp.append(False)

			#cloudy = False
			else:
				temp.append(False)
				
				#sprinkler = True
				if sprinkler < self.network['S'].prob['~c']:
					temp.append(True)
				#sprinkler = False
				else:
					temp.append(False)

				#rain = True
				if rain < self.network['R'].prob['~c']:
					temp.append(True)
				#rain = False
				else:
					temp.append(False)

			#find wetGrass based on found sprinkler and rain values
			#if sprinkler == true
			if temp[1]:
				#if rain == true
				if temp[2]:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['sr']:
						temp.append(True)
					#wetGrass = False
					else:
						temp.append(False)
				#if rain == False
				else:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['s~r']:
						temp.append(True)
					#wetGrass = False
					else:
						temp.append(False)
			#if sprinkler == False
			else:
				#if rain == true
				if temp[2]:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['~sr']:
						temp.append(True)
					#wetGrass = False
					else:
						temp.append(False)
				#if rain == False
				else:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['~s~r']:
						temp.append(True)
					#wetGrass = False
					else:
						temp.append(False)

			self.values.append(temp)

	#1.a P(Cloudy = True)
	def A(self):
		numCloudy = 0.0
		for i in range(0,self.sampleSize):
			if self.values[i][0]:
				numCloudy += 1
		return numCloudy/self.sampleSize

	#1.b P(Cloudy = True|Rain = True)
	def B(self):
		numCloudy = 0.0
		numRain = 0.0
		for i in range(0, self.sampleSize):
			if self.values[i][2]:
				numRain += 1
				if self.values[i][0]:
					numCloudy += 1
		return numCloudy/numRain

	#1.c P(Sprinkler = True|WetGrass = True)
	def C(self):
		numSprinkler = 0.0
		numWetGrass = 0.0
		for i in range(0,self.sampleSize):
			if self.values[i][3]:
				numWetGrass += 1
				if self.values[i][1]:
					numSprinkler += 1

		return numSprinkler/numWetGrass

	#1.d P(Sprinkler = True|Cloudy = True, WetGrass = True)
	def D(self):
		numSprinkler = 0.0
		numWetGrassCloudy = 0.0
		for i in range(0,self.sampleSize):
			if self.values[i][0] and self.values[i][3]:
				numWetGrassCloudy += 1
				if self.values[i][1]:
					numSprinkler += 1

		return numSprinkler/numWetGrassCloudy

	def printProbs(self):
		print "Prior Probabilities"
		print "P(c = true): ", self.A()
		print "P(c = true | r = true): ", self.B()
		print "P(s = true | w = true): ", self.C()
		print "P(s = true | c = true, w = true): ", self.D()

class Rejection:
	def __init__(self, network):
		self.samplesA = []
		self.fillSamples(self.samplesA)
		self.samplesB = []
		self.fillSamples(self.samplesB)
		self.samplesC = []
		self.fillSamples(self.samplesC)
		self.samplesD = []
		self.fillSamples(self.samplesD)
		self.network = network

	def fillSamples(self, samples):
		for i in SAMPLES:
			samples.append(i)

	#3.a P(Cloudy = True)
	def A(self):
		numSamples = 0.0
		numCloudy = 0.0
		while(len(self.samplesA) >= 1):
			cloudy = self.samplesA.pop()
			numSamples += 1
			if cloudy < self.network['C'].prob:
				numCloudy += 1

		return numCloudy/numSamples

	#3.b P(Cloudy = True|Rain = True)
	def B(self):
		numCloudy = 0.0
		numRain = 0.0
		while(len(self.samplesB) >= 2):
			cloudy = self.samplesB.pop()
			rain = self.samplesB.pop()
			if cloudy < self.network['C'].prob:
				if rain < self.network['R'].prob['c']:
					numRain += 1
					numCloudy += 1
			else:
				if rain < self.network['R'].prob['~c']:
					numRain += 1

		return numCloudy/numRain

	#3.c P(Sprinkler = True|WetGrass = True)
	#Should give same results and 1.c
	def C(self):
		numSprinkler = 0.0
		numWetGrass = 0.0
		while(len(self.samplesC) >= 4):
			cloudy = self.samplesC.pop()
			sprinkler = self.samplesC.pop()
			rain = self.samplesC.pop()
			wetGrass = self.samplesC.pop()

			#cloudy = True
			if cloudy < self.network['C'].prob:
				cloudy = True

				#sprinkler = True
				if sprinkler < self.network['S'].prob['c']:
					sprinkler = True
				#sprinkler = False
				else:
					sprinkler = False

				#rain = True
				if rain < self.network['R'].prob['c']:
					rain = True
				#rain = False
				else:
					rain = False

			#cloudy = False
			else:
				cloudy = False
				
				#sprinkler = True
				if sprinkler < self.network['S'].prob['~c']:
					sprinkler = False
				#sprinkler = False
				else:
					sprinker = False

				#rain = True
				if rain < self.network['R'].prob['~c']:
					rain = True
				#rain = False
				else:
					rain = False

			#find wetGrass based on found sprinkler and rain values
			#if sprinkler == true
			if sprinkler:
				#if rain == true
				if rain:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['sr']:
						numWetGrass +=1
						numSprinkler += 1
				#if rain == False
				else:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['s~r']:
						numWetGrass += 1
						numSprinkler += 1
			#if sprinkler == False
			else:
				#if rain == true
				if rain:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['~sr']:
						numWetGrass += 1
				#if rain == False
				else:
					#wetGrass = True
					if wetGrass < self.network['W'].prob['~s~r']:
						numWetGrass += 1
		
		return numSprinkler/numWetGrass

	#3.d P(Sprinkler = True|Cloudy = True, WetGrass = True)
	def D(self):
		numWetGrassCloudy = 0.0
		numSprinkler = 0.0
		while(len(self.samplesD) >= 4):
			cloudy = self.samplesD.pop()
			if cloudy < self.network['C'].prob:
				sprinkler = self.samplesD.pop()
				rain = self.samplesD.pop()
				wetGrass = self.samplesD.pop()

				#sprinkler
				if sprinkler < self.network['S'].prob['c']:
					sprinkler = True
				else:
					sprinkler = False

				#rain
				if rain < self.network['R'].prob['c']:
					rain = True
				else:
					rain = False

				if sprinkler:
					if rain:
						if wetGrass < self.network['W'].prob['sr']:
							numWetGrassCloudy += 1
							numSprinkler += 1
					else:
						if wetGrass < self.network['W'].prob['s~r']:
							numWetGrassCloudy += 1
							numSprinkler += 1
				else:
					if rain: 
						if wetGrass < self.network['W'].prob['~sr']:
							numWetGrassCloudy += 1
					else:
						if wetGrass < self.network['W'].prob['~s~r']:
							numWetGrassCloudy += 1

		return numSprinkler/numWetGrassCloudy

	def printProbs(self):
		print "Rejection Probabilities"
		print "P(c = true): ", self.A()
		print "P(c = true | r = true): ", self.B()
		print "P(s = true | w = true): ", self.C()
		print "P(s = true | c = true, w = true): ", self.D()

if __name__ == "__main__":
	network = createNetwork()
	print "\nProblem 1: "
	priorSampling = Prior(network)
	priorSampling.printProbs()
	print "\nProblem 2: "
	print "P(c = true): .5"
	print "P(c = true | r = true): .8"
	print "P(s = true | w = true): .597"
	print "P(s = true | c = true, w = true): .126"
	print "For work see attachment"
	print "\nProblem 3: "
	rejSampling = Rejection(network)
	rejSampling.printProbs()
	print "\nProblem 4: "
	print "No rejection and prior sampling did not get the same values for"
	print "the probabilities because rejection sampling has a smaller error rate"
	print "\nProblem 5: "