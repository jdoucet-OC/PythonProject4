from tinydb import TinyDB, Query
import classes


class DbManager:
    def __init__(self):
        self.db = TinyDB('players.json')
        self.query = Query()
        self.playersTable = self.db.table('players')
        self.demoPlayerTable = self.db.table('demo')

    def insert_to_db(self, player):
        ser_p1 = {
            'lname': player.lastName.lower(),
            'fname': player.firstName.lower(),
            'bdate': player.bDay,
            'genre': player.genre,
            'elo': player.elo
        }
        search1 = self.playersTable.search((self.query.lname == player.lastName.lower())
                                           & (self.query.fname == player.firstName.lower())
                                           & (self.query.bdate == player.bDay))

        if not search1:
            self.playersTable.insert(ser_p1)
            print('inserted')
        else:
            print('not inserted')

    def modify_elo(self, player):
        self.playersTable.search(self.query.lname == player.lastName.lower())

    def reports(self, player):
        self.playersTable.search(self.query.lname == player.lastName.lower())

    def return_demo(self):
        playerlist = []
        for player in self.demoPlayerTable.all():
            lname = player['lname'].capitalize()
            fname = player['fname'].capitalize()
            bdate = player['bdate']
            genre = player['genre']
            elo = player['elo']
            playerlist.append(classes.Player(lname, fname, bdate,
                                             genre, elo))
        return playerlist
