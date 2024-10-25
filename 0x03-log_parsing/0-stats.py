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
        Prints only none zero status code counts.

        Args:
            status (dict): status_codes
            file_size (int): total file size
        """
        print("File size: {:d}".format(file_size))

        for code, count in sorted(status_counts.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                status_codes = parts[-2]
                if status_codes in status_counts:
                    status_counts[status_codes] += 1
            except BaseException:
                pass

            try:
                file_size = int(parts[-1])

            except BaseException:
                pass

            if line_count % 10 == 0:
                print_metrics(status_counts, filesize)

            print_metrics(status_counts, filesize)

    except KeyboardInterrupt:
        print_metrics(status_counts, filesize)
        raise
