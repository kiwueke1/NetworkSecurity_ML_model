from pymongo import MongoClient

uri = "mongodb+srv://aikezie10:admin10@cluster0.i25gd.mongodb.net/?retryWrites=true&w=majority&tls=true"

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)
