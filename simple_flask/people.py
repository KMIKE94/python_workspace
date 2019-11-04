from datetime import datetime
from flask import make_response, abort
import sqlite3
import json
from models import (
    Person,
    PersonSchema
)
from config import db

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    # return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

    # conn = sqlite3.connect('people.db')
    # cur = conn.cursor()
    # cur.execute('select * from person')
    # peoples = cur.fetchall()
    # print(peoples)
    # Create the list of people from our data
    people = Person.query.order_by(Person.lname).all()

    if people is not None:
        # Serialize the data for the response
        person_schema = PersonSchema(many=True)
        return person_schema.dump(people)
    
    else:
        abort(
            404, 'No People found'
        )
    

def read_one(person_id):
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    if person is not None:
        person_schema = PersonSchema()
        return person_schema.dump(person)
    
    else:
        abort (
            404, "Person with last name {lname} not found".format(lname=lname)
        )

def create(person):
    fname = person.get("fname", None)
    lname = person.get("lname", None)

    schema = PersonSchema()
    new_person = schema.load(person)

    db.session.add(new_person)
    db.session.commit()

    return schema.dump(new_person)

    # if lname not in PEOPLE and lname is not None:
    #     PEOPLE[lname] = {
    #         "lname": lname,
    #         "fname": fname,
    #         "timestamp": timestamp
    #     }
    #     return make_response(
    #         "{lname} successfully created".format(lname=lname)
    #     )
    # else:
    #     abort(
    #         406, "Person with {lname} already exists".format(lname=lname)
    #     )

def update(person_id, person):
    # fname = person.get("fname", None)

    # if lname in PEOPLE and lname is not None:
    #     PEOPLE[lname]["fname"] = person.get("fname", None)
    #     PEOPLE[lname]["timestamp"] = get_timestamp()
    #     return make_response(
    #         "Successfully updated person {lname}".format(lname=lname)
    #     )
    # else:
    #     abort(
    #         404, "Person with {lname} does not exist".format(lname=lname)
    #     )

    fname = person.get("fname",None)
    lname = person.get("lname",None)
    # updated_person = Person.query.filter(Person.person_id == person_id).update(
    #     {Person.fname: fname, Person.lname: lname}
    # )

    schema = PersonSchema()
    update = schema.load(person)
    update.person_id = person_id

    db.session.merge(update)
    db.session.commit()

    return schema.dump(update)

        
def delete(person_id):
    Person.query.filter(Person.person_id == person_id).delete()