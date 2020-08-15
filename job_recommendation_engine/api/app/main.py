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

def predict(features: Features, number_of_recommendations = 5):
	prediction = [randint(100,1000) for i in range(number_of_recommendations)]
	return prediction

app = FastAPI()

@app.post("/predict")
def response(student_data: Student_info):
	response = {
	"student_id" : student_data.student_id,
	"job_ids": predict(student_data.features)
	}
	return response