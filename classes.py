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


class Round:
    def __init__(self, name, matcheslist):
        self.name = name
        self.matches = matcheslist
        self.startTime = ''
        self.endTime = ''


