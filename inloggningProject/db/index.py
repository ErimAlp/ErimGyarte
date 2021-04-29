from dotenv import load_dotenv
import os
import pyrebase

load_dotenv()  # Läser in miljövariabeln från .env filen
config = {
    "apiKey": os.environ["FIREBASE_API_KEY"],
    "authDomain": "inloggning-96281.firebaseapp.com",
    "databaseURL": "https://inloggning-96281.firebaseio.com",
    "projectId": "inloggning-96281",
    "storageBucket": "inloggning-96281.appspot.com",
    "messagingSenderId": "438862343495",
    "appId": "1:438862343495:web:1e05f1b21abd2b1842b062",
    "measurementId": "G-6Z97E8LMYY"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
