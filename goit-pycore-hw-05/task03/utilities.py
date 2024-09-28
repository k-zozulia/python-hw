import datetime
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)

    log_dict = {
        'timestamp': ''.join(parts[:2]),
        'level': parts[2],
        'message': parts[3].strip()
    }

    return log_dict

def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, "r", encoding='utf-8') as file:
            for line in file:
                logs.append(parse_log_line(line))
        return logs
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    
    except Exception as e:
        print(f"Error loading logs from file '{file_path}': {e}")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    filtered_logs = [log for log in logs if log['level'] == level]

    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    level_counts = Counter(levels)

    return level_counts

def display_log_counts(counts: dict):
    print("Logging Level| Count")
    print("-------------|------")
    
    for level, count in counts.items():
        print(f"{level.ljust(12)} | {count}")

