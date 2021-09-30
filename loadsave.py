import json
from soccer import Team, Game, GameFromDict, TeamFromDict

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

def loadGames(filename):
    result=[]
    with open(filename) as json_file:
        res = json.load(json_file)
    for tour in res:
        gameList=[]
        for game in tour:
            gameList.append(GameFromDict(game))
        result.append(gameList)
    return result
        
def saveGames(filename,gameList):
    toSave=[[game.asDict() for game in tour] for tour in gameList]
    with open(filename, "w") as json_file:
        json.dump(toSave, json_file, indent=4)
