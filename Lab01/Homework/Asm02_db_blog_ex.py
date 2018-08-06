from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# Connect to database
client = MongoClient(mongo_uri)
# Get database
db = client.get_default_database()
# Create new post
new_post = {
    "title": "Test",
    "author": "Tester",
    "content": "Testing"
}
# Insert new post
db.posts.insert_one(new_post)