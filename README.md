# Kairos v1.0 - Advanced Parameter Finder
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/hackinter/Archer/releases)
[![GitHub](https://img.shields.io/badge/GITHUB-HACKINTER-red.svg)](https://github.com/hackinter)

**Kairos** is a powerful and advanced tool designed to extract parameters from URLs or subdomains. Whether you need to extract parameters from a single URL or bulk URLs from a file, Kairos provides you with an efficient, multi-threaded solution for fast web security assessments, bug bounty hunting, and web scraping tasks.

## Features 🚀

- 🕵️‍♂️ Extracts query parameters from individual URLs or bulk URLs from a file.
- ⚡ Supports multi-threaded processing for faster extraction.
- 🔐 Handles both GET parameters and POST-based data.
- 🛠️ Custom HTTP headers support for bypassing certain security measures.
- 📥 Saves unique parameters into a file for later analysis.
- ✅ Useful for penetration testing, security audits, and bug bounty hunting.

## Installation 💻

### Prerequisites ⚙️
Ensure you have **Python 3.x** installed on your system. If not, download and install Python from the official site:

[![Python Download](https://img.shields.io/badge/PYTHON-DOWNLOAD-blue.svg)](https://www.python.org/downloads/)

### Install Dependencies 📦
Before running the tool, install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

This will install the required libraries such as `requests`, `beautifulsoup4`, and others for the tool to work seamlessly.

## Usage 🎯

### Process a file with subdomains/URLs 📄:
To process a file containing a list of URLs or subdomains, use the following command:

```bash
python kairos.py -i subdomains.txt -o parameters.txt
```

This command extracts parameters from all the URLs listed in `subdomains.txt` and saves them into `parameters.txt`.

### Process a single URL 🌐:
To process a single URL, use the `-u` flag as shown below:

```bash
python kairos.py -u "http://example.com?query=123&token=xyz" -o parameters.txt
```

This will extract parameters from the given URL and save them into `parameters.txt`.

### Use Custom Headers 🛡️:
Specify custom headers for the HTTP requests with the `--headers` flag. For example:

```bash
python kairos.py -i subdomains.txt -o parameters.txt --headers '{"User-Agent": "Mozilla/5.0"}'
```

### Multi-threading for Faster Processing ⚡:
Use the `-t` flag to increase the number of threads, speeding up the processing. For example, to use 10 threads:

```bash
python kairos.py -i subdomains.txt -o parameters.txt -t 10
```

### Displaying Help 🆘:
To get more details about the usage and available options, use the `-h` flag:

```bash
python kairos.py -h
```

## Output 📂
The tool will output the unique parameters extracted from the URLs into a text file (default is `parameters.txt`). This file will contain a list of all the unique parameters extracted from the URLs or subdomains.

## Example Output:
```
query
token
id
page
user
```

## License 📜
This project is licensed under the MIT License. See the [LICENSE](https://github.com/hackinter/kairos/blob/main/LICENSE) file for more details.

## Contributing 🤝
We welcome contributions! If you would like to contribute, feel free to fork the repository and submit a pull request. If you encounter any bugs or have suggestions, please open an issue.

## Contact 📧
For any queries or issues, feel free to reach out to us:

[![Email](https://img.shields.io/badge/HACKINTER-MAIL-red.svg)](mailto:ceh.ec.counselor147@gmail.com)  
[![Telegram](https://img.shields.io/badge/HACKINTER-T.ME-blue.svg)](https://t.me/chat_with_hackinter_bot)  
[![Twitter](https://img.shields.io/badge/HACKINTER-TWITTER-gray.svg)](https://x.com/_anonix_z)

---

### Project Contributors 👥

- **Kairos Team**  
  Special thanks to contributors who help us make the tool better!

---
> "Tools are only as powerful as their users, let’s discover new possibilities!" - Hackinter

## Disclaimer ⚠️

The tool **Kairos** is designed for educational purposes and legitimate security testing only. **Using this tool for illegal activities, unauthorized access, or malicious intent is strictly prohibited.**

By using this tool, you agree to comply with all local laws and regulations regarding cybersecurity, and you are solely responsible for your actions. The creators of this tool do not take any responsibility for any misuse or damage caused by the tool.


