from flask import Blueprint
from flask_restx import Resource
from flask_pydantic import validate

from src.app import api, customer_model
from src.db.database import db_session as db
from src.db.customer import Customer
from src.models.customer_model import CustomerRequest
from src.models.gender import Gender


customers_blueprint = Blueprint("customer", __name__, static_folder="static", template_folder="templates")


@api.route("/customer/<int:id>/")
class CustomerController(Resource):
    def get(self, id):
        customer = Customer.query.filter_by(id=id).first() 

        if customer is None:
            return "Customer not found", 404

        response_data = {
            "id": customer.id,
            "first_name": customer.first_name, 
            "last_name": customer.last_name, 
            "age": customer.age, 
            "gender": customer.gender, 
            "adult": customer.adult, 
            "address_id": customer.address_id
        } 

        return response_data, 200
        

    @api.expect(customer_model)
    @validate()
    def put(self, id, body: CustomerRequest):
        customer = Customer.query.filter_by(id=id).first()
        
        if customer is None:
            return "Customer not found", 404
        
        for key in ["first_name", "last_name", "age", "gender", "adult", "address_id"]:
            exec(f"setattr(customer, key, body.{key})")

        db.commit()

        response_data = {
            "id": customer.id,
            "first_name": customer.first_name, 
            "last_name": customer.last_name, 
            "age": customer.age, 
            "gender": customer.gender, 
            "adult": customer.adult, 
            "address_id": customer.address_id
        } 

        return response_data, 200
    

    def delete(self, id):
        customer = Customer.query.filter_by(id=id)

        if customer is None:
            return "Customer not found", 404

        customer.delete()
        db.commit()

        return "Customer has been deleted !", 200
    

@api.route("/customer/")
class CustomersController(Resource):
    def get(self):
        all_customers = Customer.query.all()

        if all_customers is None:
            return "Customers not found", 404

        response_data = { customer.id : \
            {
                "first_name": customer.first_name, 
                "last_name": customer.last_name, 
                "age": customer.age, 
                "gender": customer.gender, 
                "adult": customer.adult, 
                "address_id": customer.address_id
            } \
            for customer in all_customers}

        return response_data, 200
    

    @api.expect(customer_model)
    @validate()
    def post(self, body: CustomerRequest):

        first_name = body.first_name 
        last_name = body.last_name 
        age = body.age 
        gender = body.gender 
        adult = body.adult
        address_id = body.address_id

        gender_obj = Gender(gender)
        
        customer = Customer(first_name, last_name, age, gender_obj, adult, address_id)
        
        db.add(customer)
        db.commit()

        response_data = {
            "id": customer.id, 
            "first_name": customer.first_name, 
            "last_name": customer.last_name, 
            "age": customer.age, 
            "gender": customer.gender, 
            "adult": customer.adult, 
            "address_id": customer.address_id
        }

        return response_data, 200

