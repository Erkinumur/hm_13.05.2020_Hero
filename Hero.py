import random

class Hero:
    def __init__(self, team):
        self.team = team['name']
        team['hero'] = self
        self.id = next(hero_id)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Hero's level in {self.team} team is up!")


class Soldier:
    def __init__(self, team):
        self.team = team['name']
        team['soldiers'].append(self)
        self.id = next(soldier_id)
    
    def follow_hero(self, hero):
        self.folowing = hero
        print(f'Soldier(id={self.id}) follows hero(id={hero.id})')

hero_id = (i for i in range(1, 100))
soldier_id = (i for i in range(1, 100))


red_team = {'name': 'red', 'hero': '' , 'soldiers': [] }
blue_team = {'name': 'blue', 'hero': '' , 'soldiers': [] }

hero1 = Hero(red_team)
hero2 = Hero(blue_team)

for i in range(51):
    team = random.choice([red_team, blue_team])
    Soldier(team)

red_soldiers = len(red_team['soldiers'])
blue_soldiers = len(blue_team['soldiers'])

print('Soldiers in red team: ', red_soldiers)
print('Soldiers in blue team: ', blue_soldiers)

if red_soldiers > blue_soldiers:
    red_team['hero'].level_up()
else:
    blue_team['hero'].level_up()

red_team['soldiers'][random.randint(0, red_soldiers - 1)].follow_hero(red_team['hero'])



