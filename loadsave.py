import json
from soccer import Team

def loadTeams(filename):
    teamList=[]
    with open(filename) as json_file:
        result=json.load(json_file)
        for item in result:
            teamList.append(Team(item['name'],item['location'],item['force']))
    return teamList

def saveTeams(filename,teamList):
    toSave=[team.asDict() for team in teamList]
    with open(filename,"w") as json_file:
        json.dump(toSave,json_file,indent=4)
