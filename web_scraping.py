import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape blog data from a given URL
def scrape_blog_data(url):
    # Send an HTTP request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Lists to store extracted data
        titles = []
        dates = []
        image_urls = []
        likes_counts = []

        # Extract data from each blog post
        for post in soup.find_all('div', class_='blog-post'):
            # Extract blog title
            title = post.find('h2', class_='blog-title').text.strip()
            titles.append(title)

            # Extract blog date
            date = post.find('span', class_='blog-date').text.strip()
            dates.append(date)

            # Extract blog image URL
            image_url = post.find('img')['src']
            image_urls.append(image_url)

            # Extract blog likes count
            likes_count = post.find('span', class_='likes-count').text.strip()
            likes_counts.append(likes_count)

        # Create a DataFrame to store the data
        data = pd.DataFrame({
            'Blog Title': titles,
            'Blog Date': dates,
            'Blog Image URL': image_urls,
            'Blog Likes Count': likes_counts
        })

        # Save the data to CSV
        data.to_csv('blog_data.csv', index=False)

        print("Data extraction and storage completed successfully.")

    else:
        print(f"Failed to fetch the web page. Status code: {response.status_code}")

# URL for the target webpage
target_url = "https://rategain.com/blog"

# Call the function to scrape data
scrape_blog_data(target_url)
