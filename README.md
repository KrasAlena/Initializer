# Project Initializer

This project is designed to create a new project structure with predefined folders and files.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/project_initializer.git
    cd project_initializer
    ```

2. Create and activate a virtual environment (recommended):
    ```sh
    python -m venv venv
    ```

    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install the package:
    ```sh
    pip install .
    ```

## Usage

1. Navigate to the directory where you want to create a new project:
    ```sh
    mkdir my_new_project
    cd my_new_project
    ```

2. Run the command to initialize the project structure:
    ```sh
    initialize_project
    ```

After executing these steps, the `my_new_project` directory will have the following structure:
```plaintext
my_new_project/
├── run.py
└── project_profile/
    ├── __init__.py
    ├── models.py
    ├── routes.py
    ├── templates/
    │   └── base.html
    └── static/
        ├── css/
        │   └── styles.css
        └── images/


By following these instructions, any user can easily install and use your package to initialize a project structure.