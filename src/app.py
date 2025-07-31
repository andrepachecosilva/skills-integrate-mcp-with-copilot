"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import os
from pathlib import Path
import aiosqlite
import asyncio

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")


# SQLite database path
DB_PATH = os.path.join(Path(__file__).parent, "activities.db")

# Utilitário para inicializar o banco de dados (executar uma vez)
async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                name TEXT PRIMARY KEY,
                description TEXT,
                schedule TEXT,
                max_participants INTEGER
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS participants (
                activity_name TEXT,
                email TEXT,
                PRIMARY KEY (activity_name, email),
                FOREIGN KEY (activity_name) REFERENCES activities(name)
            )
        ''')
        await db.commit()

# Inicializar banco de dados ao iniciar
@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")



@app.get("/activities")
async def get_activities():
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        activities = []
        async with db.execute("SELECT * FROM activities") as cursor:
            async for row in cursor:
                # Buscar participantes
                async with db.execute("SELECT email FROM participants WHERE activity_name = ?", (row["name"],)) as pcur:
                    participants = [p[0] async for p in pcur]
                activities.append({
                    "name": row["name"],
                    "description": row["description"],
                    "schedule": row["schedule"],
                    "max_participants": row["max_participants"],
                    "participants": participants
                })
        return {a["name"]: a for a in activities}



@app.post("/activities/{activity_name}/signup")
async def signup_for_activity(activity_name: str, email: str):
    async with aiosqlite.connect(DB_PATH) as db:
        # Verifica se a atividade existe
        async with db.execute("SELECT 1 FROM activities WHERE name = ?", (activity_name,)) as cursor:
            exists = await cursor.fetchone()
        if not exists:
            raise HTTPException(status_code=404, detail="Activity not found")

        # Verifica se já está inscrito
        async with db.execute("SELECT 1 FROM participants WHERE activity_name = ? AND email = ?", (activity_name, email)) as cursor:
            already = await cursor.fetchone()
        if already:
            raise HTTPException(status_code=400, detail="Student is already signed up")

        # Inscreve o aluno
        await db.execute("INSERT INTO participants (activity_name, email) VALUES (?, ?)", (activity_name, email))
        await db.commit()
        return {"message": f"Signed up {email} for {activity_name}"}



@app.delete("/activities/{activity_name}/unregister")
async def unregister_from_activity(activity_name: str, email: str):
    async with aiosqlite.connect(DB_PATH) as db:
        # Verifica se a atividade existe
        async with db.execute("SELECT 1 FROM activities WHERE name = ?", (activity_name,)) as cursor:
            exists = await cursor.fetchone()
        if not exists:
            raise HTTPException(status_code=404, detail="Activity not found")

        # Verifica se está inscrito
        async with db.execute("SELECT 1 FROM participants WHERE activity_name = ? AND email = ?", (activity_name, email)) as cursor:
            insc = await cursor.fetchone()
        if not insc:
            raise HTTPException(status_code=400, detail="Student is not signed up for this activity")

        # Remove inscrição
        await db.execute("DELETE FROM participants WHERE activity_name = ? AND email = ?", (activity_name, email))
        await db.commit()
        return {"message": f"Unregistered {email} from {activity_name}"}
