from datetime import datetime


class Player:
    def __init__(self, fname, lname, bday, genre, elo):
        self.firstName = fname
        self.lastName = lname
        self.bDay = bday
        self.genre = genre
        self.elo = elo


class Tournament:
    def __init__(self, name, place, date,
                 timetype, desc):
        self.name = name
        self.place = place
        self.date = date
        self.turns = 4
        self.tournees = []
        self.players = []
        self.timeType = timetype
        self.Description = desc

    def sort_by_score(self):
        scoreboard = []
        for player in self.players:
            pscore = [player, 0]
            for turn in self.tournees:
                for match in turn.matches:
                    if player in match[0]:
                        pscore[1] += match[0][1]
                    if player in match[1]:
                        pscore[1] += match[1][1]
            scoreboard.append(pscore)
        sortedscoreboard = sorted(scoreboard, key=lambda score: score[1], reverse=True)

        return sortedscoreboard

    def sort_by_elo(self):
        sortedlist = sorted(self.players, key=lambda elosort: elosort.elo)
        return sortedlist


class Round:
    def __init__(self, name, matcheslist):
        self.name = name
        self.matches = matcheslist
        self.startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.endTime = ''

    def enter_scores(self, results):
        ii = 0
        for result in results:
            if result == "a":
                self.matches[ii][0][1] = 1
                self.matches[ii][1][1] = 0
            elif result == "b":
                self.matches[ii][0][1] = 0
                self.matches[ii][1][1] = 1
            else:
                self.matches[ii][0][1] = 0.5
                self.matches[ii][1][1] = 0.5
            ii += 1
        self.endTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def tbd_match(self):
        pass

