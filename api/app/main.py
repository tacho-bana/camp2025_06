from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.gemini import generate_recipe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # フロントエンドのURL（Next.js開発環境）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IngredientsRequest(BaseModel):
    ingredients: list[str]  

@app.get("/")
async def read_main():
    return {"msg":"Hello World"}

@app.post("/generate-recipe")
async def generate_recipe_endpoint(req: IngredientsRequest):
    recipe = await generate_recipe(req.ingredients)
    return {"recipe": recipe}
