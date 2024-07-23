# PDF Chatbot

## Overview

This project is a FastAPI application that allows querying a PDF document using a chatbot interface. The application uses LangChain for natural language processing, OpenAI for embeddings and QA chain, and FastAPI for building the web API. 

## Setup

### Prerequisites

- Python 3.8 or later
- `pip` for package management

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Sushant113/pdf-chatbot.git
    cd pdf-chatbot
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables:**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Add Your PDF File:**

    Place your PDF file in the appropriate directory and update the path in `main.py`.

6. **Run the FastAPI Application:**

    ```bash
    uvicorn main:app --reload
    ```

7. **Test the Application:**

    - **Health Check Endpoint:**
      - URL: `http://127.0.0.1:8000/health`
      - Method: `GET`

    - **Query Endpoint:**
      - URL: `http://127.0.0.1:8000/query`
      - Method: `POST`
      - Body (JSON): `{"query": "Your query here"}`

    You can use tools like `curl`, Postman, or a Python script to test the endpoints.

## Testing

To run the unit tests:

```bash
pytest
