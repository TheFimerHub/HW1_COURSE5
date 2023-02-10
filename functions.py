import sqlite3

def search_fresh_film(title_query):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title LIKE ?
            ORDER BY release_year DESC
            LIMIT 1
        """
        cursor.execute(sqlite_query, ('%' + title_query + '%',))
        executed_query = cursor.fetchall()
        result = executed_query[0]
        return {
            'title': result[0],
            'country': result[1],
            'release_year': result[2],
            'genre': result[3],
            'description': result[4]
        }


def search_range_release(release_start, release_end):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN ? AND ?
            ORDER BY release_year DESC
            LIMIT 100
        """
        cursor.execute(sqlite_query, (release_start, release_end,))
        executed_query = cursor.fetchall()
        result = list()
        for i in range(len(executed_query)):
            result.append({
                'title': executed_query[i][0],
                'release_year': executed_query[i][1],
            })
        return result


def profile_rating(rate):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
            SELECT title, rating, description
            FROM netflix
            WHERE rating = ?
        """
        result = list()
        for rat in rate:
            cursor.execute(sqlite_query, (rat,))
            executed_query = cursor.fetchall()
            for i in range(len(executed_query)):
                result.append({
                        'title': executed_query[i][0],
                        'rating': executed_query[i][1],
                        'description': executed_query[i][2]
                    })
        return result

def search_genere(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
            SELECT title, description
            FROM netflix
            WHERE listed_in like ?
            ORDER BY listed_in DESC
            LIMIT 10
        """
        cursor.execute(sqlite_query, ('%' + genre + '%',))
        executed_query = cursor.fetchall()
        result = list()
        for i in range(len(executed_query)):
            result.append({
                'title': executed_query[i][0],
                'description': executed_query[i][1],
            })
        return result

def with_two_actors(actor1, actor2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
            SELECT `cast`
            FROM netflix
            WHERE `cast` LIKE ?
            AND `cast` LIKE ?
        """
        cursor.execute(sqlite_query, ('%' + actor1 + '%', '%' + actor2 + '%'))
        executed_query = cursor.fetchall()
        count_actor = dict()
        for execute in executed_query:
            for actors in execute:
                for actor in actors.split(', '):
                    if actor in count_actor.keys():
                        count_actor[actor] += 1
                    elif actor != actor1 and actor != actor2:
                        count_actor[actor] = 1
        result = list()
        for key, value in count_actor.items():
            if value >= 2:
                result.append({
                    'actor': key, 'count': value}
                )
        return result

def settings_films(typical, year, ganre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
            SELECT title, description
            FROM netflix
            WHERE `type` LIKE ?
            AND `release_year` LIKE ?
            AND listed_in LIKE ?
        """
        cursor.execute(sqlite_query, ('%' + typical + '%', year, '%' + ganre + '%'))
        result = list()
        executed_query = cursor.fetchall()
        for i in range(len(executed_query)):
            result.append({
                'title': executed_query[i][0],
                'description': executed_query[i][1]
            })
        return result