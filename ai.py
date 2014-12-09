import random
import math
from pokemon import *
from type import *
from attack import *
from battle import *

class AI():


    def __init__(self, mode="safe"):
        '''pesos mostram a importancia de
        cada stat na hora do battlechance (somam 1)'''
        self.mode = mode
        self.maxpwr = 180
        self.lvlweight = 0.2   
        self.maxweight = 0.35  
        self.meanweight = 0.3
        self.spdweight = 0.05
        self.hpweight = 0.1
        
    def set_up(self, atker, defender):
        atks_pwr = []
        for atk in atker.atks :
            if atk.pp > 0:
                atks_pwr.append(self.get_expected_dmg(atker, atk, defender))
        self.maxpwr = self.maxweight * max(atks_pwr)
        self.meanpwr = self.meanweight * sum(atks_pwr) / float(len(atks_pwr))
        self.levelratio = (atker.level / defender.level) / 100
        if self.levelratio >= 0.4 : self.levelratio = self.lvlweight
        else : self.levelratio = self.lvlweight * self.levelratio / 0.4
        self.speedratio = atker.spd / 512
        if self.speedratio >= 0.4 : self.speedratio = self.spdweight
        else : self.speedratio = self.spdweight * self.speedratio / 0.4
        

    def get_expected_dmg(self, atker, atk, defender):
        '''calcula o dano esperado do ataque atk 
        no defender'''
        power = atk.pwr / self.maxpwr
        if power > 1 : power = 1
        accu = atk.accu / 100
        mult = getMultiplier(atker, atk.typ, defender) / 6
        
        score = (power * mult * accu) 
        
        return score
        
    def choose_atk(self, atker, defender, accu):
        '''determina o ataque a ser escolhido a partir
        do modo ativado'''
        atk_scores = []
        if self.mode == "safe":
            min_accu = 100
        elif self.mode == "risky":
            min_accu = accu
        else: 
            min_accu = 0
        
        for atk in atker.atks :
            dmg = 0
            if atk.pp > 0 and atk.accu >= min_accu:
                dmg = self.get_expected_dmg(atker, atk, defender)
                print("dano do atk " + atk.name + " eh " + str(dmg))
            atk_scores.append(dmg)
            
        choice = atk_scores.index(max(atk_scores))
       
        return choice
       
    def calculate_battle_chance(self, atker, defender):
        '''calculo da chance de batalha, o que pode fazer alterar
        o modo de luta da AI'''
                
        hpratio = (atker.hp / defender.hp)
        if hpratio >= 5 : hpratio = self.hpweight
        else : hpratio = self.hpweight * hpratio / 5 
        
        print("Status do " + atker.name)
        print("level ratio: " + str(100*self.levelratio))
        print("maxpwr: " + str(100*self.maxpwr))
        print("hpratio: " + str(100*hpratio))
        print("meanpwr: " + str(100*self.meanpwr))
        print("speedratio: " + str(100*self.speedratio))
        chance_sum = 100 * (hpratio + self.levelratio + self.speedratio + self.maxpwr + self.meanpwr)
        
        return chance_sum
        
    def change_battle_mode(self, atker, defender):
        chance_score = self.calculate_battle_chance(atker, defender)
        if (chance_score >= 15): mode = "safe"
        elif (chance_score >= 10): mode = "risky"
        else : mode = "allin"
        
        self.mode = mode
        print("\nScore: " + str(chance_score) + " - " + mode + " ativado!\n")
   
        
        

