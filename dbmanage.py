from tinydb import TinyDB, Query


class DbManager:
    def __init__(self):
        self.db = TinyDB('players.json')
        self.query = Query()

    def insert_to_db(self, player):
        ser_p1 = {
            'lname': player.lastName.lower(),
            'fname': player.firstName.lower(),
            'bdate': player.bDay,
            'genre': player.genre,
            'elo': player.elo
        }
        search1 = self.db.search((self.query.lname == player.lastName.lower())
                            & (self.query.fname == player.firstName.lower())
                            & (self.query.bdate == player.bDay))

        if not search1:
            self.db.insert(ser_p1)
            print('inserted')
        else:
            print('not inserted')

    def modify_elo(self, player):
        self.db.search(self.query.lname == player.lastName.lower())

    def reports(self, player):
        self.db.search(self.query.lname == player.lastName.lower())