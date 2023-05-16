import requests

# Set your access token and the Facebook API endpoint
access_token = 'EAANUlWOTIzoBACGNBjZCkJzJhXQMjBO4LZCG0wWlzQNyWSIQoXS0jPnapfHmEQ1iF69xqbsQG1O4hlSjC5Qxxk92U933ruFpEwrIrTtiZBAJSWkiqJK4iPcQw49ZAD9C60lbA82Tc0YYgP5qUcQmoFbgc0r7XjykhKbu5PBK1uR6oP5o8eZAPzq9DQaAseDjCwwk4NctWlsZBhX49zGTKy'
api_endpoint = 'https://graph.facebook.com/v16.0/'

# Function to make a GET request to the API
def make_api_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return None
    except ValueError:
        print("Error parsing API response as JSON")
        return None

# Function to fetch public posts from a Facebook page
def get_public_posts(page_id):
    url = f'{api_endpoint}/{page_id}/posts?access_token={access_token}'
    data = make_api_request(url)
    if data:
        for post in data.get('data', []):
            print(post)
    else:
        print("Failed to fetch public posts.")

# Function to fetch comments for a given post
def get_post_comments(post_id):
    url = f'{api_endpoint}/{post_id}/comments?access_token={access_token}'
    data = make_api_request(url)
    if data:
        for comment in data.get('data', []):
            print(comment)
    else:
        print("Failed to fetch post comments.")

# Example usage
if __name__ == '__main__':
    page_id = '464001128063289'  # Replace with the desired Facebook page ID
    get_public_posts(page_id)
    # You can uncomment the following lines to fetch and print comments for each post
    # posts = get_public_posts(page_id)
    # for post in posts:
    #     post_id = post['id']
    #     get_post_comments(post_id)
