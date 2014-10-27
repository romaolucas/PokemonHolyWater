import random
import math
from pokemon import *
from type import *

class Battle():
    
    def allAlive(self, first, second):
        """Checa se a batalha deve continuar ou acabar"""
        if first.hp <= 0 or second.hp <= 0:
            return False
        else:
             return True

    def getFirst(self, poke1, poke2):
        """Decide qual Pokémon vai começar atacando"""
        if poke1.spd == poke2.spd:
            chance = random.randint(1, 100)
            if chance < 50:
                return poke1
            else:
                return poke2
        else:
            if poke1.spd > poke2.spd:
                return poke1
            else:
                return poke2

    def effectMessage(self, mult):
        """Gera mensagem indicando efetividade de um ataque"""
        if mult <= 0.75 and mult > 0:
            return ' e foi pouco efetivo.'
        elif mult >= 2.0:
            return ' e foi super efetivo!'
        elif mult == 0:
            return ' e não foi efetivo!'
        else:
            return '.'

    def getLuck(self):
        """Calcula o fator aleatório a ser usado na fórmula de dano"""
        luck = random.randint(217, 255)
        luck = luck * 100
        luck = luck / 255
        luck = luck / 100
        return luck

    def willHit(self, accu):
        """Determina se um ataque vai acertar ou errar"""
        chance = random.uniform(1, 100)
        if chance <= accu:
            return True
        else:
            return False

    def getCrit(self, speed, level):
        """Determina o multiplicador de critical hit"""
        critRate = speed * 100 / 512
        chance = random.uniform(1, 100)
        if chance <= critRate:
            return (2 * level + 5) / (level + 5)
        else:
            return 1.0

    def getDmg(self, active, defender, atk, typeMult, crit):
        """
        Determina o dano que um ataque de um Pokémon vai causar
        em outro Pokémon
        """
        luck = self.getLuck()

        if not atk.special:
            offensiveStat = active.atk
            defensiveStat = defender.dfs
        else:
            offensiveStat = active.spc
            defensiveStat = defender.spc
        
        # cálculo do baseDmg
        baseDmg = ((((2 * active.level) + 10) / 250) * (offensiveStat /
                                        defensiveStat) * (atk.pwr)) + 2

        return math.floor(crit * baseDmg * typeMult * luck)


    def battle(self, first, second):
        """Executa o laço da batalha."""

        # determina primeiro quem começa
        active = self.getFirst(first, second)
        if active is first:
            defender = second
        else:
            defender = first
        
        result = True

        # laço da batalha
        while result is True:
            
            struggle = False

            print('\nVez do ' + active.name + ', HP: ' + str(int(active.hp)) +
                    '/' + str(int(active.maxhp)) + ', LVL: ' + str(active.level))
            
            active.showAtks()
            choice = input('Escolha o ataque de seu pokemon (1-' + 
                            str(len(active.atks)) + ').\n'
                            'Ou, para ver mais informações, digite +:\n')

            if choice == '+':
                print('')
                active.showStats()
                active.showAtks(True)
                choice = input('\nEscolha o ataque de seu Pokémon (1-' + 
                                str(len(active.atks)) + ').\n')
                
            try:
                choice = int(choice) - 1

            except ValueError:
                choice = -1


            if active.hasToStruggle():
                struggle = True

            # processamento da escolha
            if not (choice in [0, 1, 2, 3]):
                print('Escolha de ataque inválida!')
                continue
            elif choice in [0, 1, 2, 3] and len(active.atks) < choice + 1:
                print('Espaço vazio, escolha outro ataque!')
                continue
            elif active.atks[choice].pp <= 0 and not struggle:
                print('Sem PP para usar esse ataque!')
                continue
            
            # efeitos da escolha
            else:

                if struggle:
                    attack = Attack('Struggle', Type(0), 100, 50, 10)
                else:
                    attack = active.atks[choice]
                    attack.pp -= 1

                typeMult = getMultiplier(active, attack.typ, defender)
                crit = self.getCrit(active.spd, active.level)
                
                critMsg = ''
                if crit != 1.0:
                    critMsg = ' Foi um ataque crítico!!'
                
                dmg = self.getDmg(active, defender, attack, typeMult, crit)

                if struggle:
                    print(active.name + ' não tem mais nenhum ataque sobrando.')

                if self.willHit(attack.accu):
                    defender.hp -= dmg
                    print(active.name + ' usou ' + attack.name +
                            self.effectMessage(typeMult) + critMsg)

                else:
                    print(active.name + ' usou ' + attack.name + ' e errou.')

                if struggle:
                    active.hp -= dmg / 2
                    print(active.name + ' tomou dano de recoil.')

            # troca de turno
            if active is first:
                active = second
                defender = first
            else:
                active = first
                defender = second
            result = self.allAlive(first, second)

        # fim da batalha
        print('\n' + active.name + ' desmaiou! ' + defender.name + 
            ' ganhou a luta!\n')