# Entry point to start the app

import uvicorn
from core.db import db_core


if __name__ == "__main__":
    db_core.initialize_database()
    uvicorn.run("core.__init__:api", host="127.0.0.1", port=8082, reload=True)
    