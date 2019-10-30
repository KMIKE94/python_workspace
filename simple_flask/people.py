from datetime import datetime

from flask import make_response, abort

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
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE.get(lname)
    
    else:
        abort (
            404, "Person with last name {lname} not found".format(lname=lname)
        )

def create(person):
    fname = person.get("fname", None)
    lname = person.get("lname", None)
    timestamp = get_timestamp()

    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": timestamp
        }
        return make_response(
            "{lname} successfully created".format(lname=lname)
        )
    else:
        abort(
            406, "Person with {lname} already exists".format(lname=lname)
        )

def update(lname, person):
    fname = person.get("fname", None)

    if lname in PEOPLE and lname is not None:
        PEOPLE[lname]["fname"] = person.get("fname", None)
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return make_response(
            "Successfully updated person {lname}".format(lname=lname)
        )
    else:
        abort(
            404, "Person with {lname} does not exist".format(lname=lname)
        )
        
def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "Successfully deleted {lname} from list".format(lname=lname)
        )
    else:
        abort(
            404, "Person with last name \"{lname}\" does not exist".format(lname=lname)
        )