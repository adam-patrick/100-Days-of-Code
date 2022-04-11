# ################### Mother Fucking Scope, Beeyach! ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #local scope
# potion_strength = 1
# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength)
# #print (potion_strength) gives a Not Defined error

# #Global Scope
# player_health = 10
# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)
#   drink_potion()

# print(player_health)

# # There is no Block Scope

# # game_level = 3
# # enemies = ["Skeleton", "Zombie", "Alien" ]
# # if game_level < 5:
# #   new_enemy = enemies[0]
# # print(new_enemy)

# #Modifying Global Scope

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

#naming convention for variables one wants unchanged is to keep ALL UPPERCASE
PI = 3.14159
URL = "http://www.google.com"
TWITTER_HANDLE = "@that_dirty_sumbitch"