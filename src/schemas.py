from pydantic import BaseModel, EmailStr, ConfigDict

class StudentCreate(BaseModel):
    name:str
    age:int
    email:EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    email: EmailStr | None = None


    