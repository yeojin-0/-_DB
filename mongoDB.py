from pymongo import MongoClient

# MongoDB 인스턴스에 연결
#client = MongoClient('mongodb://hanslab.org:27117/')
client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

# 데이터베이스 선택 (없으면 새로 생성됨)
db = client['tutorial_db_yeojin']

# 컬렉션 선택 (없으면 새로 생성됨) -> sql table
collection = db['tutorial_collection']

# 새 문서 생성 및 삽입
#document = {"name": "Karen Miller", "age": 27, "city": "Seoul", "hooby" : "reading"}
#collection.insert_one(document)

# 모든 문서 조회
for doc in collection.find():
    print(doc)

print("======")

# 특정 조건에 맞는 문서 조회
query = {"city": "Seoul"}
documents = collection.find(query)
for doc in documents:
    print(doc)

print("======")

# 문서 삭제
collection.delete_one({"city": "Seoul"})
print("삭제되었습니다")

print("======")
#print(client.list_database_names())

# 모든 문서 조회
for doc in collection.find():
    print(doc)

