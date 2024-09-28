import sys
from utilities import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts

def main():
    if len(sys.argv) < 2:
        print("Invalid command")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    if len(sys.argv) > 2:
        level_filter = sys.argv[2]

        if level_filter.upper() not in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
            print("Invalid log level. Available levels: INFO, DEBUG, ERROR, WARNING")
            sys.exit(1)

        filtered_logs = filter_logs_by_level(logs, level_filter)
        detailed_display = True
    else:
        detailed_display = False
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if detailed_display:
        print(f"\nDetails for logs with level '{level_filter}':")
        
        for log in filtered_logs:
            print(f"{log['timestamp']} {log['level']} - {log['message']}")

if __name__ == "__main__":
    main()