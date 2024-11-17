# AEMO Electricity Dashboard Data Extractor

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About

The AEMO Electricity Dashboard Data Extractor is a tool designed to extract and display electricity data from the AEMO visualisation platform. This project leverages Selenium WebDriver to interact with the website, select specific regions and periods, and parse the data into structured formats for further analysis.

## Getting Started

To get a local copy up and running follow these simple steps.

## Prerequisites

- Python 3.x
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) to match your Chrome version

Python packages:
- selenium
- pytest
- setuptools

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/xinjalin/selenium_aemo_spot_price
   cd selenium_aemo_spot_price
   ```

2. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver** and add it to your PATH.

## Usage

Use the script to extract data by running the following command:

```sh
python main.py
```

This will launch a headless browser session, select the South Australia (SA) region and extract electricity data for the "Pre-Dispatch" and "Dispatch" periods, outputting the results to the console.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Email - [xinjalin@gmail.com](mailto:xinjalin@gmail.com)

Project Link: [https://github.com/xinjalin/selenium_aemo_spot_price](https://github.com/xinjalin/selenium_aemo_spot_price)

## Acknowledgments

Special thanks to the Selenium and AEMO teams for their tools and datasets.
