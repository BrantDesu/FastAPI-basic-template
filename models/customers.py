from typing import Optional
from pydantic import BaseModel, EmailStr

class AddressModel(BaseModel):
    city:        Optional[str]
    country:     Optional[str]
    line1:       Optional[str]
    line2:       Optional[str]
    postal_code: Optional[str]
    state:       Optional[str]

class CustomerModel(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: Optional[AddressModel]
    