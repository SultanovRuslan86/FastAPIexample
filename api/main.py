from fastapi import FastAPI, status
from .db import metadata, database, engine, Article
from .schemas import ArticleSchema

app = FastAPI()

metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/articles')
async def list_articles():
    return {'message': 'List of articles'}


@app.get('/all_articles', status_code=status.HTTP_200_OK)
async def all_articles():
    list_of_articles = await Article.objects.get.all()
    return list_of_articles


@app.post('/post-article', status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleSchema):
    query = Article.insert().values(
        title=article.title,
        description=article.description
    )
    last_record = await database.execute(query)
    return {**article.dict(), "id": last_record}




