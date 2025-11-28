import random;

dic = {'r':'Rock', 'p':'Paper', 's':'Scissor'};
c = tuple(dic.keys());

def get_user_choice():
   while True:
    choice = input('Rock, Paper, or Scissor? (r/p/s): ').lower(); 
    if choice in c:
      return choice;
    else:
      print('Invalid choice !');

def display_choices(user_choice,comp_choice):
   print(f'You chose {dic[user_choice]}');
   print(f'You chose {dic[comp_choice]}');

def winner(user_choice,comp_choice):
   if user_choice == comp_choice:
    print('draw !!');
   elif ( 
    (user_choice == 'r' and comp_choice == 's') or 
    (user_choice == 's' and comp_choice == 'p') or 
    (user_choice == 'p' and comp_choice == 'r') ):
      print('You win !!');
   else:
      print('You lose !!');

def play_game():
 while True:
  user_choice = get_user_choice();

  comp_choice = random.choice(c);

  display_choices(user_choice,comp_choice);

  winner(user_choice,comp_choice)

  user = input("Enter 'n' to quit: ").lower();
  if user == 'n':
    print('Well Played !');
    break;
  else:
    continue;

play_game();