# Kairos v1.0 - Advanced Parameter Finder
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/hackinter/Archer/releases)
[![GitHub](https://img.shields.io/badge/GITHUB-HACKINTER-red.svg)](https://github.com/hackinter)

**Kairos** is a powerful tool designed to extract parameters from URLs or subdomains. It can process both individual URLs and a list of URLs from a file. This tool is useful for web security assessments, bug bounty hunting, and gathering parameter information from websites.

## Features
- Extracts parameters from URLs or subdomains.
- Supports both individual URLs and bulk URLs from a file.
- Multi-threading for faster processing.
- Custom header support for advanced requests.
- Output unique parameters in a text file.
- Works well for penetration testing and security audits.

## Installation

### Prerequisites
Make sure you have **Python 3.x** installed on your system.

You can download and install Python from [python.org](https://www.python.org/).

### Install Dependencies
To install the required Python libraries, run the following command:

```bash
pip install -r requirements.txt
```

This will install the necessary dependencies such as `requests` and `beautifulsoup4`.

## Usage

### Process a file with subdomains/URLs:
To process a file containing a list of URLs or subdomains, use the following command:

```bash
python kairos.py -i subdomains.txt -o parameters.txt
```

This will extract parameters from all the URLs listed in `subdomains.txt` and save them into `parameters.txt`.

### Process a single URL:
If you want to process a single URL, use the `-u` flag like this:

```bash
python kairos.py -u "http://example.com?query=123&token=xyz" -o parameters.txt
```

This will extract parameters from the given URL and save them in `parameters.txt`.

### Use Custom Headers:
You can specify custom headers for the HTTP requests using the `--headers` flag. For example:

```bash
python kairos.py -i subdomains.txt -o parameters.txt --headers '{"User-Agent": "Mozilla/5.0"}'
```

### Use Multi-threading for Faster Processing:
To speed up the processing, you can specify the number of threads using the `-t` flag. For example:

```bash
python kairos.py -i subdomains.txt -o parameters.txt -t 10
```

This will use 10 threads for processing the file, making it faster.

## Output
The tool will output the unique parameters extracted from the URLs into a text file (`parameters.txt` in the above examples). You can review the file for the list of parameters.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements. If you encounter any bugs or have suggestions, please open an issue.

## Contact
For any queries or issues, please contact 


[![HACKINTER](https://img.shields.io/badge/HACKINTER-MAIL-red.svg)](mailto:ceh.ec.counselor147@gmail.com) 
[![TELEGRAM](https://img.shields.io/badge/HACKINTER-T.ME-blue.svg)](https://t.me/chat_with_hackinter_bot)
[![TWITTER](https://img.shields.io/badge/HACKINTER-TWITTER-gry.svg)](https://x.com/_anonix_z)
