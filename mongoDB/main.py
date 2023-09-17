from dotenv import load_dotenv, find_dotenv
import os 
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())


password = os.environ.get("")

connection_string = f""

client = MongoClient(connection_string)



dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()

print(collections)


def insert_test_doc():
    collections = test_db.test
    test_document = {
        "name" : "Adel",
        "type" : "Test"
    }
    inserted_id = collections.insert_one(test_document).inserted_id
    print(inserted_id)

production = client.production 
person_collection = production.person_collection


def create_documents():
    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen"]
    last_names = ["Ruscica", "Smith", "Bart", "Cater", "Pit", "Geral"]
    ages = [21, 40, 23, 19, 34, 67]


    docs =[]

    for first_names, last_names,ages in zip(first_names,last_names,ages):
        doc = {"first_names": first_names, "last_names": last_names, "age":ages}
        docs.append(doc)

    person_collection.insert_many(docs)


printer = pprint.PrettyPrinter()

def find_all_people():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)



def find_tim():

    #tohle je jako filtrování "najdi jednu věc v koleci person_collection, která má první jméno Tim atd.. Můžu říct že je to vyhledávání"
    tim = person_collection.find_one({"first_name": "Tim"})

def count_all_people():
    count = person_collection.find().count()

    print("Počet všech lidí v seznamu:", count)



def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    #tady je důležité že python vnímá id jako string a my mu musíme separátně říct né toto je speciálí ID ne string
    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)


def get_age_range(min_age, max_age):
    query = {"$and": [
            {"age": {"$gte": min_age}},
            {"age": {"$lte": max_age}},            
        ]}

    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)

def project_columns():
    columns = {"_id": 0, "first_name": 1, "last_name": 1}
    people = person_collection.find({}, columns)
    for person in people:
        printer.pprint(person)

project_columns()






