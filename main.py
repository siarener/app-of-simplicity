from src.log_writer import load_config, write_logs


def main():
    config = load_config()
    file_path = config["files"]["log_text"]
    write_logs(file_path)


if __name__ == "__main__":
    main()
