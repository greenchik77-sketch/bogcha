from pydantic import BaseModel, Field

class CommentSchema(BaseModel):
    kindergarten_id: int
    comment: str
    rating: int = Field(gt=0, le=5)
