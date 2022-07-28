from flask import Blueprint
from flask_restx import Resource
from flask_pydantic import validate

from src.app import api, address_model
from src.db.database import db_session as db
from src.db.address import Address
from src.models.address_model import AddressRequest


addresses_blueprint = Blueprint("address", __name__, static_folder="static", template_folder="templates")

@api.route("/address/<int:id>/")
class AddressController(Resource):
    def get(self, id):
        address = Address.query.filter_by(id=id).first() 

        if address is None:
            return "Address not found", 404

        response_data = {
            "id": address.id,
            "phone": address.phone, 
            "email": address.email, 
            "country": address.country, 
            "city": address.city, 
            "street": address.street 
        } 

        return response_data, 200
        

    @api.expect(address_model)
    @validate()
    def put(self, id, body: AddressRequest):
        address = Address.query.filter_by(id=id).first()
        
        if address is None:
            return "Address not found", 404
        
        for key in ["phone", "email", "country", "city", "street"]:
            exec(f"setattr(address, key, body.{key})")

        db.commit()

        response_data = {
            "id": address.id,
            "phone": address.phone, 
            "email": address.email, 
            "country": address.country, 
            "city": address.city, 
            "street": address.street 
        } 

        return response_data, 200
    

    def delete(self, id):
        address = Address.query.filter_by(id=id)

        if address is None:
            return "Address not found", 404

        address.delete()
        db.commit()

        return "Address has been deleted !", 200
    

@api.route("/address/")
class AddressesController(Resource):
    def get(self):
        all_addresses = Address.query.all()

        if all_addresses is None:
            return "Addresses not found", 404

        response_data = { address.id : \
            {
                "id": address.id,
                "phone": address.phone, 
                "email": address.email, 
                "country": address.country, 
                "city": address.city, 
                "street": address.street 
            } \
            for address in all_addresses}

        return response_data, 200
    

    @api.expect(address_model)
    @validate()
    def post(self, body: AddressRequest):

        phone = body.phone 
        email = body.email 
        country = body.country 
        city = body.city 
        street = body.street 
        
        address = Address(phone, email, country, city, street)
        
        db.add(address)
        db.commit()

        response_data = {
            "id": address.id,
            "phone": address.phone, 
            "email": address.email, 
            "country": address.country, 
            "city": address.city, 
            "street": address.street 
        }

        return response_data, 200

