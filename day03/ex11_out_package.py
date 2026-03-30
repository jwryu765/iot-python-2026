## ex11_out_package.py 외부라이브러리 사용

import requests

response = requests.get("https://www.google.com")

print(response.status_code) # `200` 웹페이지 요청시 정상(OK)
print(response.content) # 웹 브라우저 대신 http프로토콜로 데이터 요청