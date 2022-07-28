from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, fields


app = Flask(__name__)
api = Api(app)

customer_model = api.model(
    'customer',
    {
        'first_name':  fields.String("Mustafa", required=True),
        'last_name':  fields.String("Hasanat", required=True),
        'age':  fields.Integer(23, required=True),
        'gender':  fields.String("male", required=True),
        'adult':  fields.Boolean(True, required=True),
        'address_id':  fields.Integer(0, required=True)
    }
)

address_model = api.model(
    'address',
    {
        'phone':  fields.String("+962700000000", required=True),
        'email':  fields.String("m@m.com", required=True),
        'country':  fields.String("Jordan", required=True),
        'city':  fields.String("Amman", required=True),
        'street':  fields.String("none", required=True)
    }
)



app.run(host="127.0.0.1")

from src.controllers.customer_controller import customers_blueprint
from src.controllers.address_controller import addresses_blueprint

app.register_blueprint(customers_blueprint, url_prefix="/customer")
app.register_blueprint(addresses_blueprint, url_prefix="/address")
