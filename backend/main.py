from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, Lead

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://km-homefit-fastapi.onrender.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/leads", status_code=status.HTTP_201_CREATED)
async def create_lead(email: str, db: Session = Depends(get_db)):
    if not email or "@" not in email:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Formato de e-mail inválido"
        )
    
    db_lead = db.query(Lead).filter(Lead.email == email).first()
    if db_lead:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado"
        )
    
    new_lead = Lead(email=email)
    db.add(new_lead)
    try:
        db.commit()
        return {"message": "E-mail salvo com sucesso!"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao salvar no banco: {str(e)}"
        )

@app.get("/api/leads")
async def get_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).all()
    return {"leads": [lead.email for lead in leads]}