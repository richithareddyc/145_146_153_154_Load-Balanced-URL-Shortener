# Load-Balanced URL Shortener

This project is a simple URL Shortener built using Flask and Docker. It supports:
- Accepting long URLs
- Generating short URLs
- Redirecting to original URLs
- In-memory storage using Python dictionary

## Team Members
- 145 - Brahmani 
- 146 - Vinitha
- 153 - Chandrika
- 154 - Richitha

## Running the App

```bash
docker build -t url-shortener .
docker run -p 5050:5000 url-shortener
