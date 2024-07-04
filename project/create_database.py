from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create (or use existing) database
db = client['companyDatabase']

# Create Users Collection
users_collection = db['users']

# Insert sample users
users = [
    {
        "name": "John Doe",
        "type": "employee",
        "group_id": ObjectId("60d5ec49f2954a4e4c8b4568")
    },
    {
        "name": "Jane Smith",
        "type": "manager",
        "group_id": ObjectId("60d5ec49f2954a4e4c8b4568")
    }
]

users_collection.insert_many(users)

# Create Projects Collection
projects_collection = db['projects']

# Insert sample projects
projects = [
    {
        "group_id": ObjectId("60d5ec49f2954a4e4c8b4568"),
        "service_name": "AWS",
        "project_name": "Cloud Migration",
        "users": [
            ObjectId("60d5ec49f2954a4e4c8b4567"),  # Example user IDs
            ObjectId("60d5ec49f2954a4e4c8b4570")
        ]
    },
    {
        "group_id": ObjectId("60d5ec49f2954a4e4c8b4568"),
        "service_name": "GitHub",
        "project_name": "DevOps Automation",
        "users": [
            ObjectId("60d5ec49f2954a4e4c8b4567"),
            ObjectId("60d5ec49f2954a4e4c8b4571")
        ]
    }
]

projects_collection.insert_many(projects)

# Create Types of Services Collection
services_collection = db['services']

# Insert sample services
services = [
    {
        "_id": ObjectId("60d5ec49f2954a4e4c8b4580"),
        "service_name": "AWS"
    },
    {
        "_id": ObjectId("60d5ec49f2954a4e4c8b4581"),
        "service_name": "GitHub"
    },
    {
        "_id": ObjectId("60d5ec49f2954a4e4c8b4582"),
        "service_name": "GCloud"
    }
]

services_collection.insert_many(services)

# Create Teams Collection
teams_collection = db['teams']

# Insert sample teams
teams = [
    {
        "name": "Development Team",
        "members": [
            ObjectId("60d5ec49f2954a4e4c8b4567"),
            ObjectId("60d5ec49f2954a4e4c8b4568")
        ]
    },
    {
        "name": "Operations Team",
        "members": [
            ObjectId("60d5ec49f2954a4e4c8b4569"),
            ObjectId("60d5ec49f2954a4e4c8b4570")
        ]
    }
]

teams_collection.insert_many(teams)

print("Database and collections created successfully!")
