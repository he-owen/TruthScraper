# TruthScraper

A Python project that uses [Truthbrush](https://github.com/stanfordio/truthbrush.git) to scrape Donald J. Trump posts from Truth Social and runs sentiment analysis using FinBERT to determine potential market impact.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/he-owen/TruthScraper.git
cd TruthScraper
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root with your Truth Social credentials:

```bash
TRUTHSOCIAL_USERNAME=your_username
TRUTHSOCIAL_PASSWORD=your_password
```

## Usage


Run the scraper and analyze sentiment:

```bash
python main.py <TRUTH_SOCIAL_URL> --max-posts 5
```

Example:

```bash
python main.py https://truthsocial.com/@realDonaldTrump --max-posts 2
```

Output

```
Found 2 new post(s):

[2025-11-07T00:02:10.748Z] (ID: 115505478418176575) | Sentiment: Bullish
I just held a great call between Prime Minister Benjamin Netanyahu...
--------------------------------------------------------------------------------
[2025-11-06T21:53:38.990Z] (ID: 115504973020459337) | Sentiment: Bullish
Joe Lombardo is the strong and very popular Governor of Nevada...
--------------------------------------------------------------------------------
```
