from tinydb import TinyDB, Query
import classes


class PlayerDbManager:
    """"""
    def __init__(self):
        """"""
        self.db = TinyDB('players.json')
        self.query = Query()
        self.playersTable = self.db.table('players')
        self.demoPlayerTable = self.db.table('demo')

    def insert_player(self, player):
        """
        :param player:
        :return:
        """
        ser_p1 = {
            'lname': player.lastName.lower(),
            'fname': player.firstName.lower(),
            'bdate': player.bDay,
            'genre': player.genre,
            'elo': player.elo
        }
        cond1 = (self.query.lname == player.lastName.lower())
        cond2 = (self.query.fname == player.firstName.lower())
        cond3 = (self.query.bdate == player.bDay)

        search1 = self.playersTable.search(cond1 & cond2 & cond3)

        if not search1:
            self.playersTable.insert(ser_p1)
            print('inserted')
        else:
            print('not inserted')

    def modify_elo(self, player):
        """
        :param player:
        :return:
        """
        self.playersTable.search(self.query.lname == player.lastName.lower())

    def reports(self, player):
        """
        :param player:
        :return:
        """
        self.playersTable.search(self.query.lname == player.lastName.lower())

    def return_demo(self):
        """
        :return:
        """
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

    def return_players(self):
        """
        :return:
        """
        playerlist = []
        for player in self.playersTable.all():
            lname = player['lname'].capitalize()
            fname = player['fname'].capitalize()
            bdate = player['bdate']
            genre = player['genre']
            elo = player['elo']
            playerlist.append(classes.Player(lname, fname, bdate,
                                             genre, elo))
        return playerlist


class TournamentDbMananger:
    """"""
    def __init__(self):
        """"""
        self.db = TinyDB('tournament.json')
        self.query = Query()
        self.tournament = self.db.table('tournament')
        self.rounds = self.db.table('rounds')
        self.matches = self.db.table('matches')

    def init_tournament(self, tournament):
        """
        :param tournament:
        :return:
        """
        index = self.tournament.__len__()
        ser_tournament = {
            'id': index,
            'name': tournament.name.lower(),
            'place': tournament.place.lower(),
            'date': tournament.date,
            'turns': tournament.turns,
            'timeType': tournament.timeType,
            'description': tournament.description

        }

        cond1 = self.query.name == tournament.name.lower()
        cond2 = self.query.place == tournament.place.lower()
        cond3 = self.query.date == tournament.date

        search1 = self.tournament.search(cond1 & cond2 & cond3)

        if not search1:
            self.tournament.insert(ser_tournament)
            print('inserted')
        else:
            print('not inserted')

    def insert_round(self, tournament, index):
        """"""
        theround = tournament.tournees[index]
        ser_round = {
            'tournament': None,
            'name': theround.name,
            'count': index
        }
        self.rounds.insert(ser_round)

    def init_match(self, tournament, index):

        ser_match = {
            'tournament': None,
            'round': None,
            'count': None,
            'player1': None,
            'result1': 'TBD',
            'player2': None,
            'result2:': 'TBD'
        }
        self.rounds.insert(ser_match)

    def enter_score(self):
        pass
