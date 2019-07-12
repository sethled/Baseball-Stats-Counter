import re
import sys, os

playerDict = dict()
results = dict()
resultList = list()

def rV(list):
    return list[1]

if len(sys.argv) > 2:
     sys.exit(f"Usage: {sys.argv[0]} filename")

elif len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

elif not os.path.exists(sys.argv[1]):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

else:
    givenFile = []
    filename = sys.argv[1]
    with open(filename) as f:
        for line in f:
            givenFile.append(line.strip())
            #print(line)

nBHRegex = re.compile(r"(\w+ \w+) batted (\d) times with (\d) hits and (\d) runs")

def name(line):
    match = nBHRegex.match(line)
    if match is not None:
        return str(match.group(1))
    else:
        return False

def bats(line):
	match = nBHRegex.match(line)
	if match is not None:
		return int(match.group(2))
	else:
		return False

def hits(line):
	match = nBHRegex.match(line)
	if match is not None:
		return int(match.group(3))
	else:
		return False

def runs(line):
	match = nBHRegex.match(line)
	if match is not None:
		return int(match.group(4))
		return False

i = 0
while i < len(givenFile):
    playerName = name(givenFile[i])
    playerBats = bats(givenFile[i])
    playerHits = hits(givenFile[i])
    
    if playerName != False:

        if playerName in playerDict:
            oldBats = playerDict.get(playerName)[0]
            oldHits = playerDict.get(playerName)[1]

            newBats = oldBats + playerBats
            newHits = oldHits + playerHits

            playerDict[playerName] = [newBats, newHits]
            results[playerName] = (newHits)/(newBats)
        else:
            playerDict[playerName] = [playerBats, playerHits] 
            results[playerName] = (playerHits)/(playerBats)
            # Found syntax for maintaining trailing zeros while rounding here: https://stackoverflow.com/questions/16763327/python-round-leaving-a-trailing-0
            # My original syntax: results[playerName] = round(float(playerHits)/float(playerBats), 3)
    
    i += 1

# for playerName,values in playerDict.items():
#     print(playerName)
#     print(values)
# ADDRESS ISSUES YOU RECEIVE WHEN RUNNING THE CODE ABOVE WITH A TA~!

for nameIndex in results:
    resultList.append([nameIndex, results[nameIndex]])

resultList = sorted(resultList, key = rV, reverse = True)
i = 0
while i < len(resultList):
    resultList[i][1] = '%.3f' % (float(resultList[i][1]))
    print(f"{resultList[i][0]}: {resultList[i][1]}")
    i += 1