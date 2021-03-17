import classes
import dbmanage


class Controller:
    """"""
    def __init__(self, view):
        """
        :param view:
        """
        self.tournament = ''
        self.view = view
        self.playerDb = dbmanage.PlayerDbManager()
        self.tournamentDb = dbmanage.TournamentDbMananger()

    def run(self):
        """
        :return:
        """
        choice = self.view.menu()
        if choice == "a":
            self.new_tt()
        if choice == "b":
            self.resumt_tt()
        if choice == "c":
            self.edit_players()
        if choice == "d":
            self.start_reports()

    def new_tt(self):
        """
        :return:
        """
        name, place, date, timetype, desc = self.view.new_tournament()
        tournament = classes.Tournament(name, place, date, timetype, desc)
        self.tournamentDb.init_tournament(tournament)
        players = self.view.add_players()
        if players == "a":
            self.demo_players(tournament)
        if players == "b":
            self.pick_players(tournament)

    def demo_players(self, tournament):
        """
        :param tournament:
        :return:
        """
        tournament.players = self.playerDb.return_demo()
        tournament.players = tournament.sort_by_elo()
        self.view.show_pname(tournament.players)
        self.first_round(tournament)

    def first_round(self, tournament):
        """
        :param tournament:
        :return:
        """
        middle = len(tournament.players) // 2
        lowerhalf = tournament.players[:middle]
        upperhalf = tournament.players[middle:]
        tour1 = []
        for ii in range(0, middle):
            tour1.append(([lowerhalf[ii], 0], [upperhalf[ii], 0]))
        round1 = classes.Round('Round1', tour1)
        tournament.tournees.append(round1)
        self.tournamentDb.insert_round(tournament)
        self.view.show_elo_match(round1.matches)
        results = self.view.enter_results(round1.matches)
        self.process_results(tournament, results)

    def next_rounds(self, tournament):
        """
        :param tournament:
        :return:
        """
        index = len(tournament.tournees)
        fstring = f"Round{index}"
        sortedscorelist = tournament.sort_by_score()
        nexttour = []
        for ii in range(0, len(sortedscorelist), 2):
            nexttour.append((sortedscorelist[ii], sortedscorelist[ii+1]))
        nextround = classes.Round(fstring, nexttour)
        tournament.tournees.append(nextround)
        self.view.show_elo_match(nextround.matches)
        results = self.view.enter_results(nextround.matches)
        self.process_results(tournament, results)

    def process_results(self, tournament, results):
        """
        :param tournament:
        :param results:
        :return:
        """
        index = len(tournament.tournees)-1
        theround = tournament.tournees[index]
        theround.enter_scores(results)
        self.view.show_results(theround.matches)
        if tournament.turns == len(tournament.tournees):
            self.end_tournament()
        else:
            self.next_rounds(tournament)

    def end_tournament(self):
        """
        :return:
        """
        self.view.tournament_end_view()

    def pick_players(self, tournament):
        pass

    def resume_tt(self):
        pass

    def edit_players(self):
        players = self.playerDb.return_players()
        index = self.view.show_players_edit(players)
        if index == 'a':
            self.run()
        player = (players[int(index)-1])
        new_elo = self.view.edit_elo(player)
        print(new_elo)
        self.edit_players()

    def start_reports(self):
        choice = self.view.reports_menu()

    def resumt_tt(self):
        pass
