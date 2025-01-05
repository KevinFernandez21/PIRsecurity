from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nombre: str
    correo: EmailStr

class UserCreate(UserBase):
    contrasena: str

class UserOut(UserBase):
    id: int
    rol: str

    class Config:
        orm_mode = True
