# Web Crawling

<img width="1440" alt="Screenshot 2024-07-22 at 11 58 16 PM" src="https://github.com/user-attachments/assets/866e699c-b6ea-49a4-9839-4769ef906a89">

## Overview

Web Crawl is a web application that allows you to scrape web pages and use Retrieval-Augmented Generation (RAG) to answer questions based on the scraped content. The application is built with Streamlit and utilizes OpenAI's language models for text generation.

## Features

- Scrape web pages in parallel
- Store scraped content in a knowledge base
- Perform similarity search on the stored content
- Use OpenAI's language models to answer questions based on the scraped content
- Configuration options for chunk size, overlap, and crawling depth
- View and manage scraped JSON data and FAISS vector stores

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mhadeli/web-crawler.git
    cd deep-crawl
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

1. Set up the configuration by editing the `settings.json` file or using the settings page in the Streamlit app.
2. Run the Streamlit app:

    ```bash
    streamlit run chat.py
    ```

3. Enter your OpenAI API key in the sidebar.
4. Enter the URLs to scrape in the sidebar and click "Scrape and Add to Knowledge Base".
5. Ask questions based on the scraped content using the chat interface.

## Configuration

The configuration options can be set in `settings.json` or through the Streamlit settings page:

- `model`: The OpenAI model to use (e.g., "gpt-3.5-turbo", "gpt-4o")
- `top_k`: The number of similar documents to retrieve
- `chunk_size`: The size of text chunks for processing
- `chunk_overlap`: The overlap between text chunks
- `min_content_length`: The minimum length of HTML content to consider
- `max_depth`: The maximum crawling depth

## Project Structure

- `chat.py`: Main Streamlit app script
- `crawler.py`: Script for scraping web pages
- `settings.py`: Script for configuring the settings
- `knowledge_base.py`: Script for managing the knowledge base
- `settings.json`: JSON file for storing configuration settings

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
