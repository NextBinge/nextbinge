from django.db import connection

def toprated():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_name) from movie
                        where movie.movie_id in (
                        select details.movie_id from details
                        where vote_average>7.5);''')
        res = [x[0] for x in cursor.fetchall()]
        return res

