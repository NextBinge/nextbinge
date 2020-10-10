from django.db import connection
from . import poster

def toprated():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_name) from movie
                        where movie.movie_id in (
                        select details.movie_id from details
                        where vote_average>7.5);''')
        res = [{'name':x[0], 'img':poster.getImage(x[0])} for x in cursor.fetchall()]
        return res

def mostpopular():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name) from movie as m
                        natural join details as d
                        order by d.popularity desc;''')
        res = [{'name':x[0], 'img':poster.getImage(x[0])} for x in cursor.fetchall()]
        return res

def recent():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name) from movie as m
                        natural join details as d
                        order by d.release_date desc;
                        ''')
        res = [{'name':x[0], 'img':poster.getImage(x[0])} for x in cursor.fetchall()]
        return res

def top50():
    with connection.cursor() as cursor:
        cursor.execute('''
                        ''')
        res = [{'name':x[0], 'img':poster.getImage(x[0])} for x in cursor.fetchall()]
        return res