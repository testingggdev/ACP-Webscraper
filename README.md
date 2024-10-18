<h1>Web Scraper for Extracting Email & Contact Information</h1>
This project is a Python-based web scraper designed to extract contact information, specifically company names, emails, and phone numbers, from websites. It can crawl a given website and its internal links up to a specified depth, saving the extracted data in CSV and HTML formats.

<h2>Features</h2>
<ul>
<li>Extracts company names  or URL structure. </li>
<li>Extracts emails and phone numbers using regex. </li>
<li>Crawls internal links to extract data from multiple pages.</li>
<li>Saves extracted data in CSV and HTML formats.</li>
</ul>

<h2>Requirements</h2>
Before running the script, make sure you have the following dependencies installed:
<ul>
<li>Python 3.9+</li>
<li>Requests</li>
<li>BeautifulSoup (from the bs4 package)</li>
<li>Pandas</li>
</ul>
You can install the required packages with the following steps:
<ol>
<b><li>Go to the <a href="https://www.python.org/downloads/">Python Downloads page</a></li></b>
<ul>
<li>Download Python 3.13.0</li></ul><br/>

<li><b>Install Python</b></li>
<ul>
<li>Run the downloaded installer</li>
<li><b>Important</b>: During installation, check the box that says <b>"Add Python.exe to PATH"</b></li>
<li>Click <b>"Install Now"</b> and follow the prompts to complete the installation</li></ul>
<l




Setup
Clone the repository or download the script:

bash
Copy code
git clone https://github.com/your-repo/webscraper.git
Set up the environment:

It is recommended to create a virtual environment to manage dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

Run the following command to install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Set the target URL:

Open the main.py file and update the TARGET_URL variable with the URL of the website you want to scrape.

python
Copy code
TARGET_URL = 'https://www.example.com'
Set the Crawlbase API token:

Update the CRAWLBASE_JS_TOKEN variable with your Crawlbase API token.

python
Copy code
CRAWLBASE_JS_TOKEN = 'your_api_token_here'
Usage
Running the scraper:

To run the web scraper, simply execute the script as follows:

bash
Copy code
python main.py
How it works:

The script will start by fetching the HTML content of the TARGET_URL.
It will extract the company name, emails, and contact numbers from the page using regex patterns.
It will crawl internal links up to a specified depth (default is 3).
The script will store extracted data in a CSV file and also create an HTML table with the extracted information.
Output:

The extracted data is saved as contact_info.csv.
The HTML table version of the data is saved as contact_info.html.
Both files will be available in the same directory as the script.
Functions Overview
get_html(api_url): Fetches the HTML content of the page using a GET request.
parse_html(html_content, url): Parses the HTML to extract company name, emails, and phone numbers.
save_to_csv(data, filename='contact_info.csv'): Saves the extracted data to a CSV file.
crawl_website(url, depth=0, max_depth=3): Recursively crawls internal links of a website up to a specified depth.
is_internal_link(url): Determines whether a URL is internal to the website.
Example Output
sql
Copy code
Final extracted data:
 Name       Email            Contact Number
--------------------------------------------
 ExampleCo  info@example.com  +65 1234 5678
 Home       support@example.com None
Customization
Modify the crawling depth: You can adjust the maximum depth for internal link crawling by modifying the max_depth parameter in the crawl_website function.

Regex patterns: You can modify the regular expressions used to extract emails and phone numbers if the website uses different formats.