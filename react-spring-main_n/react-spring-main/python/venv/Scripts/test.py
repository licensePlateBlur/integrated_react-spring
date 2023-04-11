import pymongo
from urllib import parse

def main():
    host = "localhost"
    port = "27017"
    user = "user1"
    pwd = "1234"
    db = "testdb"

    client = pymongo.MongoClient("mongodb://{}:".format(user) + parse.quote(pwd) + "@{}:{}/{}".format(host,port,db))

    # for d in client.list_databases():
    #     print(d)
    db_conn=client.get_database(db)

    collection = db_conn.get_collection("testcollcection")
    
    results = collection.find()

    for data in results:
        print(data)
    # for col in db_conn.list_collection_names():
    #     print(col)



main()