from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from bd import Familia

app = FastAPI()

@app.get('/index')
async def home():
  return Familia

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)