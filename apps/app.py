from fastapi import FastAPI, Request
from typing import Union
import uvicorn
import pymongo

app = FastAPI()

# myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myClient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
myDb = myClient["model"]
myCol = myDb["deployments"]

# Function


# get current count of data -> return the next id
@app.get("/model/deployments/counts")
def read_root():
    result = myCol.count_documents({})
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


if __name__ == '__main__':
	uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True) # 若有 rewrite file 可能不行 reload=True，不然會一直重開 by 李忠大師