from pymongo import MongoClient

# MongoDB 인스턴스에 연결
client = MongoClient('mongodb://hanslab.org:27117/')
# client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')