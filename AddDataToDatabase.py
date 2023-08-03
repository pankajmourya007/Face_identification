import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("facerecognition-83891-firebase-adminsdk-c8ed1-01e8634b75.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognition-83891-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "123456":
        {
            "Name": "Manvendra Sir",
        },
    "321654":
        {
            "Name": "Sandhya",
        },
    "852741":
        {
            "Name": "Emily",
        },
    "963852":
        {
            "Name": "Elon",
        },
    "234561":
        {
            "Name": "Aditi",
        },
    "316578":
        {
            "Name": "Dilpreet",
        },
    "323456":
        {
            "Name": "Yogendra",
        },
    "723456":
        {
            "Name": "Aman",
        },
    "765432":
        {
            "Name": "Ravi",
        }





}

for key, value in data.items():
    ref.child(key).set(value)