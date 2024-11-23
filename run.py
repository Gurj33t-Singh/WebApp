# Entry point to start the app

import uvicorn
from core import db_initalize


if __name__ == "__main__":
    # uvicorn.run("core.__init__:api", host="127.0.0.1", port=8082, reload=True)
    db_initalize.initialize_database()