from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
def index():
    return "hello"


@app.get("/trimite_text")
def index(text: str):
    with open("fisier.txt", "w") as file:
        file.write(text)

    try:
        os.system("git add fisier.txt")
    except Exception as e:
        pass
    os.system("git commit -m 'update' ")
    os.system("git push")


uvicorn.run(app)
