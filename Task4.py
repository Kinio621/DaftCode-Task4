from fastapi import FastAPI, HTTPException
app = FastAPI()

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    surename: str

class PatientResp(BaseModel):
    id: int
    patient: Patient

global i
i = -1

patients = []

def increment():
    global i
    i = i + 1

@app.post('/patient', response_model=PatientResp)
def post_patient(p: Patient):
    global i
    increment()
    patients.append(p)
    return PatientResp(id=i, patient = p)

@app.get('/patient/{pk}', response_model=Patient)
def send_patient(pk: int):
    global i
    global patients
    if (i < pk):
        raise HTTPException(status_code=204, detail="Item not found")
    else:
        return patients[pk]
