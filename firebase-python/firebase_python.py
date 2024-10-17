import datetime
from config import BaseConfig

import firebase_admin 
from firebase_admin import credentials, db

settings = BaseConfig()

# Initialize Firestore
cred = credentials.Certificate(settings.FIREBASE_CREDS_JSON)
firebase_admin.initialize_app(cred, {'databaseURL':settings.FIREBASE_DB_URL})

def add_example_data():
    poll_ref = db.reference('/polls/poll-' + str(datetime.date.today()))
    poll_ref.set({
            'question': 'Poll question',
            'option_1': 0,
            'option_2': 0,
            'option_3': 0,
            'option_4': 0,
            'total_votes': 0
        })


def main():

    # Get a database reference to our polls
    ref = db.reference('/polls')

    # Read the data at the posts reference
    print(ref.get())

    # Initialize a poll (pollID based on the date)
    add_example_data()

if __name__ == '__main__':
  main()