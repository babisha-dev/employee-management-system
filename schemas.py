from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    name: str
    department: str


class EmployeeUpdate(BaseModel):
    name: str
    department: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str

    model_config = ConfigDict(from_attributes=True)
