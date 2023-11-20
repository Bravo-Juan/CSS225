# Juan Bravo
# 11/19/23

# Checks whether the game character can complete a certain task according to the items they have picked up and the debuff they have.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

def task_performance(player):

    # Stores the available tasks along with the items each one requires and the debuff that the player must not have.
    tasks = {"Climb a mountain": {"items_required": ["rope", "coat", "first aid kit"], "unrequired_debuff": "slow"},
             "Cook a meal": {"items_required": ["pan", "groceries"], "unrequired_debuff": "small"},
             "Write a book": {"items_required": ["pen", "paper", "idea"], "unrequired_debuff": "confusion"}}

    # Loops through each task along with its details.
    for task, details in tasks.items():
        needed_items = details["items_required"]
        unneeded_debuff = details["unrequired_debuff"]

        # Checks if the player has all of the needed items and doesn't have the unrequired debuff.
        listed_items = all(item in player.weapons for item in needed_items)
        listed_debuff = unneeded_debuff not in player.weaknesses

        # Informs the player if they can complete a certain task or not along with the reasoning why they can't.
        if listed_items and listed_debuff:
            print("{} can complete '{}'.".format(player.nickname, task))
        elif not listed_items:
            print("{} does not have the right items to '{}'.".format(player.nickname, task))
        else:
            print("{} cannot '{}' due to having the '{}' debuff.".format(player.nickname, task, unneeded_debuff))

task_performance(player1)