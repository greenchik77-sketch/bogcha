from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import database
from models.kindergartens import Kindergartens
from models.users import Users
from schemas.kindergartens import KindergartenSchema
from utils.auth import get_current_user
from utils.check_ident import check_ident
from utils.role_verification import admin_verification


kindergarten_router = APIRouter()



@kindergarten_router.post("/kindergartens")
def add_kindergarten(form: KindergartenSchema, db: Session = Depends(database),
                     user_data: Users = Depends(get_current_user)):

    admin_verification(user_data)

    kindergarten = Kindergartens(
        name=form.name,
        region=form.region,
        district=form.district,
        location=form.location,
        type=form.type,
        programs=form.programs,
        languages=form.languages,
        price=form.price,
        rating=0,
        image=form.image,
        short=form.short,
        phone_number=form.phone_number,
        capacity=form.capacity,
        start_time=form.start_time,
        end_time=form.end_time,
        age_limit=form.age_limit,
        islaw=form.islaw,
        mini_gallery=form.mini_gallery
    )
    db.add(kindergarten)
    db.commit()
    raise HTTPException(status_code=201, detail="Kindergarten added successfully")


@kindergarten_router.get("/kindergartens")
def get_all_kindergartens(db: Session = Depends(database)):
    return db.query(Kindergartens).all()


@kindergarten_router.put("/kindergartens")
def update_kindergarten(ident: int, form: KindergartenSchema, db: Session = Depends(database),
                        user_data: Users = Depends(get_current_user)):
    admin_verification(user_data)

    check_ident(db, Kindergartens, ident)

    db.query(Kindergartens).filter(Kindergartens.id == ident).update({
        Kindergartens.name: form.name,
        Kindergartens.region: form.region,
        Kindergartens.district: form.district,
        Kindergartens.location: form.location,
        Kindergartens.type: form.type,
        Kindergartens.programs: form.programs,
        Kindergartens.languages: form.languages,
        Kindergartens.price: form.price,
        Kindergartens.image: form.image,
        Kindergartens.short: form.short,
        Kindergartens.phone_number: form.phone_number,
        Kindergartens.capacity: form.capacity,
        Kindergartens.start_time: form.start_time,
        Kindergartens.end_time: form.end_time,
        Kindergartens.age_limit: form.age_limit,
        Kindergartens.islaw: form.islaw,
        Kindergartens.mini_gallery: form.mini_gallery
    })
    db.commit()
    raise HTTPException(status_code=200, detail="Kindergarten updated successfully")


@kindergarten_router.delete("/kindergartens")
def delete_kindergarten(ident: int, db: Session = Depends(database),
                        user_data: Users = Depends(get_current_user)):

    admin_verification(user_data)

    check_ident(db, Kindergartens, ident)

    db.query(Kindergartens).filter(Kindergartens.id == ident).delete()
    db.commit()
    raise HTTPException(status_code=200, detail="Kindergarten deleted successfully")




