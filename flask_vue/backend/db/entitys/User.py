from .. import db, Optional, Required, PrimaryKey, db_session, Set

class Person(db.Entity):
	id = PrimaryKey(int, auto=True)
	name = Required(str)
	mail = Required(str)
	#character = Set('Car')