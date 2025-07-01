import requests

def get_total_items(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        total = response.headers.get('X-WP-Total')
        return int(total) if total is not None else None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

domain = input("Enter the domain (without http:// or https://): ")
base_url = f"https://{domain}/wp-json/wp/v2"

# Get totals
total_posts = get_total_items(f"{base_url}/posts")
total_categories = get_total_items(f"{base_url}/categories")
total_tags = get_total_items(f"{base_url}/tags")

# Display results
print("\n--- WordPress Content Totals ---")
if total_posts is not None:
    print(f"Total Posts: {total_posts}")
else:
    print("Could not retrieve total posts.")

if total_categories is not None:
    print(f"Total Categories: {total_categories}")
else:
    print("Could not retrieve total categories.")

if total_tags is not None:
    print(f"Total Tags: {total_tags}")
else:
    print("Could not retrieve total tags.")
