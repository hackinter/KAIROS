import re
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import json

# ASCII Art
def print_ascii_art():
    art = """
 ▗▖ ▗▖ ▗▄▖ ▗▄▄▄▖▗▄▄▖  ▗▄▖  ▗▄▄▖
 ▐▌▗▞▘▐▌ ▐▌  █  ▐▌ ▐▌▐▌ ▐▌▐▌   
 ▐▛▚▖ ▐▛▀▜▌  █  ▐▛▀▚▖▐▌ ▐▌ ▝▀▚▖
 ▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▐▌ ▐▌▝▚▄▞▘▗▄▄▞▘
                                   
Parameter Finder Tool v1.0
"""
    print(art)

# Extract parameters from a URL using a more comprehensive approach
def extract_parameters(url):
    """Extracts parameters from a single URL using a more comprehensive approach."""
    try:
        # Capture parameters after '?' or '&' in the URL, including values
        parameters = re.findall(r'[?&](\w+)=([^&]*)', url)
        return [param[0] for param in parameters]
    except Exception as e:
        print(f"Error extracting parameters from {url}: {e}")
        return []

# Fetch links from a webpage
def fetch_links(url, headers=None):
    """Fetches all links from a webpage."""
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error fetching links from {url}: {e}")
        return []

# Generator to process URLs or subdomains
def process_urls(urls, headers=None):
    """Processes URLs to extract links and parameters."""
    for url in urls:
        try:
            print(f"Processing: {url}")
            links = fetch_links(url, headers)
            for link in links:
                params = extract_parameters(link)
                if params:
                    yield link, params
        except Exception as e:
            print(f"Error processing {url}: {e}")

# Read URLs or subdomains from a file
def read_input_file(file_name):
    """Reads a list of URLs or subdomains from a file."""
    with open(file_name, 'r') as f:
        return f.read().splitlines()

# Save parameters to a file
def save_parameters(file_name, parameter_data):
    """Saves parameters with URLs to a file in JSON format."""
    with open(file_name, 'w') as f:
        json.dump(parameter_data, f, indent=4)

# Main function
if __name__ == "__main__":
    print_ascii_art()

    parser = argparse.ArgumentParser(
        description="Advanced Parameter Finder Tool v5.0\n"
                    "Now supports both direct URL input and subdomain file input.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-i", "--input", help="Input file containing URLs or subdomains")
    parser.add_argument("-u", "--url", help="Single URL to process directly")
    parser.add_argument("-o", "--output", default="parameters.json", help="Output file (default: parameters.json)")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads for processing (default: 5)")
    parser.add_argument("--headers", help="Custom headers for requests (JSON format)")

    args = parser.parse_args()

    # Parse custom headers
    headers = None
    if args.headers:
        try:
            headers = json.loads(args.headers)
        except Exception as e:
            print(f"Error parsing headers: {e}")
            exit(1)

    # Check for input source
    if args.input:
        urls = read_input_file(args.input)
    elif args.url:
        urls = [args.url]
    else:
        print("Please provide either an input file (-i) or a single URL (-u).")
        exit(1)

    # Multi-threading for URL processing
    all_parameters = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for url, params in executor.map(lambda u: list(process_urls([u], headers)), urls):
            if params:
                all_parameters.append({"url": url, "parameters": params})

    # Save parameters along with URLs in JSON format
    save_parameters(args.output, all_parameters)

    print(f"\nExtracted {len(all_parameters)} unique URLs with parameters.")
    print(f"Saved to {args.output}")
