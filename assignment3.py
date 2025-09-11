import argparse
import urllib.request
import logging
import datetime
import csv
import io


def download_data(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def process_file(log_text):
    csv_data = csv.reader(io.StringIO(log_text))

    line_counter = 0
    png_counter = 0
    gif_counter = 0
    browser_counter_dict = {
        "Chrome": 0,
        "Firefox": 0,
        "MSIE": 0,
        "Safari": 0
    }
    for row in csv_data:
        line_counter += 1

        # Part III - Count how many images are in the file (you should use regular Expressions)
        path_to_file = row[0]
        date_access = row[1]
        browser = row[2]

        if path_to_file.lower().find(".png") != -1:
            png_counter += 1
        elif path_to_file.lower().find(".gif") != -1:
            gif_counter += 1

        # Part IV: Finding Most Popular Browser (User regex as well)
        if browser.lower().find("firefox") != -1:
            browser_counter_dict["Firefox"] += 1
        # ...
        # print(row)

    print(f"Average PNG hits = {((png_counter + gif_counter) / line_counter) * 100}%")
    print(f"Firefox browser hits = {browser_counter_dict['Firefox']}")


def main(url):
    print(f"Running main with URL = {url}...")
    response_text = download_data(url)
    process_file(response_text)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)