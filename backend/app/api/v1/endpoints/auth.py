from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserOut
from app.db.models.user import User
from app.core.security import hash_password, verify_password

router = APIRouter()

# Dependency para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.correo == user.correo).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    hashed_password = hash_password(user.contrasena)
    db_user = User(
        nombre=user.nombre,
        correo=user.correo,
        contrasena=hashed_password,
        rol="colaborador"  # Rol predeterminado
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
