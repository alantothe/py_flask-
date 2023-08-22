from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import json


f = open('master.json')

data = json.load(f)

print(data)


db = PostgresqlDatabase ('wine', user='alanmalpartida', password='',
                         host='localhost', port=5432)
app = Flask(__name__)

class BaseModel(Model):
    class Meta:
        database = db
        
class Wine(BaseModel):
    WineName = CharField()
    ProductType = CharField()
    Price = DecimalField()
    CountryState = CharField()
    Region = CharField()
    VarietalType = CharField()
    Description = TextField()
    img = CharField()
    flag =CharField()
    
    
db.connect()
db.drop_tables([Wine])
db.create_tables([Wine])

Wine.insert_many(data).execute()





@app.route('/')
def index():
    return "ALANTOTHE"

@app.route('/wine/', methods=['GET', 'POST'])
@app.route('/wine/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Wine.get(Wine.id == id)))
    else:
        wine_list = []
        for wine in Wine.select():
            wine_list.append(model_to_dict(wine))
        return jsonify(wine_list)

  if request.method == 'POST':
    new_wine = dict_to_model(Wine, request.get_json())
    new_wine.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Wine.delete().where(Wine.id == id).execute()
    return "Person " + str(id) + " deleted."

app.run(port=4000)