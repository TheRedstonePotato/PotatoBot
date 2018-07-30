# commands/sentencegen.py

import random

class Adjective:

	def __init__(self, adjective):
		self.adj = adjective

	def getAdj(self):
		intensifiers = ['very', 'very', 'quite', 'somewhat', 'really', 'slightly', '-', '-', '-', '-', '-', '-', '-', '-', '-']
		intensifier = intensifiers[random.randint(0, len(intensifiers)-1)]
		if intensifier == '-':
			return self.adj
		else:
			return intensifier + ' ' + self.adj

class Name:

	def __init__(self, name):
		self.name = name

class Noun:

	def __init__(self, singular, plural):
		self.singular = singular
		self.plural = plural

class Be:

	def __init__(self):
		self.objectSetting = '-b'
		self.isBe = True


	@staticmethod
	def conjugate(tense, person, count):
		if tense == 'present':
			if person == 1:
				if count == 'singular':
					return 'am'
				elif count == 'plural':
					return 'are'
			elif person == 2:
				return 'are'
			elif person == 3:
				if count == 'singular':
					return 'is'
				elif count == 'plural':
					return 'are'
		elif tense == 'past':
			if person == 1:
				if count == 'singular':
					return 'was'
				elif count == 'plural':
					return 'were'
			elif person == 2:
				return 'were'
			elif person == 3:
				if count == 'singular':
					return 'was'
				elif count == 'plural':
					return 'were'
		elif tense == 'future':
			return 'will be'
		elif tense == 'present prog':
			return be.conjugate('present', person, count) + ' being'
		elif tense == 'past prog':
			return be.conjugate('past', person, count) + ' being'
		elif tense == 'future prog':
			return 'will be being'
		elif tense == 'present perfect':
			return have.conjugate('present', person, count) + ' been'
		elif tense == 'past perfect':
			return have.conjugate('past', person, count) + ' been'
		elif tense == 'future perfect':
			return 'will have been'

be = Be()

class Verb:

	def __init__(self, present, present3s, past, pastPart, presentPart, objectSetting):
		self.present = present
		self.present3s = present3s
		self.past = past
		self.pastPart = pastPart
		self.presentPart = presentPart
		self.objectSetting = objectSetting
		self.isBe = False
		self.singular = '-'
		self.plural = presentPart

	def conjugate(self, tense, person, count):
		if tense == 'present':
			if person == 3 and count == 'singular':
				return self.present3s
			else:
				return self.present
		elif tense == 'past':
			return self.past
		elif tense == 'future':
			return 'will ' + self.present
		elif tense == 'present prog':
			return be.conjugate('present', person, count) + ' ' + self.presentPart
		elif tense == 'past prog':
			return be.conjugate('past', person, count) + ' ' + self.presentPart
		elif tense == 'future prog':
			return 'will be ' + self.presentPart
		elif tense == 'present perfect':
			return have.conjugate('present', person, count) + ' ' + self.pastPart
		elif tense == 'past perfect':
			return have.conjugate('past', person, count) + ' ' + self.pastPart
		elif tense == 'future perfect':
			return 'will have ' + self.pastPart

have = Verb('have', 'has', 'had', 'had', 'having', '-d')

def getAdjectives(adjFile):
	with open(adjFile, 'r') as f:
		list = []
		for adj in f:
			list.append(adj.replace('\n', ''))
		return list

def getNouns(nounFile):
	with open(nounFile, 'r') as f:
		list = []
		for noun in f:
			variants = noun.split(' ')
			templist = []
			for variant in variants:
				templist.append(variant.replace('\n', ''))
			list.append(templist)
		return list

def getNames(nameFile):
	with open(nameFile, 'r') as f:
		list = []
		for name in f:
			list.append(name.replace('\n', ''))
		return list

def getVerbs(verbFile):
	with open(verbFile, "r") as f:
		list = []
		for verb in f:
			variants = verb.split(' ')
			templist = []
			for variant in variants:
				templist.append(variant.replace('\n', ''))
			list.append(templist)
		return list

def addNouns(nounFile, nouns):
	rawNouns = getNouns(nounFile)
	for noun in rawNouns:
		nouns.append(Noun(noun[0], noun[1]))

def addAdjectives(adjFile, adjectives):
	rawAdjs = getAdjectives(adjFile)
	for adj in rawAdjs:
		adjectives.append(Adjective(adj))

def addNames(nameFile, names):
	rawNames = getAdjectives(nameFile)
	for name in rawNames:
		names.append(Name(name))

def addVerbs(verbFile, verbs):
	rawVerbs = getVerbs(verbFile)
	verbs.append(be)
	for verb in rawVerbs:
		verbs.append(Verb(verb[0], verb[1], verb[2], verb[3], verb[4], verb[5]))

def getClause(dictionaryPath):

	nounFile = dictionaryPath + '/nouns.txt'
	verbFile = dictionaryPath + '/verbs.txt'
	adjFile = dictionaryPath + '/adjectives.txt'
	nameFile = dictionaryPath + '/names.txt'

	names = []
	nouns = []
	verbs = []
	adjectives = []

	addNames(nameFile, names)
	addNouns(nounFile, nouns)
	addVerbs(verbFile, verbs)
	addAdjectives(adjFile, adjectives)

	tenses = ['present', 'present', 'present', 'past', 'future', 'present prog', 'past prog', 'future prog', 'present perfect', 'past perfect', 'future perfect']
	persons = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
	counts = ['singular', 'plural']
	adjs = [True, True, False, False, False]
	isNames = [True, False, False, False, False]

	subjectNoun = ''
	verb = ''
	objectNoun = ''

	tense = tenses[random.randint(0, len(tenses)-1)]
	person = persons[random.randint(0, len(persons)-1)]
	count = counts[random.randint(0, len(counts)-1)]

	def getNounPhrase(count, person, be):

		nounPhrase = ''

		if be:

			nounPhrase = adjectives[random.randint(0, len(adjectives)-1)].getAdj()

		elif count == 'singular':
			if person == 3:
				articles = ['a', 'the', 'the']
				article = articles[random.randint(0, len(articles)-1)]
				validNoun = False
				noun = '' 
				while validNoun == False:
					noun = nouns[random.randint(0, len(nouns)-1)]
					if noun.singular != '-':
						validNoun = True
				nounPhrase = noun.singular
				adj = adjs[random.randint(0, len(adjs)-1)]
				if adj:
					adjective = adjectives[random.randint(0, len(adjectives)-1)]
					nounPhrase = adjective.getAdj() + ' ' + nounPhrase
				if article == 'a' and nounPhrase[0] in 'aeiouAEIOU':
					article = 'an'
				nounPhrase = article + ' ' + nounPhrase
				isName = isNames[random.randint(0, len(isNames)-1)]
				if isName:
					name = names[random.randint(0, len(names)-1)]
					nounPhrase = name.name

			elif person == 1:
				if case == 'subject':
					nounPhrase = 'I'
				elif case == 'object':
					nounPhrase = 'me'
			elif person == 2:
				nounPhrase = 'you'
		elif count == 'plural':
			if person == 3:
				articles = ['some', 'the', 'the', '-', '-', '-']
				article = articles[random.randint(0, len(articles)-1)]
				noun = nouns[random.randint(0, len(nouns)-1)]
				nounPhrase = noun.plural
				adj = adjs[random.randint(0, len(adjs)-1)]
				if adj:
					adjective = adjectives[random.randint(0, len(adjectives)-1)]
					nounPhrase = adjective.getAdj() + ' ' + nounPhrase
				if noun.singular == '-':
					count = 'singular'
				if article != '-':
					nounPhrase = article + ' ' + nounPhrase
			elif person == 1:
				if case == 'subject':
					nounPhrase = 'we'
				elif case == 'object':
					nounPhrase = 'us'
			elif person == 2:
				nounPhrase = 'you'

		return nounPhrase

	case = 'subject'
	subjectNoun = getNounPhrase(count ,person, False)
	verb = verbs[random.randint(0, len(verbs)-1)]

	verbPhrase = verb.conjugate(tense, person, count)
	sentenceFormat = '{s} {v}'
	be = False

	if verb.objectSetting == '-a':
		sentenceFormats = ['{s} {v}', '{s} {v} {o}', '{s} {v} {o}', '{s} {v} {o}', '{s} {v} {o}']
		sentenceFormat = sentenceFormats[random.randint(0, len(sentenceFormats)-1)]
	elif verb.objectSetting == '-b':
		if verb.isBe and random.randint(0, 100) > 60:
			be = True
			sentenceFormat = '{s} {v} {a}'
		else:
			sentenceFormat = '{s} {v} {o}'

	adjective = ''
	objectNoun = ''

	if sentenceFormat == '{s} {v} {o}':
		case = 'object'
		person = persons[random.randint(0, len(persons)-1)]
		count = counts[random.randint(0, len(counts)-1)]
		objectNoun = getNounPhrase(count, person, be)

	elif sentenceFormat == '{s} {v} {a}':
		adjective = adjectives[random.randint(0, len(adjectives)-1)].getAdj()

	sentence = sentenceFormat.format(s=subjectNoun, v=verbPhrase, o=objectNoun, a=adjective)

	return sentence

def getSentence(dictionaryPath):
	
	clause = getClause(dictionaryPath)
	sentence = clause

	if random.randint(0, 100) > 90:

		connectives = [' and ', ' but ', ', although ', '. However, ', ' so ', ', so ', ' because ', ' and therefore ', '. Also, ']
		connective = connectives[random.randint(0, len(connectives)-1)]

		sentence = sentence + connective + getClause(dictionaryPath)

	punctuations = ['.', '.', '.', '.', '.', '.', '.', '!']
	punctuation = punctuations[random.randint(0, len(punctuations)-1)]

	sentence = sentence[0].upper() + sentence[1:] + punctuation
	sentence = sentence.replace('%s', ' ')
	
	return sentence

# Yes, this is a mess.