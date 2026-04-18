import os
import subprocess
import time

SCRIPT_PATH = "scripts/user_script.py"

def run_code(code: str):
    try:
        start = time.time()

        # Save user code
        with open(SCRIPT_PATH, "w") as f:
            f.write(code)

        # Run Docker container
        result = subprocess.run(
            [
                "docker", "run",
                "--rm",
                "-v", f"{os.getcwd().replace('\\','/')}/scripts:/app",
                "gaas-image"
            ],
            capture_output=True,
            text=True,
            timeout=60
        )

        end = time.time()

        if result.returncode != 0:
            return {
                "error": result.stderr,
                "execution_time": f"{round(end - start, 2)} sec"
            }

        return {
            "output": result.stdout,
            "execution_time": f"{round(end - start, 2)} sec"
        }

    except Exception as e:
        return {"error": str(e)}