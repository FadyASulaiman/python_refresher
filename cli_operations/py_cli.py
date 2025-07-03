if __name__ == "__main__":
    import argparse, sys, json
    from pathlib import Path
    p = argparse.ArgumentParser()
    p.add_argument("path", type = Path)
    args = p.parse_args()
    try:
        data = json.loads(args.path.read_text())
    except Exception as e:
        sys.exit(f"Invalid file: {e}")
    print(len(data))