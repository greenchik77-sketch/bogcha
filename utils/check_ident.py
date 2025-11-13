from fastapi import HTTPException


def check_ident(db, model, ident):

    obj = db.query(model).filter(model.id == ident).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")
