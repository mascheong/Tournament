#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print "Cannot connect to database tournament."


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""

    """Uses count() aggregation function then returns singular row tuple"""

    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) as num from players;")
    row = c.fetchone()
    return row[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    """Insert query into players table and sanitizing input"""

    db = connect()
    c = db.cursor()
    c.execute("""INSERT INTO players (name) values(%s);""",
              (bleach.clean(name),))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("""SELECT w.id, w.name, w.wins, w.wins + l.losses as matches
                 FROM wins w left join losses l
                 ON w.id = l.id
                 GROUP BY w.id, w.name, w.wins, l.losses
                 ORDER BY wins desc;""")
    rows = c.fetchall()
    db.close
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    """
    Insert into matches table then update players table with win or loss then
        total match count
    """

    db = connect()
    c = db.cursor()
    c.execute("""INSERT INTO matches (winner, loser) values(%s, %s);""",
              (winner, loser))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    """Get playerStandings then iterate every two rows to generate matchups"""
    matches = []
    rows = playerStandings()
    for x in range(0, len(rows), 2):
        id1 = rows[x][0]
        name1 = rows[x][1]
        id2 = rows[x+1][0]
        name2 = rows[x+1][1]
        t = (id1, name1, id2, name2)
        matches.append(t)
    return matches
