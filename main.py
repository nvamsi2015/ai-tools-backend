from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get('/fakestore')
async def get_dashboard():
    print('new request received')
    async with httpx.AsyncClient() as client:
        response = await client.get('https://fakestoreapi.com/products')
        print(response.status_code)
        data = response.json()
    return data
