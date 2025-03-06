import sys
from datetime import datetime

def logging(log_file):
    try: 
        with open(log_file, "a") as f:
            while True:
                line = sys.stdin.readline().strip()
                if line == "QUIT":
                    break
                if not line:
                    continue
                parts = line.split(" ",1)
                action = parts[0]
                message = parts[1] if len(parts) > 1 else ""
                if not action:
                    continue
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp} [{action}] {message}\n"
                f.write(log_entry)
                f.flush()
    except Exception as e:
        print(f"Logger Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python logger.py <logfile>")
        sys.exit(1)
    logging(sys.argv[1])
