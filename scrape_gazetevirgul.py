# Import necessary libraries from Playwright
from playwright.sync_api import sync_playwright
import csv
import time

# Function to scrape the links from the homepage
def scrape_links():
    # Start Playwright
    print("[DEBUG] Starting Playwright...")
    with sync_playwright() as p:
        # Launch the browser (headless mode)
        print("[DEBUG] Launching browser in headless mode...")
        browser = p.chromium.launch(headless=True)

        # Open a new browser page
        print("[DEBUG] Opening a new page...")
        page = browser.new_page()

        # Navigate to the target webpage
        print("[DEBUG] Navigating to https://www.gazetevirgul.com/ ...")
        page.goto("https://www.gazetevirgul.com/")

        # Wait for the network to be idle, allowing JavaScript to load content
        print("[DEBUG] Waiting for network to be idle...")
        page.wait_for_load_state("networkidle")
        time.sleep(3)  # Additional delay to ensure all elements are loaded
        print("[DEBUG] Page load complete, starting to locate links...")

        # Get all the links for the posts on the homepage using a broader CSS selector
        post_links = []
        links = page.locator("a")

        # Loop through all links and extract the href attributes
        element_handles = links.element_handles()
        print(f"[DEBUG] Found {len(element_handles)} potential links.")

        for idx, element in enumerate(element_handles):
            print(f"[DEBUG] Processing element {idx + 1}/{len(element_handles)}...")
            href = element.get_attribute("href")
            if href:
                print(f"[DEBUG] href attribute found: {href}")  # Print every href found
                post_links.append(href)
            else:
                print(f"[DEBUG] No href attribute found for element {idx + 1}")

        # Close the browser
        print("[DEBUG] Closing the browser...")
        browser.close()

        # Return the list of post links
        return post_links

# Function to save links to a CSV file
def save_links_to_csv(links, filename="post_links.csv"):
    print(f"[DEBUG] Saving {len(links)} links to CSV file: {filename}")
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Post Links"])
        for link in links:
            writer.writerow([link])
    print("[DEBUG] CSV file saved successfully.")

# Run the script, print the links, and save them to a CSV file
if __name__ == "__main__":
    print("[DEBUG] Starting link scraping process...")
    links = scrape_links()
    if links:
        print("[DEBUG] Links found:")
        for link in links:
            print(link)
        save_links_to_csv(links)
        print(f"Saved {len(links)} links to 'post_links.csv'")
    else:
        print("No links found. Please check the page structure or adjust the script.")
