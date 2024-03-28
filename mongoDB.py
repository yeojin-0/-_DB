from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

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

def doc_collection_delete():
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

    # 모든 문서 조회
    for doc in collection.find():
        print(doc)

print("======")
#print(client.list_database_names())

print(db.list_collection_names())

users = db['users'] # users라는 이름의 collection을 생성한다 cf. sql의 table

# 'email' 필드에 대한 인덱스 생성
users.create_index([('email', 1)], unique=True)

try:
    users.insert_many(
        [
        {"name": "John Doe", "email": "john1@example.com"},
        {"name": "Jane Doe", "email": "jane@example.com"}
    ]
        )
    print("Documents inserted successfully.")
except Exception as e:
    print("An error occurred:", e)

# 모든 문서 조회
for doc in users.find():
    print(doc)

try:
    result = users.update_many(
        {"name": {"$regex": "^J"}},  # 이름이 J로 시작하는 모든 문서
        {"$set": {"status": "verified"}}
    )
    print(f"{result.matched_count} documents matched, {result.modified_count} documents updated.")
except Exception as e:
    print("An error occurred:", e)

try:
    result = users.delete_many({"status": "verified"})
    print(f"{result.deleted_count} documents deleted.")
except Exception as e:
    print("An error occurred:", e)


# 심화 내용 실습

try:
    users.insert_one({"email": "john@example.com"})  # 이미 존재하는 이메일
except DuplicateKeyError as e:
    print("Duplicate key error:", e)
except Exception as e:
    print("An error occurred:", e)

collection = db['users1'] #바꾸기

# 기존 데이터가 있다면 삭제 (새로운 실습을 위해)
collection.delete_many({})

# 샘플 데이터 삽입
sample_users = [
    {"name": "Alice", "team":"lion", "age": 25, "status": "active"},
    {"name": "Bob", "age": 30, "status": "inactive","team":"tiger"},
    {"name": "Charlie", "age": 35, "status": "active","team":"tiger"},
    {"name": "David", "age": 40, "status": "active","team":"lion"},
    {"name": "Eve", "age": 25, "status": "active","team":"king"},
    {"name": "Frank", "age": 30, "status": "active","team":"lion"}
]

collection.insert_many(sample_users)