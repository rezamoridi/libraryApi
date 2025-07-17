# ❗ TODO : Import Uvicorn and use run method to run the uvicorn when ever this file has been executed
import uvicorn
from os import getenv, path,environ
from dotenv import load_dotenv

load_dotenv(path="/home/gh/Desktop/libraryApi/.env")

UVICORN_PORT = getenv("UVICORN_PORT")
UVICORN_HOST = getenv("UVICORN_HOST")
UVICORN_RELOAD = getenv("UVICORN_RELOAD")

print(UVICORN_PORT)
if __name__ == "__main__":
    uvicorn.run(
    app="config:app",
    host=UVICORN_HOST,
    port=int(UVICORN_PORT),
    reload=bool(UVICORN_RELOAD)
    )