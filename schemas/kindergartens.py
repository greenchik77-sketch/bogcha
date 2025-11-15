from enum import Enum

from pydantic import BaseModel, Field
from datetime import time

class KindergartenSchema(BaseModel):
    name: str
    region: str
    district: str
    location: str
    type: str
    programs: list
    languages: list
    price: int = Field(gt=0)
    image: str
    short: str
    phone_number: str
    capacity: int
    start_time: time
    end_time: time
    age_limit: str
    islaw: bool
    mini_gallery: list



class RegionSelect(str, Enum):
    Toshkent = "Toshkent"
    Samarqand = "Samarqand"
    Buxoro = "Buxoro"
    Jizzax = "Jizzax"
    Navoiy = "Navoiy"
    Fergana = "Farg'ona"
    Xorazm = "Xorazm"
    Surxondaryo = "Surxondaryo"
    Andijon = "Andijon"
    Namangan = "Namangan"
    Qashqadaryo = "Qashqadaryo"
    Sirdaryo = "Sirdaryo"


class TypeSelect(str, Enum):
    xususiy = 'xususiy'
    davlat = 'davlat'
    montessori = 'montessori'