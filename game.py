# Tic Tac Toe

board_slots = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
winning_combinations = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]

# Game state: [turn_count, current_player_symbol, is_game_over]
game_state = [0, 0, False] 

def start_game():
  print("Welcome to Tic Tac Toe!\n")

def show_board():
  print(f" {board_slots[1]} | {board_slots[2]} | {board_slots[3]} ")
  print("---+---+---")
  print(f" {board_slots[4]} | {board_slots[5]} | {board_slots[6]} ")
  print("---+---+---")
  print(f" {board_slots[7]} | {board_slots[8]} | {board_slots[9]} ")
  print()

def play_turn(player_num, player_symbol):
  game_state[1] = player_num

  valid_input = False
  print(f"Player {player_num}'s turn.")
  
  while not valid_input:
    user_input = input(f"Choose a box (1-9) for ({player_symbol}): ")
    
    # Input Validation
    if not (user_input.isdigit() and 1 <= int(user_input) <= 9):
      print("\nPlease enter a valid number (1-9).")
    elif board_slots[int(user_input)] in ['X', 'O']:
      print("\nThat box is already taken.")
    else:
      board_slots[int(user_input)] = player_symbol
      valid_input = True
      game_state[0] += 1
      print()
      show_board()
      check_game_over()

def check_game_over():
  # Check for winner
  for combo in winning_combinations:
    if board_slots[combo[0]] == board_slots[combo[1]] == board_slots[combo[2]] != '':
      print("Tic Tac Toe!")
      print(f"Player {game_state[1]} Wins!")
      game_state[2] = True

  # Check for draw
  if game_state[0] == 9 and game_state[2] == False:
    print("It's a Draw!")

# Main Loop
start_game()
show_board()

while game_state[0] < 9:
  if game_state[2] == True:
    break
  play_turn(1, 'X')
  
  if game_state[0] == 9 or game_state[2] == True:
    break
  play_turn(2, 'O')