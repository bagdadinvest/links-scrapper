# Link Scraper README

## Overview

This project is a simple web scraper built using Python and Playwright. It navigates to a specified website, collects all the post links available on the homepage, and saves them into a CSV file. This project is useful for quickly collecting hyperlinks from a website for further analysis or reference.

## Requirements

To run this project, you need to install the following tools and libraries:

### System Requirements
- Python 3.7 or higher
- Internet connection for accessing the target website

### Python Packages
The following Python packages are required:

1. **Playwright**: Used for web automation and interaction.
   - Installation: `pip install playwright`
   - Additional Setup: After installing the package, you need to install the browsers by running:
     ```sh
     playwright install
     ```

2. **CSV**: The built-in Python `csv` module is used to save extracted links.

3. **Time**: The built-in Python `time` module is used for introducing delays to ensure all content is fully loaded.

