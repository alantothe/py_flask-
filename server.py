from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model


db = PostgresqlDatabase ('people', user='alanmalpartida', password='',
                         host='localhost', port=5432)
app = Flask(__name__)

class BaseModel(Model):
    class Meta:
        database = db
        
class Person(BaseModel):
    name = CharField()
    age = IntegerField()
    
db.connect()
db.drop_tables([Person])
db.create_tables([Person])

Person(name='alan', age=28).save()
Person(name='Yeezus', age=300).save()

@app.route('/')
def index():
    return 'Hello World'

@app.route('/person/', methods=['GET', 'POST'])
@app.route('/person/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Person.get(Person.id == id)))
    else:
        people_list = []
        for person in Person.select():
            people_list.append(model_to_dict(person))
        return jsonify(people_list)

  if request.method =='PUT':
    body = request.get_json()
    Person.update(body).where(Person.id == id).execute()
    return "Person " + str(id) + " has been updated."

  if request.method == 'POST':
    new_person = dict_to_model(Person, request.get_json())
    new_person.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Person.delete().where(Person.id == id).execute()
    return "Person " + str(id) + " deleted."

app.run(port=4000)