import random
import math
from pokemon import *
from type import *
from attack import *
from battle import *

class AI():


    def __init__(self, mode):
        self.mode = mode
        self.maxpwr = 180
        self.lvlweight = 0.2   #pesos que mostram quanto vale cada stats
        self.maxweight = 0.35  #na hora do battlechance (somam 1.0)
        self.meanweight = 0.3
        self.spdweight = 0.05
        self.hpweight = 0.1
        
        #dano esperado de cada ataque disponível
    def getExpectedDmg(self, atker, atk, defender):
        power = atk.pwr / self.maxpwr
        if power > 1 : power = 1
        accu = atk.accu / 100
        mult = getMultiplier(atker, atk.typ, defender) / 6
        
        score = (power * mult * accu) 
        
        return score
        
        #escolha do atk de acordo com o modo ativado
    def chooseAtk(self, atker, defender, accu):
        
        atkScores = []
        if self.mode == "safe":
            minAccu = 100
        elif self.mode == "risky":
            minAccu = accu
        else: 
            minAccu = 0
        
        for atk in atker.atks :
            dmg = 0
            if atk.pp > 0 and atk.accu >= minAccu:
                dmg = self.getExpectedDmg(atker, atk, defender)
                print("dano do atk " + atk.name + " eh " + str(dmg))
            atkScores.append(dmg)
            
        choice = atkScores.index(max(atkScores))
       
        return choice
       
       #calculo da chance de batalha, o que faz possivelmente alterar o modo de
       # luta
    def calculateBattleChance(self, atker, defender):
        atksPwr = []
        for atk in atker.atks :
            if atk.pp > 0:
                atksPwr.append(self.getExpectedDmg(atker, atk, defender))
        
        hpratio = (atker.hp / defender.hp)
        if hpratio >= 5 : hpratio = self.hpweight
        else : hpratio = self.hpweight * hpratio / 5 
        
        levelratio = (atker.level / defender.level) / 100
        if levelratio >= 0.4 : self.lvlweight = 0.2
        else : levelratio = self.lvlweight * levelratio / 0.4
        
        speedratio = atker.spd / 512
        if speedratio >= 0.4 : speedratio = self.spdweight
        else : speedratio = self.spdweight * speedratio / 0.4
        
        maxpwr = self.maxweight * max(atksPwr)
        meanpwr = self.meanweight * sum(atksPwr) / float(len(atksPwr))
        
        print("Status do " + atker.name)
        print("level ratio: " + str(100*levelratio))
        print("maxpwr: " + str(100*maxpwr))
        print("hpratio: " + str(100*hpratio))
        print("meanpwr: " + str(100*meanpwr))
        print("speedratio: " + str(100*speedratio))
        chanceSum = 100 * (hpratio + levelratio + speedratio + maxpwr + meanpwr)
        
        return chanceSum
        
    def changeBattleMode(self, atker, defender):
        chanceScore = self.calculateBattleChance(atker, defender)
        if (chanceScore >= 25): mode = "safe"
        elif (chanceScore >= 15): mode = "risky"
        else : mode = "allin"
        
        self.mode = mode
        print("\nScore: " + str(chanceScore) + " - " + mode + " ativado!\n")
   
        
        

