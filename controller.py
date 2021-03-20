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
        if choice == "q":
            quit()

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

        # insertion du round 1 et du match 1 sans resultat dans la DB
        self.tournamentDb.insert_round(tournament, 0)
        indexm = 0
        for match in round1.matches:
            p1 = match[0][0]
            p2 = match[1][0]
            self.tournamentDb.init_match(tournament, 0, indexm, p1, p2)
            indexm += 1

        # Préparation du match
        self.view.show_elo_match(round1.matches)
        results = self.view.enter_results(round1.matches)
        self.process_results(tournament, results)

    def next_rounds(self, tournament):
        """
        :param tournament:
        :return:
        """
        roundnumber = len(tournament.tournees)+1
        fstring = f"Round{roundnumber}"
        sortedscorelist = tournament.sort_by_score()
        nexttour = []
        for ii in range(0, len(sortedscorelist), 2):
            nexttour.append((sortedscorelist[ii], sortedscorelist[ii+1]))
        nextround = classes.Round(fstring, nexttour)
        tournament.tournees.append(nextround)

        # insertion du round et du match sans resultat dans la DB
        indexr = roundnumber-1
        self.tournamentDb.insert_round(tournament, indexr)
        indexm = 0
        for match in nextround.matches:
            p1 = match[0][0]
            p2 = match[1][0]
            self.tournamentDb.init_match(tournament, indexr, indexm, p1, p2)
            indexm += 1

        # Préparation du match
        print(indexr, indexm)
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
        # insertion des resultats du match dans la DB
        self.tournamentDb.enter_score(tournament)
        if tournament.turns == len(tournament.tournees):
            self.end_tournament()
        else:
            self.next_rounds(tournament)

    def end_tournament(self):
        """
        :return:
        """
        self.run()

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
        choice_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        choice_func = [
            self.all_player_alpha_sort,
            self.all_players_elo_sort,
            self.tournament_alpha_sort,
            self.tournament_elo_sort,
            self.all_tournaments,
            self.list_all_rounds,
            self.list_all_matches
        ]
        for letter in choice_list:
            if choice == letter:
                index = choice_list.index(choice)
                choice_func[index]()

    def all_player_alpha_sort(self):
        all_players = self.playerDb.return_players()
        all_players.sort(key=lambda x: x.lastName)
        self.view.show_pname(all_players)

    def all_players_elo_sort(self):
        all_players = self.playerDb.return_players()
        all_players.sort(key=lambda x: x.elo, reverse=True)
        self.view.show_pname(all_players)

    def tournament_alpha_sort(self):
        plist = self.tournamentDb.return_player_tournament(0)
        for item in plist:
            print(item)

    def tournament_elo_sort(self):
        plist = self.tournamentDb.return_player_tournament(0)
        for item in plist:
            print(item)

    def all_tournaments(self):
        plist = self.tournamentDb.return_tournaments()
        for item in plist:
            print(item)

    def list_all_rounds(self):
        rlist = self.tournamentDb.return_rounds(0)
        for item in rlist:
            print(item)

    def list_all_matches(self):
        mlist = self.tournamentDb.return_all_matches(0)
        for item in mlist:
            print(item)

    def resumt_tt(self):
        pass
