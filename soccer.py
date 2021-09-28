import random as rnd
import datetime as dt
from collections import defaultdict as dd

from dataclasses import dataclass,field

class Team:
    def __init__(self,name,location,force=None) -> None:
        self.name=name
        self.location=location
        if force:
            self.force=force
        else:
            self.force=rnd.randint(50,99)
        self.results=dd(int)
            
    def __repr__(self):
        return f'{self.name} ({self.location}) -> {self.force}'
    
    
    def __str__(self):
        return f'{self.name} ({self.location})'
    
    
@dataclass()
class Game:
    home:Team
    away:Team
    completed: bool=False
    
    
    
    @property
    def score(self):
        return (self.hg1+self.hg2,self.ag1+self.ag2)

    @property
    def score1(self):
        return (self.hg1, self.ag1)

    @property
    def score2(self):
        return (self.hg2,self.ag2)
    
    @property
    def winner(self):
        if not self.completed:
            return None
        if self.score[0]>self.score[1]:
            return self.home
        elif self.score[0]<self.score[1]:
            return self.away
        else:
            return None 
        
    @property
    def looser(self):
        if not self.completed:
            return None
        if self.score[0] > self.score[1]:
            return self.away
        elif self.score[0] < self.score[1]:
            return self.home
        else:
            return None
        
    @property
    def winner1(self):
        if not self.completed:
            return None
        if self.score1[0] > self.score1[1]:
            return self.home
        elif self.score1[0] < self.score1[1]:
            return self.away
        else:
            return None
    
    @property
    def looser1(self):
        if not self.completed:
            return None
        if self.score1[0] > self.score1[1]:
            return self.away
        elif self.score1[0] < self.score1[1]:
            return self.home
        else:
            return None

    
        
    @property
    def winner2(self):
        if not self.completed:
            return None
        if self.score2[0] > self.score2[1]:
            return self.home
        elif self.score2[0] < self.score2[1]:
            return self.away
        else:
            return None
    
    @property
    def looser2(self):
        if not self.completed:
            return None
        if self.score2[0] > self.score2[1]:
            return self.away
        elif self.score2[0] < self.score2[1]:
            return self.home
        else:
            return None

    
    @property
    def hg1(self):
        if self.completed:
            return len(list(filter(lambda z: z["minute"]<45 and z['goal']=='home',self.goals)))

    @property
    def hg2(self):
        if self.completed:
            return len(list(filter(lambda z: z["minute"] > 45 and z['goal'] == 'home', self.goals)))
        
    @property
    def ag1(self):
        if self.completed:
            return len(list(filter(lambda z: z["minute"] < 45 and z['goal'] == 'away', self.goals)))
        return 0

    @property
    def ag2(self):
        if self.completed:
            return len(list(filter(lambda z: z["minute"] > 45 and z['goal'] == 'away', self.goals)))
        return 0
    
    def clear(self):
        self.completed=False
        self.goals=[]
        
    def play(self):
        if self.completed:
            return
        homeBonus=self.home.force//5
        sumForce=homeBonus+self.home.force+self.away.force
        self.goals=[]
        for minute in range(1,90):
            rm=rnd.randint(1,100)
            if rm >96:
                rt=rnd.randint(0,sumForce)
                if rt<self.away.force:
                    self.goals.append({'minute':minute,'goal':'away'})
                else:
                    self.goals.append({'minute': minute, 'goal': 'home'})
        self.completed=True
        if self.winner:
            self.winner.results['games']+=1
            self.looser.results['games'] += 1
            self.winner.results['wins']+=1
            self.looser.results['lost']+=1
        else:
            self.home.results['games']+=1
            self.away.results['games'] += 1
            self.home.results['draw']+=1
            self.away.results['draw'] += 1
        self.home.results['goalsIn']+=self.score[0]
        self.away.results['goalsIn'] += self.score[1]
        self.home.results['goalsOut'] += self.score[1]
        self.away.results['goalsOut'] += self.score[0]

    def __repr__(self) -> str:
        if self.completed:
            ret=f'{self.home} - {self.away} \n'
            ret+=f'{self.score} ({self.score1}) \n'
        else:
            ret = f'{self.home} - {self.away} not played\n'
        return ret
