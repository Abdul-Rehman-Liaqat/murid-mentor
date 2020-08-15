from typing import Optional, Union, Dict, List

from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

from random import randint


class Features(BaseModel):
	features: Dict[str,Union[int,str, List[int]]]

class Student_info(BaseModel):
	student_id: int
	features: Features

def predict(features: Features):
	prediction = randint(100,1000)
	return prediction

app = FastAPI()

@app.post("/predict")
def response(student_data: Student_info):
	response = {
	"student_id" : student_data.student_id,
	"monthly_fee_capacity": predict(student_data.features)
	}
	return response
