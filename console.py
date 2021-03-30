import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()

artist_repository.delete_all()

artist1 = Artist("Katy Perry")
artist_repository.save(artist1)

artist2 = Artist("Justin Bieber")
artist_repository.save(artist2)

print(artist1.name)
album1 = Album("Teenage Dream", artist1, "pop")
album_repository.save(album1)
album2 = Album("My world", artist2, "pop")
album_repository.save(album2)
print(album1.title)
pdb.set_trace()

