import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/")
async def p_index():
    return {"FIO": "Жерносенко Елизавета Александровна"}


@app.get("/users",response_class=HTMLResponse)
async def p_users():
    output ="<h3> Номер: 89628023376 </h3>"
    return output

@app.get("/tools",response_class=HTMLResponse)
async def p_tools():
    output = "<h2> Artist </h2>"
    return output


