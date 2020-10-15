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
        cursor.execute('''select DISTINCT(a.name),a.actor_id, ch.char_name from movie_character as ch
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
        cursor.execute('''select DISTINCT(m.movie_name),m.movie_id, ch.char_name, d.release_date, d.runtime 
                        from movie_character as ch
                        natural join movie as m
                        natural join actor as a
                        natural join details as d
                        where a.name=%s''',[act_name])
        res = [{'mname':x[0],'mid':x[1],'cname':x[2],'date':x[3],'time':x[4]} for x in cursor.fetchall()]
        return res

def getGenre(name):
    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCT(d.genre)
                        from details as d
                        natural join movie as m
                        where m.movie_name=%s''',[name[0]])
        one = cursor.fetchall()[0][0].split(",")
    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCT(d.genre)
                        from details as d
                        natural join movie as m
                        where m.movie_name=%s''',[name[1]])
        two = cursor.fetchall()[0][0].split(",")
    with connection.cursor() as cursor:
        cursor.execute('''select DISTINCT(d.genre)
                        from details as d
                        natural join movie as m
                        where m.movie_name=%s''',[name[2]])
        three = cursor.fetchall()[0][0].split(",")
        res = one+two+three
        return res

def getRecommendation(genres):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name)
                        from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0''',[genres[0]])
        # return [x for x in cursor.fetchall()]
        one = [x[0] for x in cursor.fetchall()]
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name)
                        from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0''',[genres[1]])
        two = [x[0] for x in cursor.fetchall()]
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name)
                        from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0''',[genres[2]])
        three = [x[0] for x in cursor.fetchall()]
        res = one+two+three
        return res
    
def getMovies_genre(gen_name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name) from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0 limit 1''',[gen_name])
        res = cursor.fetchall()[0][0]
        return res

def genre_detail(gen_name):
    with connection.cursor() as cursor:
        cursor.execute('''select distinct(m.movie_name), m.movie_id, d.release_date, d.runtime from movie as m
                        natural join details as d
                        where FIND_IN_SET(%s,genre)>0''',[gen_name])
        res = [{'name': x[0], 'id': x[1],'date':x[2],'time':x[3]} for x in cursor.fetchall()]
        return res

def actor_id_retrieve(name):
    with connection.cursor() as cursor:
        cursor.execute('''select actor_id from actor where name=%s''',name)
        res = cursor.fetchall()[0][0]
        return res

def director_id_retrieve(name):
    with connection.cursor() as cursor:
        cursor.execute('''select director_id from director where name=%s''',name)
        res = cursor.fetchall()[0][0]
        return res

def production_id_retrieve(name):
    with connection.cursor() as cursor:
        cursor.execute('''select production_id from production_house where name=%s''',name)
        res = cursor.fetchall()[0][0]
        return res

def max_movie():
    with connection.cursor() as cursor:
        cursor.execute('''select MAX(movie_id) from movie;''')
        res = cursor.fetchall()[0][0]
        return res

def max_cast():
    with connection.cursor() as cursor:
        cursor.execute('''select MAX(cast_id) from cast;''')
        res = cursor.fetchall()[0][0]
        return res

def insert_into_cast(castvalues):
    with connection.cursor() as cursor:
        cursor.executemany('''insert into cast values (%s,%s)''',castvalues)

def insert_into_movie(movievalues):
    with connection.cursor() as cursor:
        cursor.executemany('''insert into movie values (%s,%s,%s)''',movievalues)

def insert_into_details(detailsvalues):
    with connection.cursor() as cursor:
        cursor.execute('''insert into details values (%s,%s,%s,%s,%s,%s,%s,%s)''',detailsvalues[0],detailsvalues[1],detailsvalues[2],detailsvalues[3],detailsvalues[4],detailsvalues[5],detailsvalues[6],detailsvalues[7])

def insert_into_character(charactervalues):
    with connection.cursor() as cursor:
        cursor.executemany('''insert into movie_character values (%s,%s,%s)''',charactervalues)

def delete_movie_id_char():
    with connection.cursor() as cursor:
        cursor.executemany('''delete from movie_character where movie_id=%s''',[])

def delete_movie_id_cast():
    with connection.cursor() as cursor:
        cursor.executemany('''delete from cast where movie_id=%s''',[])
    
def delete_movie_id_details():
    with connection.cursor() as cursor:
        cursor.executemany('''delete from details where movie_id=%s''',[])

def delete_movie_id():
    with connection.cursor() as cursor:
        cursor.executemany('''delete from movie where movie_id=%s''',[])



