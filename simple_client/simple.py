import sys
from cache_mode import run_cache_mode
from read_mode import run_read_mode


def main():
    # Parse command line arguments
    mode = sys.argv[1]  # --mode=cache or --mode=read
    if mode == "--mode=cache":
        times = int(sys.argv[2].split("=")[1])  # --times=10
        run_cache_mode(times)
    elif mode == "--mode=read":
        run_read_mode()
    else:
        print("Invalid mode selected. Use --mode=cache or --mode=read")


if __name__ == "__main__":
    main()
