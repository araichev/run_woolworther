import os

import countdowner as cd
import dotenv as de


# Load secrets
de.load_dotenv()

U = os.getenv("GMAIL_USERNAME")
P = os.getenv("GMAIL_PASSWORD")

if not U or not P:
    raise ValueError("Could not find GMail credentials")

# Run pipeline
config = [
    ["ibatatas@runbox.com", "https://docs.google.com/spreadsheets/d/1Cu8wEckdfGPtkN9zj5H8O_4ZUrQyrXBZ8Um-K2BSlnc/edit?usp=sharing"],
    ["jenklosser@gmail.com", "https://docs.google.com/spreadsheets/d/1IXh32XgrUq1O_xWq5SqXZlhwGmoK2tChwFqP2AEXJUo/edit?usp=sharing"],
    ["helena.teichrib@gmail.com", "https://docs.google.com/spreadsheets/d/1v2ZmJrSwSok0dTeVV6KBksAVa_eTTFE2YDQheXAYZT4/edit?usp=sharing"],
    ["dobozban@gmail.com", "https://docs.google.com/spreadsheets/d/1KBYj80WRxFSojyO6lKLswxrshNIJea_aro3lIjnVnqU/edit?usp=sharing"],
    ["jesse.p.prendergast@gmail.com", "https://docs.google.com/spreadsheets/d/10X11TILgnFvOyEs6K1rntTOvE2w3WmsxLKWsk5ALTjM/edit?usp=sharing"],
    ["cstewart000@gmail.com", "https://docs.google.com/spreadsheets/d/16oAl4UZNHN9wSOK_n0y_yBv7FVZ5y3IlkF9gygwoH7E/edit?usp=sharing"],
]
for email, url in config:
    print(f"Working on watchlist for {email}...")
    f = cd.run_pipeline(
        url,
        recipients=[email],
        gmail_username=U,
        gmail_password=P,
        sales_only=True,
    )

