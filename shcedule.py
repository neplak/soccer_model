import random as rnd
from soccer import Team, Game
from collections import namedtuple
from loadsave import loadTeams,saveTeams


class record(namedtuple('record', ['team', 'games', 'points',
                                   'wins', 'draw', 'loss',
                                   'gf', 'ga'])):
    def __gt__(self,other):
        if self.points!=other.points:
            return self.points>other.points
        if self.wins!=other.wins:
            return self.wins>other.wins
        if (self.gf-self.ga) != (other.gf-other.ga):
            return (self.gf-self.ga) > (other.gf-other.ga)
        if self.gf!= other.gf:
            return self.gf>other.gf
        
        return self.team > other.team
    
    def __lt__(self, other) -> bool:
        if self.points != other.points:
            return self.points < other.points
        if self.wins != other.wins:
            return self.wins < other.wins
        if (self.gf-self.ga) != (other.gf-other.ga):
            return (self.gf-self.ga) < (other.gf-other.ga)
        if self.gf != other.gf:
            return self.gf < other.gf

        return self.team < other.team

    def __eq__(self,other):
        return self.team==other.team
    
    
    def __str__(self):
        ret=f'{self.team:<40} {self.games:<3} {self.points:<3} {self.wins:<3} {self.draw:<3} {self.loss:<3} {self.gf:<4} {self.ga:<4}'
        return ret

class GameSchedule:
    def __init__(self,teamList):
        self.teams=len(teamList)
        self.matchDays=[]
        self.teamList=teamList
        self.toursPlayed=[]
        
    @property
    def lastTour(self):
        return len(self.toursPlayed)
    
    def  currentTable(self,pointsForGame):
        ret={}
        
        # team results table initialization 
        for team in self.teamList:
            ret[str(team)]={
                'games':0,
                'points':0,
                'wins':0,
                'draw':0,
                'loss':0,
                'gf':0,
                'ga':0
                
            }
        #fill table of results
        for tour in self.toursPlayed:
            for game in tour:
                home=str(game.home)
                away=str(game.away)
                score=game.score
                ret[home]['games']+=1
                ret[away]['games'] += 1
                ret[home]['gf'] += score[0]
                ret[away]['gf'] += score[1]
                ret[home]['ga'] += score[1]
                ret[away]['ga'] += score[0]
                if score[0]==score[1]:
                    ret[home]['draw']+=1
                    ret[away]['draw'] += 1
                if score[0] > score[1]:
                    ret[home]['wins'] += 1
                    ret[away]['loss'] += 1
                if score[0] < score[1]:
                    ret[home]['loss'] += 1
                    ret[away]['wins'] += 1
                pts=pointsForGame(game)
                ret[home]['points']+=pts[0]
                ret[away]['points'] += pts[1]
        res=[]
        
        for key in ret:
            res.append(record(key,ret[key]['games'],ret[key]['points'],
                           ret[key]['wins'],ret[key]['draw'],
                               ret[key]['loss'],
                               ret[key]['gf'],
                               ret[key]['ga']))
        return sorted(res,reverse=True)
                
    def generateRound(self):
        if self.lastTour:
            return 
        homes=[i for i in range(0,self.teams//2)]
        guests=[i for i in range(self.teams//2,self.teams)]
        round1=[]
        for k in range(self.teams-1):
            round1.append(list(zip(homes,guests)))
            guests.insert(0,homes.pop(1))
            homes.append(guests.pop())
        rnd.shuffle(round1)
        guests = [i for i in range(0, self.teams//2)]
        homes = [i for i in range(self.teams//2, self.teams)]
        round2 = []
        for k in range(self.teams-1):
            round2.append(list(zip(homes, guests)))
            guests.insert(0, homes.pop(1))
            homes.append(guests.pop())
        rnd.shuffle(round2)
        self.matchDays=[]
        self.matchDays=round1+round2
        
        
    def nextTour(self):
        tour=self.lastTour
        games=self.matchDays[tour]
        tourResults=[]
        for game in games:
            tourResults.append(
                Game(self.teamList[game[0]], self.teamList[game[1]]))
        for game in tourResults:
            game.play()
        self.toursPlayed.append(tourResults)
        
    def info(self):
        count=1
        for day in self.matchDays:
            tDay=[]
            for game in day:
                tDay.append(Game(self.teamList[game[0]], self.teamList[game[1]]))
                    
            print(f'{count}->{tDay}')
            count+=1
            
    def infoPlayed(self):
        counter=1
        for tour in self.toursPlayed:
            print(f'{counter}->{tour}')
            counter+=1
            print('*'*10)

teams = [Team('Zenit', 'SPB',95),
         Team('CSKA', 'Moscow',70),
         Team('Spartak', 'Moscow',80),
         Team('Lokomotiv', 'Moscow',85),
         Team('Dinamo', 'Moscow',82),
         Team('Khimki', 'Khimki',60),
         Team('Krasnodar', 'Krasnodar',70),
         Team('Sochi', 'Sochi',72),
         Team('Rubin', 'Kazan',65),
         Team('Akhmat', 'Groznyy',59),
         Team('Nizhniy Novgorod', 'Nizhniy Novgorod',50),
         Team('Krylya Sovetov', 'Samara',50),
         Team('Arsenal', 'Tula',55),
         Team('Ufa', 'Ufa',57),
         Team('Rostov', 'Rostov',55),
         Team('Ural', 'Ekaterinburg',55)]

saveTeams('data\\rfpl.json',teams)

sch=GameSchedule(teams)
sch.generateRound()
#sch.info()

#sch.nextTour()
#sch.nextTour()
#sch.infoPlayed()
#print(sch.teamList[3],sch.teamList[3].results)
def pfg(game):
    score=game.score
    if score[0]>score[1]:
        return 3,0
    if score[0]<score[1]:
        return 0,3
    if score[0]==score[1]:
        return 1,1
    

for i in range(30):
    sch.nextTour()
    print(sch.toursPlayed[-1][1])    
table=sch.currentTable(pfg)

for line in table:
    print(line)
    
   
#t1=loadTeams("data\\rfpl.json")
#print(t1)
