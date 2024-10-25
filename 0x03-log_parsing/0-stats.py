#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize = 0
    line_count = 0

    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_counts = {code: 0 for code in status_codes}

    def print_metrics(status_counts: dict, file_size: int) -> None:
        """
        Prints current metrics: total file size and count of each status code.
        Prints only non-zero status code counts.
        """
        print("File size: {:d}".format(file_size))
        for code, count in sorted(status_counts.items()):
            if count > 0:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

            try:
                file_size = int(parts[-1])
                filesize += file_size
            except (IndexError, ValueError):
                pass

            if line_count % 10 == 0:
                print_metrics(status_counts, filesize)

        print_metrics(status_counts, filesize)

    except KeyboardInterrupt:
        print_metrics(status_counts, filesize)
        raise
