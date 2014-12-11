import random
import math
from pokemon import *
from type import *
from ai import *

class Battle():
    
    def all_alive(self, first, second):
        """Checa se a batalha deve continuar ou acabar"""
        if first.hp <= 0 and second.hp <= 0:
            print('Ambos os pokémon desmaiaram! Empate!')
            first.hp = second.hp = 0

            return False

        elif first.hp <= 0:
            print('\n' + first.name + ' desmaiou! ' +
                  second.name + ' ganhou a luta!\n')
            first.hp = 0

            return False

        elif second.hp <= 0:
            print('\n' + second.name + ' desmaiou! ' +
                  first.name + ' ganhou a luta!\n')
            second.hp = 0

            return False

        return True

    def get_first(self, poke1, poke2):
        """Decide qual Pokémon vai começar atacando"""
        if poke1.spd == poke2.spd:
            chance = random.randint(0, 100)
            if chance < 50:
                return poke1
            else:
                return poke2
        else:
            if poke1.spd > poke2.spd:
                return poke1
            else:
                return poke2

    def effect_message(self, mult):
        """Gera mensagem indicando efetividade de um ataque"""
        if mult <= 0.75 and mult > 0:
            return ' e foi pouco efetivo.'
        elif mult >= 2.0:
            return ' e foi super efetivo!'
        elif mult == 0:
            return ' e não foi efetivo!'
        else:
            return '.'

    def get_luck(self):
        """Calcula o fator aleatório a ser usado na fórmula de dano"""
        luck = random.randint(217, 255)
        luck = luck * 100
        luck = luck / 255
        luck = luck / 100
        return luck

    def will_hit(self, accu):
        """Determina se um ataque vai acertar ou errar"""
        chance = random.uniform(1, 100)
        if chance <= accu:
            return True
        else:
            return False

    def get_crit(self, speed, level):
        """Determina o multiplicador de critical hit"""
        crit_rate = speed * 100 / 512
        chance = random.uniform(1, 100)
        if chance <= crit_rate:
            return (2 * level + 5) / (level + 5)
        else:
            return 1.0

    def get_dmg(self, active, defender, atk, type_mult, crit):
        """
        Determina o dano que um ataque de um Pokémon vai causar
        em outro Pokémon
        """
        luck = self.get_luck()

        if not atk.special:
            offensive_stat = active.atk
            defensive_stat = defender.dfs
        else:
            offensive_stat = active.spc
            defensive_stat = defender.spc
        
        # cálculo do baseDmg
        base_dmg = ((((2 * active.level) + 10) / 250) * (offensive_stat /
                                        defensive_stat) * (atk.pwr)) + 2

        return math.floor(crit * base_dmg * type_mult * luck)


    def make_choice(self, poke, poke_oponente, ai=None):
        
        #comportamento com AI
        if (ai != None):
            ai.change_battle_mode(poke, poke_oponente)
            choice = ai.choose_atk(poke, poke_oponente, 70)
            return choice
            
        #comportamento sem AI
        print('\nAdversário: ' + poke_oponente.name + ', HP: ' + str(int(poke_oponente.hp)) +
                '' + ', LVL: ' + str(poke_oponente.level))
        print('\nVez do ' + poke.name + ', HP: ' + str(int(poke.hp)) +
                '' + ', LVL: ' + str(poke.level))

        poke.show_atks()
        choice = input('Escolha o ataque de seu pokemon (1-' + 
                        str(len(poke.atks)) + ').\n'
                        'Ou, para ver mais informações, digite +:\n')

        if choice == '+':
            print('')
            poke.show_stats()
            poke.show_atks(True)
            choice = input('\nEscolha o ataque de seu Pokémon (1-' + 
                            str(len(poke.atks)) + ').\n')
            
        try:
            choice = int(choice) - 1

        except ValueError:
            choice = -1

        return choice

    def attack(self, first, second, choice = None):
        """Executa o laço da batalha."""
    
        struggle = False
        
        if first.has_to_struggle():
            struggle = True

        if choice == None:

            choice = self.make_choice(first, second)

            success = False

            while not success:
            # processamento da escolha
                if not (choice in [0, 1, 2, 3]):
                    print('Escolha de ataque inválida!')
                    choice = self.make_choice(first)

                elif choice in [0, 1, 2, 3] and len(first.atks) < choice + 1:
                    print('Espaço vazio, escolha outro ataque!')
                    choice = self.make_choice(first)

                elif first.atks[choice].pp <= 0 and not struggle:
                    print('Sem PP para usar esse ataque!')
                    choice = self.make_choice(first)

                else:
                    success = True

        
        # efeitos da escolha

        if struggle:
            attack = Attack('Struggle', Type(0), 100, 50, 10)
        else:
            attack = first.atks[choice]
            attack.pp -= 1

        type_mult = get_multiplier(first, attack.typ, second)
        crit = self.get_crit(first.spd, first.level)
        
        crit_msg = ''
        if crit != 1.0:
            crit_msg = ' Foi um ataque crítico!!'
        
        dmg = self.get_dmg(first, second, attack, type_mult, crit)

        if struggle:
            print(first.name + ' não tem mais nenhum ataque sobrando.')

        if self.will_hit(attack.accu):
            second.hp -= dmg
            print(first.name + ' usou ' + attack.name +
                    self.effect_message(type_mult) + crit_msg)

        else:
            print(first.name + ' usou ' + attack.name + ' e errou.')

        if struggle:
            first.hp -= math.floor(dmg / 2)
            print(first.name + ' tomou dano de recoil.')