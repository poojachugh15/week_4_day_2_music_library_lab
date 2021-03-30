from db.run_sql import run_sql
from models.artist import Artist


def save(artist):
    
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    
    id = results[0]['id']
    artist.id = id
    return artist
    
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def find_by_id(id):
    sql = "SELECT * FROM artists WHERE ID = %s"
    values = [id]
    results = run_sql(sql, values)
    artist_dictionary = results[0]
    
    if artist_dictionary is not None:
        return Artist(artist_dictionary["name"], artist_dictionary["id"])
    