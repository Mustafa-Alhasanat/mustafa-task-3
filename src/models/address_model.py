from pydantic import BaseModel


class AddressRequest(BaseModel):
  phone: str
  email: str
  country: str
  city: str
  street: str
