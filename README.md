# Title Insurance Document Parser

This project provides a simple Flask web application that allows users to upload legal documents related to title insurance. The application extracts key sections such as **Exceptions**, **Requirements**, and the **Mortgage Schedule**.

## Installation

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

## Running

```bash
python app.py
```

Then open your browser at <http://localhost:5000> to upload a document.

The parser supports PDF or plain text files. PDF support requires the `PyPDF2` package.

## Command Line Usage

You can also parse a file directly using the parser module:

```bash
python parser.py path/to/document.pdf
```

## Full Stack Application

A basic full stack example using Node.js, MongoDB and React is included in the `backend` and `frontend` folders.

### Backend

Install dependencies and start the API server:

```bash
cd backend
npm install
npm start
```

The server exposes REST endpoints under `/api` and uses JWT authentication. Set `MONGODB_URI` and `JWT_SECRET` environment variables as needed.

### Frontend

The frontend is a small React app served as static files. Open `frontend/index.html` in a browser after starting the backend to interact with the API.
