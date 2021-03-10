import controller
import dbmanage


class Views:
    def __init__(self):
        self.control = controller.Controller()
        self.managedb = dbmanage.DbManager

    def menu(self):
        print('Chess Tournament Menu :')
        choice = input('A: New Tournament\n'
                       'B: Resume Tournament\n'
                       'C: Edit Players\n'
                       'D: Reports\n').lower()

        if choice == "a":
            self.new_tournament()
        if choice == "b":
            self.resume_tournament()
        if choice == "c":
            self.edit_players()
        if choice == "d":
            self.reports()

    def new_tournament(self):
        print("New tournament :")
        self.control.new_tournament()

    def resume_tournament(self):
        print("Resuming previous tournament...")
        self.control.resume_tournament()

    def edit_players(self):
        print("Edit players :")
        self.managedb.modify_elo()

    def reports(self):
        print("Reports :")
        self.managedb.reports()


