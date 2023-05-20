'''App builder that starts the server'''
import uvicorn
from app.app import build_app

app = build_app()

if __name__ == "__main__":
    uvicorn.run(app)
