from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import database
from models.comments import Comments
from models.kindergartens import Kindergartens
from models.users import Users
from schemas.comments import CommentSchema
from utils.auth import get_current_user
from utils.check_ident import check_ident

comment_router = APIRouter()


@comment_router.post("/comments")
def add_comment(comment: CommentSchema, db: Session = Depends(database),
                     user_data: Users = Depends(get_current_user)):

    check_ident(db, Kindergartens, comment.kindergarten_id)

    kindergarten = db.query(Kindergartens).filter(Kindergartens.id == comment.kindergarten_id).first()
    kindergarten.rating_sum += comment.rating
    kindergarten.rating_count += 1
    kindergarten.rating = round(kindergarten.rating_sum / kindergarten.rating_count, 1)


    db.commit()

    comment = Comments(
        user_id=user_data.id,
        kindergarten_id=comment.kindergarten_id,
        comment=comment.comment,
        rating=comment.rating
    )
    db.add(comment)
    db.commit()
    raise HTTPException(status_code=201, detail="Comment added successfully")



@comment_router.get("/get_comments")
def get_comments(db: Session = Depends(database)):
    return db.query(Comments).all()


@comment_router.delete("/delete_comments")
def delete_comment(comment_id: int, db: Session = Depends(database),
                   user_data: Users = Depends(get_current_user)):
    comment = db.query(Comments).filter(Comments.id == comment_id, Comments.user_id == user_data.id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(comment)
    db.commit()
    raise HTTPException(status_code=204, detail="Comment deleted successfully")