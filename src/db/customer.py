from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from src.db.database import Base


class Customer(Base):
  __tablename__ = "fake_customer_db"

  id = Column("id", Integer, primary_key=True)
  first_name = Column("first_name", String(50), nullable=False)
  last_name = Column("last_name", String(50), nullable=False)
  age = Column("age", Integer, nullable=False)
  gender = Column("gender", String(10), nullable=False)
  adult = Column("adult", Boolean, nullable=False)
  address_id = Column("address_id", Integer, ForeignKey("fake_address_db.id"), nullable=False)

  def __init__(self, 
    first_name=None, 
    last_name=None, 
    age=None,
    gender=None,
    adult=None,
    address_id=None
    ):

      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      self.gender = gender
      self.adult = adult
      self.address_id = address_id
      
      
