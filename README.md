# Python-CLI-Todo-App
A CLI task manager to add, view, complete, and delete tasks. Features persistent storage and text file report generation.

# Python CLI Task Manager

[![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust and user-friendly command-line application designed for efficient task management directly from your terminal. Built with standard Python libraries, this tool allows you to add, view, complete, and delete tasks seamlessly. All data is persistently stored in a local `tasks.json` file, ensuring your to-do list is always saved between sessions.

## Table of Contents

- [Key Features](#-key-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation and Usage](#-installation-and-usage)
- [File Structure](#-file-structure)
- [How It Works](#-how-it-works)
- [Future Improvements](#-future-improvements)
- [License](#-license)

##  Key Features

-   **Add, View, and Delete Tasks:** Full CRUD (Create, Read, Delete) functionality for your tasks.
-   **Mark as Complete:** Easily toggle the status of any task to keep track of your progress.
-   **Persistent Storage:** Utilizes a `tasks.json` file to automatically save all changes, so your data is safe even after closing the terminal.
-   **Report Generation:** Instantly create a `task_report.txt` file for a clean, shareable summary of your task list.
-   **Zero Dependencies:** Runs with a standard Python 3 installation, no external packages needed.

##  Demo

Here is a sample workflow of the application in action:

```
$ python To_Do_list.py
Tasks loaded successfully.

Task Manager
1. Show Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Save Task Report to File
6. Exit
Choose an option: 2
Enter task title: Design the new database schema
Task 'Design the new database schema' added.
Tasks saved.

Task Manager
...
Choose an option: 2
Enter task title: Write the API documentation
Task 'Write the API documentation' added.
Tasks saved.

Task Manager
...
Choose an option: 1

Your Tasks:
1. [✗] Design the new database schema
2. [✗] Write the API documentation

Task Manager
...
Choose an option: 3
Enter task number to mark as completed: 1
Task 'Design the new database schema' marked as completed.
Tasks saved.

Task Manager
...
Choose an option: 1

Your Tasks:
1. [✓] Design the new database schema
2. [✗] Write the API documentation

Task Manager
...
Choose an option: 6
Goodbye!
```

##  Tech Stack

-   **Backend:** Python
-   **Data Storage:** JSON (using the built-in `json` module)

##  Installation and Usage

To get this project up and running on your local machine, please follow these steps.

### Prerequisites

-   Python 3.7 or newer
-   Git

### Instructions

1.  **Clone the Repository**
    Open your terminal and clone the repository using the following command:
    ```bash
    git clone https://github.com/nayanj2221/Python-CLI-Todo-App
    ```

2.  **Navigate to the Directory**
    ```bash
    cd To_Do_list.py 
    ```

3.  **Run the Application**
    Execute the main script to start the task manager:
    ```bash
    python To_Do_list.py
    ```
    The application will launch, and you can interact with it through the menu options.

##  File Structure

The project repository is organized as follows:

```
├── .gitignore          # Tells Git which files to ignore
├── LICENSE             # Project's MIT License file
├── README.md           # This documentation file
├── To_Do_list.py       # The main application source code
│
├── tasks.json          # (Generated) Database file for storing tasks
└── task_report.txt     # (Generated) Text file containing the task summary
```

##  How It Works

The application's logic is centered around a list of dictionaries, where each dictionary represents a single task.

1.  **Initialization:** Upon starting, the `load_tasks()` function attempts to read and parse the `tasks.json` file into the main tasks list. If the file doesn't exist or is empty, it starts with an empty list.
2.  **User Actions:** The `main()` function runs an infinite loop, presenting the user with a menu. Based on user input, it calls the appropriate function (e.g., `add_task()`, `delete_task()`).
3.  **Data Persistence:** After any action that modifies the task list (add, complete, delete), the `save_tasks()` function is immediately called. This function overwrites the `tasks.json` file with the updated list, ensuring that no data is lost.

##  Future Improvements

This project has a solid foundation, but there is always room to grow. Here are some potential features to add in the future:

-   **Edit Tasks:** Implement functionality to edit the title of an existing task.
-   **Task Priorities:** Add a priority level (e.g., High, Medium, Low) to each task.
-   **Due Dates:** Allow users to add due dates to tasks.
-   **Enhanced UI:** Improve the terminal output with colors for different statuses using a library like `colorama` or `rich`.

##  License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
