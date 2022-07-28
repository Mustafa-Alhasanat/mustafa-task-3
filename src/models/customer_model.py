from pydantic import BaseModel
from src.models.gender import Gender


class CustomerRequest(BaseModel):
  first_name: str
  last_name: str
  age: int
  gender: Gender
  adult: bool
  address_id: int
