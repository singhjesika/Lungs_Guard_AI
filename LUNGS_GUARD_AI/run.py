import subprocess
import sys
import uvicorn


def run_api():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


def run_ui():
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "app/ui/dashboard.py"])


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "api"
    if mode == "ui":
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app/ui/dashboard.py"])
    elif mode == "both":
        run_ui()
        run_api()
    else:
        run_api()