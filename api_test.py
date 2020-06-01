import requests as r
import json

aaa={
    "api":"docker_logs",
    "psw":"tttest",
    "args":{
        "container_id":"80df53944051"
    }
}

aaa=r.post(
    "http://127.0.0.1/server/api",json=aaa
)

bbb=json.loads(aaa.text)

get_message = bbb.get("message").split("\n")