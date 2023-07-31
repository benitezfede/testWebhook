# Code Interpreter API Project

This is a Python project that uses the `codeinterpreterapi` to interact with OpenAI's GPT-4 to execute commands and print the results. The application loops, allowing the user to continuously ask questions until they decide to exit.

## Setup

Here are the steps to setup and run the project:

1. Clone the project repository:

   ```bash
    git clone 
   
    # Clone the repository
    cd <directory-name>
   
    # Create a virtual environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    # Install the dependencies
    pip install -r requirements.txt
   
   # Create a .env file
    touch .env
   
   # Add the following to the .env file
    OPENAI_API_KEY=<your-openai-api-key>
    FILE_PATH=<path-to-your-file>

    # Run the application
    python main.py   

    ```

