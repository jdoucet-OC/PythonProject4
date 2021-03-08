from tinydb import TinyDB, Query


def insert_to_db(player):
    db = TinyDB('players.json')
    query = Query()

    ser_p1 = {
        'lname': player.lastName.lower(),
        'fname': player.firstName.lower(),
        'bdate': player.bDay,
        'genre': player.genre,
        'elo': player.elo
    }
    search1 = db.search((query.lname == player.lastName.lower())
                        & (query.fname == player.firstName.lower())
                        & (query.bdate == player.bDay))

    if not search1:
        db.insert(ser_p1)
        print('inserted')
    else:
        print('not inserted')

