import requests

# Step 1: Fetch the list of users
users_response = requests.get("https://jsonplaceholder.typicode.com/users")
users = users_response.json()


# Step 2: Find the user with username "Bret"
user_bret = next(user for user in users if user["username"] == "Bret")
# print(user_bret)

# Step 3: Fetch all posts made by the user
user_posts_response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_bret['id']}")
user_posts = user_posts_response.json()
# print(user_posts)

# Step 4: Count the number of posts made by the user
num_posts = len(user_posts)
# print(num_posts)

# Step 5: Print the titles of each post
print(f"Number of posts made by user 'Bret': {num_posts}")

for post in user_posts:
    print(post["title"])

if num_posts > 5:
    print("This user is quite active!")
