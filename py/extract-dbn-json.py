import json 

def readLines():
    with open("py/dbn.tsv", "r") as f:
        lines = f.readlines()
        
        return lines[1:13] + lines[14:26] + lines[27:39] + lines[40:52] + lines[53:65] + lines[66:78] + lines[79:91]

def createBlockStages(block):
    block = { "block": block, "start": block * 2, "end": (block + 1) * 2 }
    # for stage in range(1, 9):
    #     block[str(stage)] = -1

    return block

lines = readLines()
print(len(lines) /12)

data = [{"day": day + 1, "blocks": [createBlockStages(block) for block in range(12)]} for day in range(31)]
zoneSet = set()

block = 0
stage = 1
for line in lines:
    parts = line.split()
    block = parts[0]
    blockNumber = int(block[0:2]) // 2
    day = int(parts[5])
    stages = [[str(y) for y in x.replace("\"", "").split(',')] for x in parts[1:5]]
    print(blockNumber, block, stages, day)
    for stageNumber in range(4):
        zones = stages[stageNumber]
        data[day]["blocks"][blockNumber][stageNumber + 1] = zones
        for zone in zones:
            zoneSet.add(zone)
    # continue
    # for zone in zones:
    #     data[day]["blocks"][block][stage] = zone
    #     zoneSet.add(zone)
    #     day = day + 1
    # stage = stage + 1
    # if stage == 9:
    #     stage = 1
    #     block = block + 1

zoneList = list(zoneSet)
zoneList.sort()

dbnData = {
    "zones": zoneList,
    "matrix": data
}

with open("src/js/dbn.json", "w") as fout:
    print(json.dumps(dbnData, indent=2), file = fout)

