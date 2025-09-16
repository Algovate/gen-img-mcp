from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
from dotenv import load_dotenv
import os

prompt = "一间有着精致窗户的花店，漂亮的木质门，摆放着花朵"

load_dotenv()

api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    print("⚠️  Warning: DASHSCOPE_API_KEY not found in environment variables.")
    print("Please set your DashScope API key in the .env file as DASHSCOPE_API_KEY=your_api_key_here")
    exit(1)
print('----sync call, please wait a moment----')
rsp = ImageSynthesis.call(api_key=api_key,
                          model="wan2.2-t2i-flash",
                          prompt=prompt,
                          n=1,
                          size='1024*1024')
print('response: %s' % rsp)
if rsp.status_code == HTTPStatus.OK:
    # 在当前目录下保存图片
    for result in rsp.output.results:
        file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
        with open('./%s' % file_name, 'wb+') as f:
            f.write(requests.get(result.url).content)
else:
    print('sync_call Failed, status_code: %s, code: %s, message: %s' %
          (rsp.status_code, rsp.code, rsp.message))