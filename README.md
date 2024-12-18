# FastAPI Web Service

This project is a simple web service built with FastAPI. It allows users to customize a greeting message using query parameters passed through the URL. The default message is: "Hello Recruto! Давай дружить!", but the name and message can be modified via the `name` and `message` query parameters.

---
## Features

- Returns a customized greeting message.
- Supports query parameters:
  - `name`: Custom name for the greeting (default is "Recruto").
  - `message`: Custom message to include (default is "Давай дружить").

Example usage: https://deepra-test-task.onrender.com/?name=Recruto&message=Let's%20be%20friends

---
## Tech Stack

- **FastAPI**: High-performance web framework for building APIs.
- **Uvicorn**: ASGI server used to run the FastAPI application.
- **Docker**: Containerization for easy deployment.
- **Pydantic**: Data validation and parsing.

---
## Project Setup

### Prerequisites

- **Python 3.12** or higher
- **Docker** (for containerization)
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-hello-recruto.git
   cd fastapi-hello-recruto
   
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload

4. Open your browser and navigate to:
    ```bash
   https://deepra-test-task.onrender.com//?name=Recruto&message=Let's%20be%20friends
   
---
Performed by: Vladislav Gavrikov