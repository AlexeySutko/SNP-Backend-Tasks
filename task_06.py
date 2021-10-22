

class WrongNumberOfPlayersError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "WrongNumberOfPlayersError"

class NoSuchStrategyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "NoSuchStrategyError"



def rps_game_winner(players):
    if isinstance(players, list):
        numOfPlayersErr = "WrongNumberOfPlayersError"
        if len(players) == 2:
            strategyErr = "NoSuchStrategyError"
            choices = "rpsRPS"
            player1 = players[0]
            player2 = players[1]

            chose_list = []
            chose_list.append(player1[1])
            chose_list.append(player2[1])

            chose = ''.join(chose_list)

            if player1[1] in choices and player2[1] in choices:
                if chose.lower() == "pp" or chose.lower() == "ss" or chose.lower() == "rr":
                    return player1
                elif chose.lower() == "rs" or chose.lower() == "pr" or chose.lower() == "sp":
                    return player1
                elif chose.lower() == "sr" or chose.lower() == "rp" or chose.lower() == "ps":
                    return player2

            else:
                return strategyErr
        else:
            return numOfPlayersErr

    else:
        print("Wrong input")


print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'r']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'p']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'a']]))