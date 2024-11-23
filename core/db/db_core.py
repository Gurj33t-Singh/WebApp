from core.db import db_conn
from core.db import db_models
from core import utils

def initialize_database():
    # Create all tables in the database
    print("Creating tables...")
    db_conn.Base.metadata.create_all(db_conn.engine)
    print("Tables created successfully!")

    seed_data(db_models.Data, "seed_data.json")
   
def seed_data(data_model, seed_data_path):

    db = next(get_db())
    # Check if the table has any data
    existing_data = db.query(data_model).first()
    if not existing_data:  # If no data exists, insert seed data
        print("Inserting seed data...")
        try:
            for data in utils.read_json(seed_data_path):
                new_data = data_model(**data)
                db.add(new_data)
            db.commit()
            print("Seed data inserted successfully!")
        except db_conn.IntegrityError:
            db.rollback()
            print("Seed data insertion failed: Duplicate entry or other error.")
    else:
        print("Table already contains data, skipping seed insertion.")

# Dependency for getting DB session
def get_db():
    db = db_conn.db_session()
    try:
        yield db
    finally:
        db.close()