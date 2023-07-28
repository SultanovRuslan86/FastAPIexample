from pydantic import BaseModel

class ArticleSchema(BaseModel):
    title: str
    description: str



