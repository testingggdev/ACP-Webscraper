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
<li>Crawlbase API token</li>
</ul>
You can install the required packages with the following steps:
<ol>
<b><li>Crawlbase API Token</li></b>
<ul>
<li>Sign up <a href="https://crawlbase.com/signup">here</a></li>
<li>Click this<a href="https://crawlbase.com/docs/crawling-api/#authentication"> link </a> to get your JavaScript token</li>
<li>Copy the token </li>
</ul><br/>
<b><li>Go to the Python Downloads page</li></b>
<ul>
<li>Download <a href="https://www.python.org/downloads/">Python 3.13.0</a></li></ul><br/>

<li><b>Install Python</b></li>
<ul>
<li>Run the downloaded installer</li>
<li><b>Important</b>: During installation, check the box that says <b>"Add Python.exe to PATH"</b></li>
<li>Click <b>"Install Now"</b> and follow the prompts to complete the installation</li></ul>
<br/>
<li><b>Download Git</b></li>
<ul>
<li>Go to the <a href="https://github.com/testingggdev/ACP-Webscraper">ACP-Webscraper</a> on GitHub</li>
<li>Under '< >Code' Button, <b>Download ZIP</b></li>
<li>Unzip file</li>
</ul><br/>

<li><b>Open Command Prompt (copy & paste these commands)</b></li>
<ul>
<li>cd C:\path\to\where\you\saved\the\download</li>
<li>pip install requests beautifulsoup4 pandas</li>
<li>notepad main.py</li>
<li>paste the JavaScript token into
CRAWLBASE_JS_TOKEN = ' '</li>
<li>Save file</li>
</ul></ol>



<h2>To run the web scraper, simply execute the script as follows:</h2>

In the command prompt: python main.py


<h2>How it works:</h2>
Update TARGET_URL = 'https://www.example.com' with your website <br/>

The script will start by fetching the HTML content of the TARGET_URL.
It will extract the <b>company name, emails, and contact numbers</b> from the page using regex patterns.
It will crawl internal links up to a specified depth (default is 3).
The script will store extracted data in a CSV file and also create an HTML table with the extracted information.

<h2>Output:</h2>
The extracted data is saved as <b>contact_info.csv</b>.
The HTML table version of the data is saved as <b>contact_info.html</b>.
Both files will be available in the same directory as the script.

<h2>Functions Overview:</h2>
<b>get_html(api_url):</b> Fetches the HTML content of the page using a GET request.<br/>
<b>parse_html(html_content, url):</b> Parses the HTML to extract company name, emails, and phone numbers.<br/>
<b>save_to_csv(data, filename='contact_info.csv'):</b> Saves the extracted data to a CSV file.<br/>
<b>crawl_website(url, depth=0, max_depth=3):</b> Recursively crawls internal links of a website up to a specified depth.<br/>
<b>is_internal_link(url):</b> Determines whether a URL is internal to the website.
<h2>Example Output</h2>

Final extracted data:
<table border="1">
  <thead>
    <tr style="text-align: right;">
      <th>Name</th>
      <th>Email</th>
      <th>Contact Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Home</td>
      <td>jcscholarship@csit.gov.sg</td>
      <td>None</td>
    </tr>
    <tr>
      <td>about-us</td>
      <td>cctp@csit.gov.sg</td>
      <td>None</td>
    </tr>
    <tr>
      <td>cybersecurity</td>
      <td>hr@csit.gov.sg</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
