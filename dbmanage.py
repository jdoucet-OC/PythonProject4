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

    def modify_elo(self, player, elo):
        """"""
        cond1 = (self.query.lname == player.lastName.lower())
        cond2 = (self.query.fname == player.firstName.lower())
        cond3 = (self.query.bdate == player.bDay)
        self.playersTable.update({'elo': elo}, cond1 & cond2 & cond3)

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
            playerlist.append(classes.Player(fname, lname, bdate,
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
            playerlist.append(classes.Player(fname, lname, bdate,
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

    def get_tournament_id(self, tournament):
        """"""
        cond1 = self.query.name == tournament.name.lower()
        cond2 = self.query.place == tournament.place.lower()
        cond3 = self.query.date == tournament.date

        search1 = self.tournament.search(cond1 & cond2 & cond3)
        return search1[0]['id']

    def insert_round(self, tournament, index):
        """"""

        theround = tournament.tournees[index]
        thetournament = self.get_tournament_id(tournament)
        ser_round = {
            'id': index,
            'tournament': thetournament,
            'name': theround.name
        }
        cond1 = self.query.tournament == ''
        cond2 = self.query.count == index
        search1 = self.rounds.search(cond1 & cond2)
        if not search1:
            self.rounds.insert(ser_round)
        else:
            print('round déjà existant')

    def init_match(self, tournament, indexr, indexm, p1, p2):
        """"""

        thetournament = self.get_tournament_id(tournament)
        ser_match = {
            'id': indexm,
            'round': indexr,
            'tournament': thetournament,
            'player1': p1.firstName,
            'result1': 'TBD',
            'player2': p2.firstName,
            'result2:': 'TBD'
        }
        self.matches.insert(ser_match)

    def enter_score(self, tournament):
        """"""
        pass

    def return_player_tournament(self, tourid):
        search1 = self.query.tournament == tourid
        search2 = self.query.round == 0
        playerlist = []
        for item in self.matches.search(search1 & search2):
            playerlist.append(item['player1'])
            playerlist.append(item['player2'])
        return playerlist

    def return_tournaments(self):
        tourlist = []
        for tournament in self.tournament.all():
            name = tournament['name'].capitalize()
            place = tournament['place'].capitalize()
            date = tournament['date']
            turns = tournament['turns']
            timetype = tournament['timeType']
            tourlist.append((name, place, date, turns, timetype))
        return tourlist

    def return_rounds(self, tourid):
        search1 = self.query.id == tourid
        roundlist = []
        for rounds in self.rounds.search(search1):
            round_id = rounds['id']
            tournament_id = rounds['tournament']
            name = rounds['name'].capitalize()
            roundlist.append((round_id, tournament_id, name))
        return roundlist

    def return_all_matches(self, tourid):
        search1 = self.query.tournament == tourid
        matchlist = []
        for item in self.matches.search(search1):
            matchlist.append(item)
        return matchlist
