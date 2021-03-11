class Views:
    def __init__(self):
        pass

    @staticmethod
    def menu():
        print('Chess Tournament Menu :\n')
        choice = input('A: New Tournament\n'
                       'B: Resume Tournament\n'
                       'C: Edit Players\n'
                       'D: Reports\n').lower()

        return choice

    @staticmethod
    def new_tournament():
        print("\n\nNew tournament, enter tournament attributes")
        name = input("Tournament name : ")
        place = input("City : ")
        date = input("Date : ")
        timetype = input("TimeType : ")
        desc = input("Description : ")
        return name, place, date, timetype, desc

    @staticmethod
    def add_players():
        print("\n\nAdd players")
        players = input("A: Add 8 Pre-selected Player ( demo )\n"
                        "B: Pick 8 Players\n").lower()
        return players

    @staticmethod
    def show_pname(players):
        for player in players:
            print(player.lastName)

    @staticmethod
    def resume_tournament():
        print("Resuming previous tournament...")
        pass

    @staticmethod
    def edit_players():
        print("Edit players :")
        pass

    @staticmethod
    def reports():
        print("Reports :")
        pass


