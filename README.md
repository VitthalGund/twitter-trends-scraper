# 🚀 Twitter Trends Scraper

Welcome to the Twitter Trends Scraper project! This project helps you scrape the top 5 trending topics on Twitter using Selenium, ProxyMesh, and FastAPI, and display the results on a web page.

## 📋 Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Problem Solved](#problem-solved)
4. [Getting Started](#getting-started)
5. [Folder Structure](#folder-structure)
6. [Configuration](#configuration)
7. [Usage](#usage)
8. [Example Output](#example-output)
9. [Contributing](#contributing)
10. [License](#license)

## 📖 About

We are a startup focused on building marketing-tech products. This project is part of an internship assignment to demonstrate skills in web automation, data extraction, and web development.

## ✨ Features

- 🐍 **Selenium Automation**: Automates the process of logging into Twitter and scraping trending topics.
- 🌐 **ProxyMesh Integration**: Uses rotating IP addresses for each request to avoid being blocked.
- 🗄️ **MongoDB Storage**: Stores the scraped data in a MongoDB database.
- ⚡ **FastAPI Backend**: Provides a fast and modern backend for running the scraping script and serving the results.
- 💻 **Interactive Web Interface**: Displays the trending topics in a user-friendly web interface.
- ⏳ **Loading Spinner and Error Handling**: Improved user experience with a loading spinner and error messages.

## 🛠️ Problem Solved

This project solves the problem of manually checking Twitter for trending topics. By automating the process, it saves time and ensures you always have the latest trends available with minimal effort.

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine:

### Prerequisites

- Python 3.7 or higher
- MongoDB
- Twitter account

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/twitter-trends-scraper.git
   cd twitter-trends-scraper
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   Create a `.env` file in the root directory with the following content:

   ```env
   MONGO_URI=mongodb://localhost:27017
   TWITTER_USERNAME=your_twitter_username
   TWITTER_PASSWORD=your_twitter_password
   PROXYMESH_URL=http://your_proxymesh_url
   ```

6. **Run the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

7. **Open your browser and go to**:
   ```bash
   http://127.0.0.1:8000
   ```

## 📂 Folder Structure

```plaintext
twitter-trends-scraper/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── selenium_script.py
├── templates/
│   ├── index.html
│   ├── results.html
├── static/
│   ├── css/
│   ├── js/
├── logs/
├── .env
├── config.py
├── requirements.txt
├── README.md
└── venv/
```

## ⚙️ Configuration

Ensure your `.env` file is correctly configured with the required environment variables:

```env
MONGO_URI=mongodb://localhost:27017
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password
PROXYMESH_URL=http://your_proxymesh_url
```

## 🎮 Usage

### Running the Scraper

1. **Start the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Open your browser and navigate to** `http://127.0.0.1:8000`.

3. **Click the "Click here to run the script" button** to start scraping the top 5 trending topics on Twitter.

4. **View the results** on the web page. The page will display the trending topics, the IP address used, and a JSON extract of the record.

### Example Output

```json
[
 {
   "_id": { "$oid": "60b8d2958e6200f55fd1bc4e" },
   "trend1": "#ExampleTrend1",
   "trend2": "#ExampleTrend2",
   "trend3": "#ExampleTrend3",
   "trend4": "#ExampleTrend4",
   "trend5": "#ExampleTrend5",
   "datetime": "2021-06-03T12:00:00Z",
   "ip_address": "123.456.789.000"
 }
]
```

## 🤝 Contributing

We welcome contributions! Here’s how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

