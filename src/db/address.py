from sqlalchemy import Column, Integer, String

from src.db.database import Base


class Address(Base):
  __tablename__ = "fake_address_db"

  id = Column("id", Integer, primary_key=True)
  phone = Column("phone", String(50), nullable=False)
  email = Column("email", String(50), nullable=False)
  country = Column("country", String(50), nullable=False)
  city = Column("city", String(50), nullable=False)
  street = Column("street", String(50), nullable=False)

  def __init__(self, 
    phone=None, 
    email=None, 
    country=None,
    city=None,
    street=None):

      self.phone = phone
      self.email = email
      self.country = country
      self.city = city
      self.street = street
      
