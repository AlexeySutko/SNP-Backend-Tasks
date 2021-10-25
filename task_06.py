

class WrongNumberOfPlayersError(Exception):
    def __init__(self, message = "WrongNumberOfPlayersError"):
        self.message = message

class NoSuchStrategyError(Exception):
    def __init__(self, message = "NoSuchStrategyError"):
        self.message = message


def rps_game_winner(players):
    if isinstance(players, list):
        if len(players) == 2:
            choices = "rpsRPS"
            player1 = players[0]
            player2 = players[1]
            strPlayer1 = " ".join(player1)
            strPlayer2 = " ".join(player2)

            chose_list = []
            chose_list.append(player1[1])
            chose_list.append(player2[1])

            chose = ''.join(chose_list)

            if player1[1] in choices and player2[1] in choices:
                if chose.lower() == "pp" or chose.lower() == "ss" or chose.lower() == "rr":
                    return strPlayer1
                elif chose.lower() == "rs" or chose.lower() == "pr" or chose.lower() == "sp":
                    return strPlayer1
                elif chose.lower() == "sr" or chose.lower() == "rp" or chose.lower() == "ps":
                    return strPlayer2

            else:
                raise NoSuchStrategyError()
        else:
            raise WrongNumberOfPlayersError()

    else:
        print("Wrong input")


print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'r']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'p']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'a']]))