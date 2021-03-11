import classes
import dbmanage

class Controller:
    def __init__(self, view):
        self.tournament = ''
        self.view = view
        self.db = dbmanage.DbManager()
        self.players = []

    def run(self):
        choice = self.view.menu()
        if choice == "a":
            self.new_tt()
        if choice == "b":
            self.resumt_tt()
        if choice == "c":
            self.edit_players()
        if choice == "d":
            self.reports()

    def new_tt(self):
        name, place, date, timetype, desc = self.view.new_tournament()
        self.tournament = classes.Tournament(name, place, date, timetype, desc)
        players = self.view.add_players()
        if players == "a":
            self.demo_players()
        if players == "b":
            self.pick_players()

    def demo_players(self):
        self.players = self.db.return_demo()
        self.view.show_pname(self.players)

    def pick_players(self):
        pass

    def resume_tt(self):
        pass

    def edit_players(self):
        pass

    def reports(self):
        pass
