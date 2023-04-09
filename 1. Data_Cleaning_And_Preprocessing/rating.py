"""
Suppose you have a dataset of customer reviews for a product, and the reviews include both text and numerical ratings. 
However, some of the reviews have been entered with mistakes or inconsistencies in the way the ratings are expressed.

For example, the following are all possible ways the rating "4.5 stars" might have been entered:
    1. 4.5
    2. 4.5/5
    3. 4.5 out of 5
    4. 4.5 stars
    5. 4.5 out of 5 stars
    6. 90%
    7. 9/10
To clean up the data and ensure that all ratings are consistently expressed, you could use regex to extract the numerical ratings from the text, regardless of the format in which they were entered
"""

import re

reviews = ["Great product, 4.5 stars!",
           "I'd give it a 9/10 rating",
           "Not bad, 90% satisfaction rating",
           "4.5 out of 5 stars - highly recommend!",
           "Terrible quality, 1 star only",
           "Amazing value for the price, 4.8/5 rating"]

for review in reviews:
    # Extract numerical rating from text using regex
    rating_match = re.search(r"(\d+(\.\d+)?)\s*(?:/|out of|stars)?\s*(?:10|\d+%|\d+(?:\.\d+)?\s*(?:/|out of|stars)?\s*5)?", review)
    if rating_match:
        rating = float(rating_match.group(1))
        print(f"Extracted rating: {rating}")
    else:
        rating = None
        print("No rating found")

    # Extract sentiment from text using regex
    sentiment_match = re.search(r"(good|great|excellent|bad|terrible|poor|average|mediocre)", review, re.IGNORECASE)
    if sentiment_match:
        sentiment = sentiment_match.group(1)
        print(f"Extracted sentiment: {sentiment}")
    else:
        sentiment = None
        print("No sentiment found")

    # Do something with the extracted data...
    if rating and sentiment:
        if rating >= 4.0 and sentiment in ["good", "great", "excellent"]:
            print("Highly positive review!\n")
        elif rating < 3.0 and sentiment in ["bad", "terrible", "poor"]:
            print("Highly negative review.\n")
        else:
            print("Neutral or mixed review.\n")
    else:
        print("Insufficient data to classify review.\n")
