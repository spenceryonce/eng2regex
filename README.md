# eng2regex

`eng2regex` is an innovative web application designed to translate English instructions into JavaScript regular expressions (regex). Utilizing the power of AI through the `g4f` library, it simplifies the creation of regex patterns by allowing users to describe what they want in plain English, along with example texts and expected results. This tool bridges the gap between complex regex syntax and user-friendly English, making regex generation accessible to everyone.

## How It Works

The application consists of a FastAPI backend and a simple, interactive frontend. Users enter three pieces of information in a web form:

1. **English Instructions**: Describe what the regex should do in English.
2. **Example Text**: Provide an example text that the regex will operate on.
3. **Example Expected Result**: Show an example of the expected result after applying the regex.

Upon submitting the form, the backend uses the `g4f` library to process these inputs and generate a JavaScript regex pattern. This pattern is then displayed on the webpage, formatted nicely with markdown and syntax highlighting for clarity and readability.

### Frontend

The frontend is built with HTML, CSS, and JavaScript. It provides a user-friendly interface for inputting the English instructions, example text, and expected result. The response from the server is displayed with markdown formatting and code highlighting, enhancing the user experience.

### Backend

The backend is developed using FastAPI. It receives the user inputs from the frontend, processes them using the `g4f_integration.py` module to interact with the `g4f` library, and returns the generated regex pattern. The FastAPI server is designed to be lightweight, fast, and easy to extend.

## Future Features

- **Support for more languages**: Extend functionality to generate regex for programming languages other than JavaScript.
- **Interactive regex tester**: Implement a feature allowing users to test the generated regex within the application.
- **Advanced customization options**: Provide advanced options for users to customize the regex generation process, such as specifying regex flags.
- **User authentication**: Add user authentication to save and manage generated regex patterns over time.

## Getting Started

To launch the `eng2regex` application locally, follow these steps:

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/eng2regex.git
    cd eng2regex
    ```

2. **Install dependencies**

    Ensure you have Python installed on your machine and then install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

3. **Start the FastAPI server**

    Use the following command to start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

    The `--reload` option makes the server restart upon code changes, which is useful during development.

4. **Access the Web Interface**

    Open a web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the `eng2regex` application.

## Contribution

Contributions to `eng2regex` are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

--- 
