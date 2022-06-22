import random
 
class NumberValidator:
  number = 0
 
  def get(self, low, high):
    ready = False
    user_input = 0
    
    while (not ready):
      user_input = int(input('Higher or lower? [h/1] '))
 
      if user_input in range(1, 14):
        ready = True
      else:
        print('Not in range')
    
    return user_input
 
class CardGame:
  player_number = 0
  score = 0
 
  def print_player_number(self):
    print(self.player_number)
 
  def get_random_number(self):
    pass
 
  def check_number(self):
    pass
 
  def start(self):
    dealer_number = random.randint(1, 13)
    print(f'The card is: {dealer_number}')
 
    validator = NumberValidator()
    user_number = validator.get(0, 20)
    print(user_number)
 
def main():
  game = CardGame()
  game.start()
 
main()
 




