from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository


def save(album):
    
    sql = "INSERT INTO albums (title, artist_id, genre ) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
def select_all():
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    
    # return results
    albums = []
    
    for row in results:
        artist = artist_repository.find_by_id(row["artist_id"])
        album = Album(row["title"], row ["genre"], artist)
        albums.append(album)
        
    return albums
