from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS (para o front-end acessar a API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque pelo domínio do seu front-end
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo Pydantic para validação
class Lead(BaseModel):
    email: str

# "Banco de dados" temporário (em memória)
leads_db = []

@app.post("/api/leads")
async def create_lead(lead: Lead):
    leads_db.append(lead.email)
    print(f"E-mail salvo: {lead.email}")  # Para debug
    return {"message": "E-mail cadastrado com sucesso!"}

@app.get("/api/leads")
async def get_leads():
    return {"leads": leads_db}