import app
import uvicorn
if __name__ == "__main__":
    uvicorn.run("app:API", host="0.0.0.0", port=3000, debug=True)
