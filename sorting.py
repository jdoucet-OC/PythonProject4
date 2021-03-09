def score_sort(rounds, tournament):
    scores = []
    for item in rounds.matches:
        scores.append(item[0])
        scores.append(item[1])
    sortedscore = sorted(scores, key=lambda score: score[1], reverse=True)
    for jj in range(0, 4):
        newmatch = ([sortedscore[jj], 'TBD'], [sortedscore[jj+1], 'TBD'])
        np1, np2 = newmatch[0][0], newmatch[1][0]
        for theround in tournament.tournees:
            for oldmatch in rounds.matches:
                # On prend les npn ( new players, prochain round en création )
                # et opn ( old players, matches du round précédent )
                # pour vérifier si ils ont déjà joué ensemble
                np1, np2 = newmatch[0][0], newmatch[1][0]
                op1, op2 = oldmatch[0][0], oldmatch[1][0]
                # Condition pour voir si le np1 et np2 se trouve dans le match avec
                # op1 et op2
                if (np1 and np2) == ((op1 and op2) or (op2 and op1)):
                    print('déjà joué')
