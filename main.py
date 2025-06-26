from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import register, recognize, history, absent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your Flutter IP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(register.router)
app.include_router(recognize.router)
app.include_router(history.router)
app.include_router(absent.router)
