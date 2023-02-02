from api import app

@app.get("/")
async def root_endpoint():
    return {"message": "Serverless function is alive powered by vercel and findthatmeme.com 💪"}