import fastapi

app = fastapi.FastAPI()


@app.get("/endpoint")
async def endpoint():
    try:
        with open("endpoint.value") as fd:
            value = int(fd.read())
    except FileNotFoundError:
        value = 0

    return {"value": value}
