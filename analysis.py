# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 🔧 Optional: Seaborn style
sns.set(style="whitegrid")
 
 # Load Dataset
df = pd.read_csv("comments.csv")

# Clean Column Names
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Convert to datetime using correct format
df['created_timestamp'] = pd.to_datetime(df['created_timestamp'], dayfirst=True, errors='coerce')


# Add Extra Columns
df['date'] = df['created_timestamp'].dt.date
df['weekday'] = df['created_timestamp'].dt.day_name()

# Emoji Usage
plt.figure(figsize=(6, 4))
sns.countplot(x='emoji_used', data=df, palette='Set2')
plt.title('Emoji Usage in Comments')
plt.xlabel('Emoji Used?')
plt.ylabel('Number of Comments')
plt.tight_layout()
plt.savefig("emoji_usage.png")
plt.show()

# Hashtag Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['hashtags_used_count'], bins=10, kde=True, color='skyblue')
plt.title('Hashtags Used per Comment')
plt.xlabel('Number of Hashtags')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("hashtags_distribution.png")
plt.show()

# Most Active Users
plt.figure(figsize=(8, 4))
top_users = df['user__id'].value_counts().head(10)
top_users.plot(kind='barh', color='orange')
plt.title('Top 10 Most Active Commenters')
plt.xlabel('Number of Comments')
plt.ylabel('User ID')
plt.tight_layout()
plt.savefig("top_users.png")
plt.show()

# Daily Comments Trend
daily_comments = df.groupby('date').size()

daily_comments.plot(title='Daily Comments Count', figsize=(10,4), color='green')
plt.ylabel('Number of Comments')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("daily_comments.png")
plt.show()

# Most Commented Photos
plt.figure(figsize=(8, 4))
top_photos = df['photo_id'].value_counts().head(10)
top_photos.plot(kind='bar', title='Top 10 Most Commented Photos', color='purple')
plt.ylabel('Comments')
plt.xlabel('Photo ID')
plt.tight_layout()
plt.savefig("top_photos.png")
plt.show()

# Word Cloud from Comments
text = " ".join(str(comment) for comment in df['comment'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Comments")
plt.tight_layout()
plt.savefig("wordcloud.png")
plt.show()

# Weekday Comment Activity
plt.figure(figsize=(8, 4))
sns.countplot(x='weekday', data=df, order=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    palette='pastel')
plt.title('Comments by Weekday')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Comments')
plt.tight_layout()
plt.savefig("weekday_comments.png")
plt.show()

#  Save Cleaned Data
df.to_csv("processed_comments.csv", index=False)

print("✅ All analysis complete! Charts saved in your folder.")
