from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def custom(request: Request):
    # print(request)
    return "<h2>Heyyyyyyyyyy</h2>"
    return {
        "status": "OK", 
        "client": request.client.host,
        "method": request.method,
        "url": str(request.url),
        "client_ip": request.client.host,
        "headers": dict(request.headers),
        "query": dict(request.query_params),
        "path": request.path_params,
        "cookies": request.cookies,
        "body": await request.body(),
        # "json": await request.json(),
    }
