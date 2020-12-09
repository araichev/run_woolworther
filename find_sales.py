import os
import pathlib as pl

import countdowner as cd
import dotenv as de


# Load secrets
ROOT = pl.Path(os.path.abspath(__file__))
de.load_dotenv(ROOT / ".env")

U = os.getenv("GMAIL_USERNAME")
P = os.getenv("GMAIL_PASSWORD")

# Run pipeline
config = [
    ["ibatatas@runbox.com", "https://docs.google.com/spreadsheets/d/1Cu8wEckdfGPtkN9zj5H8O_4ZUrQyrXBZ8Um-K2BSlnc/edit?usp=sharing"],
    ["helena.teichrib@gmail.com", "https://docs.google.com/spreadsheets/d/1v2ZmJrSwSok0dTeVV6KBksAVa_eTTFE2YDQheXAYZT4/edit?usp=sharing"],
    ["jenklosser@gmail.com", "https://docs.google.com/spreadsheets/d/1IXh32XgrUq1O_xWq5SqXZlhwGmoK2tChwFqP2AEXJUo/edit?usp=sharing"],
    ["dobozban@gmail.com", "https://docs.google.com/spreadsheets/d/1KBYj80WRxFSojyO6lKLswxrshNIJea_aro3lIjnVnqU/edit?usp=sharing"],
]
for email, url in config:
    print(f"Working on watchlist for {email}...")
    cd.run_pipeline(
        url,
        recipients=[email],
        gmail_username=U,
        gmail_password=P,
        sales_only=True,
    )
