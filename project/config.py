import os

class Config:
    MONGO_URI = "mongodb+srv://naamameypen:kJlFQ6jtZj8zK1eZ@cluster0.nh5hxwe.mongodb.net/companyDatabase?retryWrites=true&w=majority&appName=Cluster0"

def configure_app(app):
    app.config.from_object(Config)