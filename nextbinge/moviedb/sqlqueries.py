from django.db import connection
from . import poster

def getname(id):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_name) from movie
                        where movie.movie_id = %s''', [id])
        res = cursor.fetchall()[0][0]
        return res

def toprated():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_name), movie_id from movie
                        where movie.movie_id in (
                        select details.movie_id from details
                        where vote_average>7.5);''')
        res = [{'name': x[0], 'id': x[1]} for x in cursor.fetchall()]
        return res

def mostpopular():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), movie_id from movie as m
                        natural join details as d
                        order by d.popularity desc;''')
        res = [{'name': x[0], 'id': x[1]} for x in cursor.fetchall()]
        return res

def recent():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), movie_id from movie as m
                        natural join details as d
                        order by d.release_date desc;
                        ''')
        res = [{'name': x[0], 'id': x[1]} for x in cursor.fetchall()]
        return res

def actor_descp(mov_name):
    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCt(a.name), ch.char_name from movie_character as ch
                        natural join movie as m
                        natural join actor as a
                        where m.movie_name=%s''',[mov_name])
        res = [{'aname':x[0],'cname':x[1]} for x in cursor.fetchall()]
        return res

def movie_descp(mov_name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(d.description) from details as d
                        natural join movie as m
                        where m.movie_name=%s''',[mov_name])
        res = cursor.fetchall()[0][0]
        return res

