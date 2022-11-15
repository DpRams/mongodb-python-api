# mongodb-python-api



## Getting started

Provide the basic CRUD operations with FastAPI.

#### GET : 透過 action_url 直接輸入參數

```python=0
import requests

key = "modelId"
value = 1
res = requests.get(f"http://127.0.0.1:8001/model/deployments?key={key}&value={value}")

print(res.json())
```

#### UPDATE : 透過 requests 接收參數

```python=0
import requests

res = requests.put("http://127.0.0.1:8001/model/deployments", json={"modelId" : 0, "keyToBeChanged" : "deployStatus", "valueToBeChanged" : "deploying"})

print(res.json())
```

#### INSERT : 透過 requests 接收參數

```python=0
import requests


res = requests.post("http://127.0.0.1:8001/model/deployments", json={"modelId" : 1, "modelName" : "solar_custoNet_SLFN_0.6_0.729_221022_182027.pkl", \
                    "trainedDataset":"solar", "deployStatus":"revoking", "containerID": "None", \
                        "containerPort" : "None"})

print(res.json())
```

#### DELETE : 透過 action_url 直接輸入參數

```python=0
import requests

key = "modelId"
value = 0
res = requests.delete(f"http://127.0.0.1:8001/model/deployments?key={key}&value={value}")

print(res.json())
```

#### 查詢目前資料筆數

```python=0
import requests

res = requests.get(f"http://127.0.0.1:8001/model/deployments/counts")

print(res.json())
```