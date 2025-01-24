import argparse
import subprocess


def do_rsync(src, dest):
    rsync_command = ["rsync", "-rauvt", "--delete", src, dest]
    try:
        process = subprocess.Popen(
            rsync_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        while True:
            stdout_line = process.stdout.readline()
            stderr_line = process.stderr.readline()
            if stdout_line:
                print("Stdout:", stdout_line.strip())
            if stderr_line:
                print("Stderr:", stderr_line.strip())
            # 检查进程是否已结束
            if process.poll() is not None:
                break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some inputs.")
    parser.add_argument("--src", type=str, required=True)
    parser.add_argument("--dest", type=str, required=True)
    args = parser.parse_args()

    do_rsync(args.src, args.dest)
