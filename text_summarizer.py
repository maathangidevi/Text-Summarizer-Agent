from textblob import TextBlob

# Ask user for input
text = input("Enter the text: ")

# Create TextBlob object
blob = TextBlob(text)

# Simple summary (first sentence)
summary = blob.sentences[0]

print("\nSummary:")
print(summary)