# This code was designed to imitate a typical snakes and ladders game. Players compete against one another,
# whilst the program rolls the dice, moves their positions on the board, and adjusts as they encounter
# snakes or ladders. This game can be played by any number of players. The position of the players is printed out,
# and the is also displayed on the board with a strikethrough on their numbered position.


# The module "random" is imported
import random


# Define dice rolling function
def roll_dice(player):
    # When the user presses "enter" key, a random digit between 1 and 6 will be picked
    # and the number the player rolled will be given. The number rolled will be stored for later use.
    input("Press enter to roll the dice: ")
    num_rolled = random.randint(1, 6)
    print(player + " rolled: " + str(num_rolled))
    return num_rolled


# Define function to set up board
def board_set():
    # There is a list from the number 1-100, and then it is reversed
    init = 0
    nums_on_board = list(range(1, 101))
    nums_on_board.reverse()
    # For each number in the list, the index of that number is taken and if the index is divisible by 10,
    # the next 10 numbers will be on the next line, and so on
    for x in nums_on_board:
        index_x = nums_on_board.index(x)
        if (int(index_x) + 1) % 10 == 0:
            print(nums_on_board[int(init): int(index_x + 1)])
            init = index_x + 1


# Define function to update the board each time a player rolls
def updating_board(positions):
    # An empty list is made, and there is a variable that has all numbers from 1 to 100 stored in it
    board_nums = list(range(101))
    new_list = []

    # For every number in positions, that number is added to the empty list
    for i in positions:
        if i not in new_list:
            new_list.append(i)

    # strikethrough the items from new list in the board
    for x in new_list:
        IndexToStrikeThrough = board_nums.index(x)
        board_nums[IndexToStrikeThrough] = str(board_nums[IndexToStrikeThrough]) + '\u0336'
    # The order of the board is reversed, and the numbers are set tp go into a new line after 10 numbers are down
    board_nums.reverse()
    index = 0
    while index < 100:
        print(board_nums[index:index+10])
        index += 10


# Define the function to move the players and run the game
def moving(players):
    # Defining the starting positions of the players to 0
    winner_position = 0
    players_positions = []
    for person in players:
        players_positions.append(0)

    # Define where the snakes and the ladders are. The number at the end of each list is the new position of a player
    # after they land on the first number
    snakes_ladders = [[32, 10], [36, 6], [48, 26], [62, 18], [88, 24], [95, 56], [97, 79], [1, 38], [4, 14], [8, 20],
                      [21, 42], [28, 84], [50, 67], [80, 99], [71, 92]]

    # While nobody has arrived at 100 yet, the winners position is set to whoever is at the highest number.
    while winner_position < 100:
        pl_num = 0
        winner_position = max(players_positions)
        print("Winner's position is at " + str(winner_position) + "\n")
        print("#############################")
        if winner_position == 100:
            break
        # For each player, the dice is rolled
        for player_position in players_positions:
            print(players[pl_num] + "'s position is: " + str(player_position))
            nums_moved = roll_dice(players[pl_num])
            # If the position of the player after the dice is rolled is more than 100,
            # the players position doesn't change
            if player_position + nums_moved > 100:
                print(players[pl_num] + " rolled too high. Your position remains at " + str(player_position))
            # if the position of the player after the dice rolled is not more than 100,
            # the players new position is set to the new number plus what they already were at.
            else:
                player_position += nums_moved
                # If the player lands on any of the first numbers in the list of snakes and ladders, they end up
                # at the second number. If the second number is lower than the first number, it is told to the
                # player they landed on a snake. Otherwise, it is told that they landed on a ladder.
                for x in snakes_ladders:
                    if player_position == x[0]:
                        player_position = x[1]
                        if x[0] > x[1]:
                            print("SNAKE AT " + str(x[0]) + "...")
                        else:
                            print("LADDER AT " + str(x[0]) + "...")
                # The players new position is printed
                print(players[pl_num] + "'s new position is: " + str(player_position)+"\n")
            # If a player is at 100, the code to move will stop running
            players_positions[pl_num] = player_position
            if players_positions[pl_num] == 100:
                break
            pl_num = pl_num+1
        # The update_board function is called to do the strikethroughs
        updating_board(players_positions)
    # Once someone arrived at 100, they will be called out as the winner, and the code will stop running
    print(winner_position)
    winning_player = players_positions.index(winner_position)
    print("winning player index is " + str(winning_player))
    print("The winner is " + players[winning_player])


# Stating the name and number of the players, and calling the function to move them.
players = ["Player1", "Player2"]
moving(players)
