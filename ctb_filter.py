import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer

while True:
    # Assume you have a CSV file
    df = pd.read_csv("manga.csv")

    #df = df.rename(columns={"old_name1": "new_name1", "old_name2": "new_name2"})

    # Sample 5 random items or all items if the DataFrame has fewer than 5 rows
    num_items_to_sample = min(5, len(df))
    random_items = df.sample(num_items_to_sample)

    print("Select one item for recommendations:")
    print(random_items)

    # User chooses an item
    selected_index = int(
        input("Enter the index of the item for recommendations (1-5): ")
    )
    if selected_index < 1 or selected_index > 5:
        print("Invalid index. Exiting.")
        exit()

    selected_item = random_items.iloc[selected_index - 1]
    print("\nSelected Item:")
    print(selected_item)

    # Extract the selected genre
    selected_genre = selected_item["genre"]

    # Store the original 'genre' column
    original_genre_column = df["genre"].copy()

    # Check for NaN values in the 'genre' column and replace with an empty string
    df["genre"] = df["genre"].fillna("")

    # Filter rows with any one of the genres in the selected item
    recommendations = df[
        df["genre"]
        .str.split(", ")
        .apply(lambda x: any(item in x for item in selected_genre.split(", ")))
    ]

    # Restore the original 'genre' column
    df["genre"] = original_genre_column

    # Exclude the selected item from recommendations
    recommendations = recommendations[recommendations["name"] != selected_item["name"]]

    # Sample 5 random rows from the recommendations, including the 'genre' column
    recommendations = recommendations.sample(5)
    print("\nRecommendations:")
    print(recommendations[["name", "genre"]])
