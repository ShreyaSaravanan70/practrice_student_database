from fastapi import FastAPI, status, Depends
from database import Base, engine, get_db
from sqlalchemy.orm import Session
from schemas import StudentCreate, StudentResponse
from models import Student



app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/create_student",response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session= Depends(get_db)):
    new_student=Student(
        id=student.id,
        name=student.name,
        age=student.age,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/get_students", response_model=list[StudentResponse], status_code=status.HTTP_200_OK)
def get_students(db: Session= Depends(get_db)):
    return db.query(Student).all()


# @app.update("/update_student/{student.id}", Response_model=Student)

@app.delete("/delete_student/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db:Session=Depends(get_db)):
    student = db.query(Student).filter(Student.id==student_id ).first()
    if student is None:
        return {"message":"Student not found"}
    else:
        return {"message": "Student deleted successfully"}
    