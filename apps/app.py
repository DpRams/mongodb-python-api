from fastapi import FastAPI, Request
from typing import Union
import uvicorn
import pymongo

app = FastAPI()

# myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myClient = pymongo.MongoClient("mongodb://host.docker.internal:27017/", \
                                username="root", \
                                password="rootPassword")
myDb = myClient["model"]
myCol = myDb["deployments"]

# Function

@app.get("/")
def read_root():

    return "MongoDB-Python-API"

# get current count of data
@app.get("/model/deployments/counts")
def read_root():
    result = myCol.count_documents({})
    return result


# get max id of data
@app.get("/model/deployments/id/max")
def get_max_id():
    result = myCol.find().sort("modelId", pymongo.DESCENDING)[0]["modelId"]
    print(result)
    return result

# Read
@app.get("/model/deployments")
def read_root(key:str, value:Union[int, str]):
    result = myCol.find({key : value}, {"_id" : 0})
    result = list(result)
    return result

# Read all
@app.get("/model/deployments/all")
def read_root():
    result = myCol.find({},{"_id" : 0})
    result = list(result)
    return result

# Insert
@app.post("/model/deployments")
async def read_root(request: Request):
    # mytestData = {"modelId" : 1, "modelName" : "solar_custoNet_SLFN_0.6_0.729_221022_182027.pkl", \
    #                 "trainedDataset":"solar", "deployStatus":"revoking", "containerID": "None", \
    #                     "containerPort" : "None"}
    data = await request.json()
    myCol.insert_one(data)
    result = myCol.find_one({"modelId":data["modelId"]}, {"_id" : 0})
    return result

# Update
@app.put("/model/deployments")
async def read_root(request: Request):
    data = await request.json()
    filter = {"modelId":data["modelId"]}
    newValues = { "$set": {data["keyToBeChanged"]: data["valueToBeChanged"]} }
    myCol.update_one(filter, newValues)
    result = myCol.find_one({"modelId":data["modelId"]}, {"_id" : 0})
    return result

# Delete
@app.delete("/model/deployments")
def read_root(key:str, value:Union[int, str]):

    result = myCol.find_one({key : value}, {"_id" : 0})
    myCol.delete_one({key : value})
    return result

# Delete all
@app.delete("/model/deployments/all")
def delete_all():

    result = myCol.delete_many({})
    
    return f"{result.deleted_count} record(s) has been deleted"


if __name__ == '__main__':
	uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)