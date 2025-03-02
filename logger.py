import sys
from datetime import datetime

def logging(logging_file):
    while True:
        line = sys.stdin.readline().strip()
        if line == "QUIT":
            break
        parts = line.split(" ",1)
        action = parts[0]
        message = parts[1] if len(parts) > 1 else ""
        timestamp = datetime.now().strftime("%Y-%m-%d %h:%m")
        with open(logging_file, "a") as f:
            f.write(f"{timestamp} [{action}] {message}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python logger.py <logfile>")
        sys.exit(1)
    logging(sys.argv[1])
