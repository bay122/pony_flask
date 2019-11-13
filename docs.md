Crear archivo requirements:
pip freeze > requirements.txt

Cargar dependencias:
$ pip install -r requirements.txt
o
$ pip3 install -r requirements.txt

Documentación de dependencias:
https://rukbottoland.com/blog/como-instalar-paquetes-python-con-requirementstxt/
https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e

________________________________________________

Existencia de registro:

PlayerDb.exists(id=playerId)
return PartidaDb.exists(idChat = player.getChatId(), gameType = game_name, owner = player.getId())
return select(game for game in Partida if chat_id == chatId and game.name == gameName).exists()

---------------------------------------
Inserciones:

idNewPlayer = db.insert("PlayerDb", id = playerId, name = str(playerName), userName = pUserName)
StatsUnoDb(idPlayer = player.getId(), gamesPlayed = 1, firstPlaces = 0, cardsPlayed = 0, totalCards = 0)


---------------------------------------
Extracciones individuales:

p = PlayerDb[playerId]
partida = PartidaDb.get(token = game_token)
return PlayerDb[self.__playerId].idCurrentGame
game = PartidaDb.get(idChat = player.getChatId(), gameType = game_name, owner = player.getId())


---------------------------------------
Extracciones grupales:

for card in DeckUnoDb.select(lambda card: card.idPartida == self.getCurrentGame() and card.idPlayer == self.getId()):
select(p for p in PlayerDb)[:3].show() #el [:3] significa que el limite maximo de players a mostrar es 3
select((p.id, p.token, p.gameType, p.idGame, p.owner) for p in PartidaDb).show()
select(p for p in PartidaPlayerDb).show()
totalPlayersDb = PartidaPlayerDb.select(lambda p: p.idPartida == self.__partidaDb.id)
p = PartidaPlayerDb.select(lambda p: p.idPartida == self.__partidaDb.id and p.turnNumber == 0)

---------------------------------------
Edicion:

PartidaDb[idNewPartida].set(token= token_game)
stats.gamesPlayed += 1

---------------------------------------
Borrar:

delete(pp for pp in PartidaPlayerDb if pp.idPartida == partida.getPartidaId())
PartidaUnoDb[partida.getGameId()].delete()

_________________________________________________________________________
@db_session
def print_person_name(person_id):
    p = Person[person_id]
    print p.name
    # database session cache will be cleared automatically
    # database connection will be returned to the pool

@db_session
def add_car(person_id, make, model):
    Car(make=make, model=model, owner=Person[person_id])
    # commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool
    
The db_session() decorator performs the following actions on exiting function:

Performs rollback of transaction if the function raises an exception
Commits transaction if data was changed and no exceptions occurred
Returns the database connection to the connection pool
Clears the database session cache
Even if a function just reads data and does not make any changes, it should use the db_session() in order to return the connection to the connection pool.

The entity instances are valid only within the db_session(). If you need to render an HTML template using those objects, you should do this within the db_session().

Another option for working with the database is using the db_session() as the context manager instead of the decorator:

with db_session:
    p = Person(name='Kate', age=33)
    Car(make='Audi', model='R8', owner=p)
    # commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool