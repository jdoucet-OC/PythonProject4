import classes
import dbmanage
import time
# players = []
# specs = 'CEC', 'Berlin', '18/03/2021', 'Bullet', 'EUW WIN'
# newTournament = classes.Tournament(specs)
dbmanager = dbmanage.PlayerDbManager()
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
    dbmanager.insert_player(pp)
