from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['octofit_tracker_db']

# Test collection
test_collection = db['test_collection']

# Insert a test document
test_document = {"name": "Test User", "email": "testuser@example.com"}
insert_result = test_collection.insert_one(test_document)
print(f"Inserted document ID: {insert_result.inserted_id}")

# Retrieve the inserted document
retrieved_document = test_collection.find_one({"_id": insert_result.inserted_id})
print(f"Retrieved document: {retrieved_document}")

# Clean up by deleting the test document
test_collection.delete_one({"_id": insert_result.inserted_id})
print("Test document deleted.")
