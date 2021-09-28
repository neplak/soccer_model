from soccer import *

teams=[Team('Zenit','SPB'),
       Team('CSKA', 'Moscow'),
       Team('Spartak', 'Moscow'),
       Team('Lokomotiv', 'Moscow'),
       Team('Dinamo', 'Moscow'),
       Team('Khimki', 'Khimki'),
       Team('Krasnodar', 'Krasnodar'), 
       Team('Sochi', 'Sochi'),
       Team('Rubin', 'Kazan'), 
       Team('Akhmat', 'Groznyy'), 
       Team('Nizhniy Novgorod', 'Nizhniy Novgorod'),
       Team('Krylya Sovetov', 'Samara'), 
       Team('Arsenal', 'Tula'), 
       Team('Ufa', 'Ufa'),
       Team('Rostov', 'Rostov'),
       Team('Ural', 'Ekaterinburg') ]


q = [[i, j] for i in range(0, 16) for j in range(0, 16)]
allGamesIndex=list(filter(lambda x: x[0]!=x[1],q))
allGames=[]

for index in allGamesIndex:
    allGames.append(Game(teams[index[0]],teams[index[1]]))
    
for game in allGames:
    game.play()
    print(game)
    
def getPoint(games):
    result={}
    for game in games:
        winner=game.winner
        if winner:
            if str(winner) in result.keys():
                result[str(winner)]+=3
            else:
                result[str(winner)] = 3
        else:
            for key in (str(game.home),str(game.away)):
                if key in result.keys():
                    result[key]+=1
                else:
                    result[key]=1
    return result


def getPoint1(games):
    result = {}
    for game in games:
        winner = game.winner
        if winner:
            if str(winner) in result.keys():
                result[str(winner)] += 1
            else:
                result[str(winner)] = 1
        winner=game.winner1
        if winner:
            if str(winner) in result.keys():
                result[str(winner)] += 1
            else:
                result[str(winner)] = 1
                
        winner=game.winner2        
        if winner:
            if str(winner) in result.keys():
                result[str(winner)] += 1
            else:
                result[str(winner)] = 1
        
    return result

res=getPoint(allGames)

res1=getPoint1(allGames)

print("Normal")
for k in sorted(res,key=res.get,reverse=True):
    print(k,res[k])
            
print('1 point for win in game and any time')
for k in sorted(res1, key=res1.get, reverse=True):
    print(k, res1[k])



