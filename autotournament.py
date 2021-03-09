import classes
import dbmanage
# players = []
# specs = 'CEC', 'Berlin', '18/03/2021', 'Bullet', 'EUW WIN'
# newTournament = classes.Tournament(specs)

# players
player1 = classes.Player("James", "McGill", "21/12/1976", "M", 1950)
player2 = classes.Player("James", "McGales", "21/12/1976", "M", 1873)
player3 = classes.Player("Jason", "Doucet", "12/11/1997", "M", 1281)
player4 = classes.Player("Rémi", "Laroche", "09/07/1997", "M", 1281)
player5 = classes.Player("Jane", "McGill", "18/04/1947", "F", 1603)
player6 = classes.Player("Alice", "Wonderland", "21/06/1984", "F", 1551)
player7 = classes.Player("Betty", "Dove", "28/01/45", "F", 2117)
player8 = classes.Player("Nono", "Riana", "14/08/2000", "F", 2108)

players = [player1, player2, player3, player4,
           player5, player6, player7, player8]
for pp in players:
    dbmanage.insert_to_db(pp)

# Tournament
tournament = classes.Tournament("LEC", "Berlin", "21/03/2021",
                                "Bullet", "LEC en bullet à berlin, 2021")
tournament.players = players

# Round1
# Système suisse
sortedlist = sorted(players, key=lambda elosort: elosort.elo)
middle = len(sortedlist)//2
lowerhalf = sortedlist[:middle]
upperHalf = sortedlist[middle:]

tour1 = []
for ii in range(0, middle):
    tour1.append(([lowerhalf[ii], 'TBD'], [upperHalf[ii], 'TBD']))

Round1 = classes.Round("Round 1", tour1)

# j'entre les resultats, deux nuls, une victoire une défaite
results = ([1, 0], [0.5, 0.5], [0.5, 0.5], [0, 1])
# entrée des resultats du round1 en enregistré dans tournoi
for ii in range(0, middle):
    Round1.matches[ii][0][1] = results[ii][0]
    Round1.matches[ii][1][1] = results[ii][1]

tournament.tournees.append(Round1)
# Round2
# Système suisse 2 : avec points
# comparer si le tuple existe dans la liste des tournées du tournoi
scoreboard = tournament.gen_sorted_scoreboard()

tour2 = []
for ii in range(0, 8, 2):
    tour2.append(([scoreboard[ii][0], 'TBD'], [scoreboard[ii+1][0], 'TBD']))

Round2 = classes.Round("Round 2", tour2)

results = ([0, 1], [0, 1], [0.5, 0.5], [1, 0])

for ii in range(0, middle):
    Round2.matches[ii][0][1] = results[ii][0]
    Round2.matches[ii][1][1] = results[ii][1]

tournament.tournees.append(Round2)

print(tournament.gen_sorted_scoreboard())
