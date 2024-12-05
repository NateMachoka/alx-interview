#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
- Every 10 lines or on keyboard interruption (CTRL + C), prints statistics from
the beginning:
  - Total file size
  - Count of each status code (200, 301, 400, 401, 403, 404, 405, 500)
"""


import sys


status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_file_size = 0
line_count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        try:
            parts = line.split()
            ip, date, status_code, file_size = (
                parts[0], parts[3], parts[-2], parts[-1]
                )

            # Check if status code and file size are integers
            if status_code in status_counts:
                status_counts[status_code] += 1
            total_file_size += int(file_size)
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (IndexError, ValueError):
            # Skip lines that don't match the expected format
            continue


except KeyboardInterrupt:
    # Print final stats upon keyboard interrupt
    print_stats()
    raise

# Print final stats after processing all input
print_stats()
