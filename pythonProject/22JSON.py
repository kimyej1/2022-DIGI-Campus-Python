# 22JSON.py
# JavaScript Object Notation = JSON

# cf) 전치사는 약자로 쓸 때도 소문자로~
# voice over internet protocol = VoIP
# internet of things = IoT


import json

# JSON은 dict타입이므로 중괄호 사용, 모델은 여러명이니까 list타입으로 대괄호
myInfo = {"company":"KB", "city":"Seoul", "model":["김연아", "BTS", "공유"]}
print("myInfo = ", myInfo)

# json으로 만드는 행위 : 직렬화 (serialize)
json.dumps(myInfo)  # console - json으로 저장하려고~

with open("./myInfo.json", "w", encoding="UTF8") as f: # w: write(덮어쓰기) 모드
    json.dump(myInfo, f) # 화면이 아니라 f에다가~


# 역직렬화...(다시 빼오기)
with open("./myInfo.json", "r", encoding="UTF8") as f: # r: read(읽기) 모드
    readInfo = json.load(f)
    print("readInfo = ", readInfo)
    print("city = ", readInfo["city"])
