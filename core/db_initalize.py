from core.db import *
from core.db_models import *
from core.utils import *

def initialize_database():
    # Create all tables in the database
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

    # Insert seed data if table is empty
    with SessionLocal() as db:
        # Check if the table has any data
        existing_data = db.query(Data).first()
        if not existing_data:  # If no data exists, insert seed data
            print("Inserting seed data...")
            try:
                for data in read_json("seed_data.json"):
                    new_data = Data(**data)
                    db.add(new_data)
                db.commit()
                print("Seed data inserted successfully!")
            except IntegrityError:
                db.rollback()
                print("Seed data insertion failed: Duplicate entry or other error.")
        else:
            print("Table already contains data, skipping seed insertion.")
