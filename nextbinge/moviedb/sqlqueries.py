from django.db import connection
from . import poster

def getname(id):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_name) from movie
                        where movie.movie_id = %s''', [id])
        res = cursor.fetchall()[0][0]
        return res

def getid(name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_id) from movie
                        where movie.movie_name = %s''', [name])
        res = cursor.fetchall()[0][0]
        return res

def getnameactor(id):
    with connection.cursor() as cursor:
        cursor.execute('''select name from actor
                        where actor_id = %s''', [id])
        res = cursor.fetchall()[0][0]
        return res

def getnamedirector(id):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(d.name) from director as d
                        natural join cast as c
                        natural join movie as m
                        where m.movie_id = %s''', [id])
        res = [{'name': x[0]} for x in cursor.fetchall()]
        return res

def getnameprod(id):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(p.name) from production_house as p
                        natural join cast as c
                        natural join movie as m
                        where m.movie_id = %s''', [id])
        res = [{'name': x[0]} for x in cursor.fetchall()]
        return res

def getallmovienames():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_name) from movie''')
        res = [x[0] for x in cursor.fetchall()]
        return res

def toprated():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), m.movie_id, d.release_date, d.runtime from movie as m
                        natural join details as d
                        where d.vote_average>7.5;''')
        res = [{'name': x[0], 'id': x[1],'date':x[2],'time':x[3]} for x in cursor.fetchall()]
        return res

def mostpopular():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), m.movie_id, d.release_date, d.runtime from movie as m
                        natural join details as d
                        order by d.popularity desc;''')
        res = [{'name': x[0], 'id': x[1],'date':x[2],'time':x[3]} for x in cursor.fetchall()]
        return res

def recent():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), m.movie_id, d.release_date, d.runtime from movie as m
                        natural join details as d
                        order by d.release_date desc;
                        ''')
        res = [{'name': x[0], 'id': x[1],'date':x[2],'time':x[3]} for x in cursor.fetchall()]
        return res

def actor_descp(mov_name):
    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCt(a.name),a.actor_id, ch.char_name from movie_character as ch
                        natural join movie as m
                        natural join actor as a
                        where m.movie_name=%s''',[mov_name])
        res = [{'aname':x[0],'aid':x[1],'cname':x[2]} for x in cursor.fetchall()]
        return res

def movie_descp(mov_name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(d.description) from details as d
                        natural join movie as m
                        where m.movie_name=%s''',[mov_name])
        res = cursor.fetchall()[0][0]
        return res

def getMovies():
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(movie_id) from movie''')
        res = [x[0] for x in cursor.fetchall()]
        return res

def actor_movies(act_name):
    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCt(m.movie_name),m.movie_id, ch.char_name, d.release_date, d.runtime 
                        from movie_character as ch
                        natural join movie as m
                        natural join actor as a
                        natural join details as d
                        where a.name=%s''',[act_name])
        res = [{'mname':x[0],'mid':x[1],'cname':x[2],'date':x[3],'time':x[4]} for x in cursor.fetchall()]
        return res

def getMovies_genre(gen_name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), m.movie_id from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0 limit 1''',[gen_name])
        res = cursor.fetchall()[0][0]
        return res

def genre_detail(gen_name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), m.movie_id, d.release_date, d.runtime from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0''',[gen_name])
        res = [x[0] for x in cursor.fetchall()]
        return res