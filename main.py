import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from urllib.parse import urljoin, urlparse

#insert Javascript token here in between the quotation
CRAWLBASE_JS_TOKEN = ' '

#track visited URLs to avoid crawling the same page multiple times
visited_urls = set()

def get_html(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            # Check if the response content type is HTML
            if 'text/html' in response.headers.get('Content-Type', ''):
                return response.text
            else:
                print("Response is not HTML. Skipping parsing.")
                return None
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def parse_html(html_content, url):
    soup = BeautifulSoup(html_content, 'html.parser')
    print("Parsing HTML content for URL:", url)

    #extracting Company Name
    company_name = urlparse(url).path.split('/')[-1]  #get the last part of the URL path
    if not company_name or company_name == '':
        company_name = 'Home'  #default to 'Home' if the last part is empty

    #extract Email
    emails = set()  #use a set to store unique emails
    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    for tag in soup.find_all(['p', 'span', 'div', 'a']):
        #search for emails in the text
        email_match = email_pattern.search(tag.get_text())
        if email_match:
            emails.add(email_match.group().strip())
        #check for mailto links
        if tag.has_attr('href') and tag['href'].startswith('mailto:'):
            emails.add(tag['href'].split(':', 1)[1].strip())  

    # Extract Contact Number
    contact_number = None
    phone_pattern = re.compile(r'(\+65|\(65\))?\s?[689]\d{3}\s?\d{4}')
    for tag in soup.find_all(['p', 'span', 'div']):
        if not contact_number:
            phone_match = phone_pattern.search(tag.get_text())
            if phone_match:
                contact_number = phone_match.group().strip()
                break

   
    print(f"Extracted - Name: {company_name}, Emails: {list(emails)}, Contact Number: {contact_number}")

    return company_name, list(emails), contact_number  


def save_to_csv(data, filename='contact_info.csv'):
    #filter out None values and keep valid entries
    valid_names = [name for name in data['Name'] if name]
    valid_emails = [email for email in data['Email'] if
                    email and re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email)]
    valid_numbers = [number for number in data['Contact Number'] if
                     number and re.match(r'(\+65|\(65\))?\s?[689]\d{3}\s?\d{4}', number)]

    #create a DataFrame from the valid data, ensuring all columns are the same length
    max_length = max(len(valid_names), len(valid_emails), len(valid_numbers))

    final_data = {
        'Name': valid_names + [None] * (max_length - len(valid_names)),
        'Email': valid_emails + [None] * (max_length - len(valid_emails)),
        'Contact Number': valid_numbers + [None] * (max_length - len(valid_numbers))
    }

    df = pd.DataFrame(final_data)

    #save the DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def crawl_website(url, depth=0, max_depth=3):
    if depth > max_depth or url in visited_urls:
        return None  #no valid data to return

    visited_urls.add(url)  #add URL to visited list here
    html_content = get_html(url)
    if not html_content:
        return None

    # Store unique values
    extracted_data = {
        'Name': [],
        'Email': [],
        'Contact Number': []
    }

    company_name, emails, contact_number = parse_html(html_content, url)

    # Add extracted data to the lists if available
    if company_name:
        extracted_data['Name'].append(company_name)
    extracted_data['Email'].extend(emails)  # Add all unique emails
    if contact_number:
        extracted_data['Contact Number'].append(contact_number)

    # Find all internal links and visit them
    soup = BeautifulSoup(html_content, 'html.parser')
    for link_tag in soup.find_all('a', href=True):
        link = link_tag['href']
        full_url = urljoin(url, link)

        # Only crawl internal links
        if is_internal_link(full_url, url):
            results = crawl_website(full_url, depth + 1, max_depth)
            if results:
                for key in extracted_data:
                    extracted_data[key].extend(results[key])

    return extracted_data

def is_internal_link(url, base_url):
    parsed_url = urlparse(url)
    base_url_parsed = urlparse(base_url)

    # Normalize the URL by removing the fragment identifier
    normalized_url = parsed_url._replace(fragment='').geturl()

    # Return True only if it's an internal link and hasn't been visited
    return (parsed_url.netloc == base_url_parsed.netloc or parsed_url.netloc == "") and normalized_url not in visited_urls


def main():
    target_url = input("Please enter the target URL to crawl: ")  # Get user input for target URL
    api_url = f'https://api.crawlbase.com/?token={CRAWLBASE_JS_TOKEN}&url={target_url}'

    extracted_data = crawl_website(target_url)

    if extracted_data:
        save_to_csv(extracted_data)

        # Create a final summary DataFrame with only valid entries
        valid_names = [name for name in extracted_data['Name'] if name]

        # Normalize emails to lowercase before filtering for uniqueness
        valid_emails = list(set(email.lower() for email in extracted_data['Email'] if
                                 email and re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email)))  # Ensure unique emails
        valid_numbers = [number for number in extracted_data['Contact Number'] if
                         number and re.match(r'(\+65|\(65\))?\s?[689]\d{3}\s?\d{4}', number)]

        # Determine the length of the final DataFrame based on the maximum list length
        length = max(len(valid_names), len(valid_emails), len(valid_numbers))

        final_summary = pd.DataFrame({
            'Name': valid_names + [None] * (length - len(valid_names)),
            'Email': valid_emails + [None] * (length - len(valid_emails)),
            'Contact Number': valid_numbers + [None] * (length - len(valid_numbers))
        })

        # Filter out rows where both Email and Contact Number are None
        final_summary = final_summary[~(final_summary['Email'].isnull() & final_summary['Contact Number'].isnull())]

        # Print the DataFrame in a table format
        print("\nFinal extracted data:")
        print(final_summary.to_string(index=False))  # Print as table without the index

        # Save the final summary as an HTML table
        html_output = final_summary.to_html(index=False)
        with open('contact_info.html', 'w') as f:
            f.write(html_output)
    else:
        print("No data extracted.")

if __name__ == "__main__":
    main()
