from pony.orm import *

#db = Database()
db = Database('mysql', host='127.0.0.1', user='root', passwd='1234', db='board_rol')

class Person(db.Entity):
	name = Required(str)
	mail = Optional(unicode)
	age = Required(int)
	cars = Set('Car')

class Car(db.Entity):
	make = Required(str)
	model = Required(str)
	owner = Required(Person)


sql_debug(True)
db.generate_mapping(create_tables=True)

'''
def createBD():
	try:
	    db.bind(provider='mysql', host='127.0.0.1', user='root', passwd='1234', db='board_rol')
	    #sql_debug(True)
	    set_sql_debug(True)
	    db.generate_mapping(create_tables=True)
	except Exception as e:
	    print("Error: [DbManager.createDB] ->"+str(e))
'''

@db_session
def llenarBD():
	p1 = Person(name='John', age=20)
	p2 = Person(name='Mary', age=22)
	p3 = Person(name='Bob', age=30)
	c1 = Car(make='Toyota', model='Prius', owner=p2)
	c2 = Car(make='Ford', model='Explorer', owner=p3)
	
@db_session
def print_person_name(person_id):
    p = Person[person_id]
    print(p.name)
    # database session cache will be cleared automatically
    # database connection will be returned to the pool

@db_session
def add_car(person_id, make, model):
    Car(make=make, model=model, owner=Person[person_id])
    # commit() will be done automatically
    # database session cache will be cleared automatically
    # database connection will be returned to the pool

if __name__ == '__main__':
	#createBD()
	#llenarBD()
	with db_session:
		select(p for p in Person).order_by(Person.name)[:2].show()