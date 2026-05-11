# BiasExplorationInNovels

This folder contains my exploratory data analysis notebook for the Goodreads Top Ranked Novels dataset and the New York Times Bestseller dataset.

## Notebook

- `BiasExplorationInNovels1.ipynb`

## Project Description

In this notebook, I explore patterns in genre, publication year, Top 500 ranking, and Goodreads ratings. The goal of this assignment is to use exploratory data analysis to better understand the structure of the datasets and identify possible gaps, patterns, or bias.

## Datasets Used

The notebook uses remote dataset links, so the datasets do not need to be downloaded locally.

Top 500 Novels dataset:

https://raw.githubusercontent.com/melaniewalsh/responsible-datasets-in-context/main/datasets/top-500-novels/final_merged_dataset_no_full_text.tsv

New York Times Bestseller dataset:

https://raw.githubusercontent.com/ecds/post45-datasets/main/nyt_full.tsv

## Main Questions Explored

- How are genres distributed in the Top 500 Novels dataset?
- Which genres have higher or lower average rankings?
- How are novels distributed across publication years?
- Is there a strong relationship between Goodreads ratings and Top 500 ranking?

## Tools Used

- Python
- Pandas
- Altair
- Jupyter Notebook

## Notes

The New York Times Bestseller dataset stores titles in all capital letters, so I cleaned the title column before merging it with the Top 500 Novels dataset. I used a left merge so that all novels from the Top 500 Novels dataset would stay in the combined dataset.