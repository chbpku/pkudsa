from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
headers = {
    'Cookie': '_ga=GA1.2.387593542.1617107630; _gid=GA1.2.1534665002.1617107630; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1617107630,1617109657; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1617110185; kw_token=QUE6LY91RKT',
    'csrf': 'QUE6LY91RKT',
    'Host': 'www.kuwo.cn',
    'Referer': 'http://www.kuwo.cn/search/list?key=fuck',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
app = FastAPI()

class status:
    data = 1
    changed = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/status")
async def music(id: int):
    status.data = id
    status.changed = True
    return status.data

@app.get("/data")
async def data():
    if status.changed:
        status.changed = False
        return status.data
    else:
        return 0