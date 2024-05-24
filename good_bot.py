import praw

# Authenticate with Reddit API
reddit = praw.Reddit(client_id='p5Zg70RMU4Dozjv-E4_T8g',
                     client_secret='maMmRnuBnYl0uOiG_Bxz9L6O9RKKZw',
                     user_agent='Replies good bot to u/pixel_counter_bot (by u/Professional-Rope840)',
                     username='good_bot_pix_counter',
                     password='6B7qvuf:kjy7qWW')

# Define the subreddit where you want to search for the user's posts
subreddit_name = 'countablepixels'

# Define the username you want to search for
target_username = 'pixel-counter-bot'

# Load replied comment IDs from a file or initialize an empty set
replied_comments = set()

# Read replied comment IDs from a file if it exists
try:
    with open('replied_comments.txt', 'r') as file:
        replied_comments = set(file.read().splitlines())
except FileNotFoundError:
    pass

# Search for posts by the target user in the specified subreddit
for submission in reddit.subreddit(subreddit_name).new(limit=None):
    submission.comments.replace_more(limit=None)  # Retrieve all comments for the submission
    for comment in submission.comments.list():
        if comment.author and comment.author.name.lower() == target_username.lower():
            if comment.id not in replied_comments:  # Check if comment has not been replied to
                # Reply to the user's comment
                comment.reply("Good bot")

                # Print confirmation message
                print("Replied to user", target_username)

                # Add the comment ID to the set of replied comments
                replied_comments.add(comment.id)

                # Write replied comment IDs to file
                with open('replied_comments.txt', 'a') as file:
                    file.write(comment.id + '\n')

            # Break out of the loop after replying to the first comment found
            break
    else:
        continue  # Continue to the next submission if no comments are found from the target user
    break  # Exit the outer loop after replying to the first comment found
else:
    print("No posts found from user", target_username)
