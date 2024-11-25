# Entry point to start the app

import uvicorn
from core.db import db_core
from ui import ui_logic


if __name__ == "__main__":
    db_core.initialize_database()
    uvicorn.run("core.__init__:api", host="127.0.0.1", port=8082, reload=True)
    # ui_logic.run(debug=True, host="127.0.0.1", port=8083)  # Accessible on your local network at port 5001
    