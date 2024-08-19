# MicroCascade Server

MicroCascade Server is designed to be used in conjunction with the "3+ Levels Cascade" app available on the Atlassian Marketplace. This server manages the options for your custom fields and serves them via an API endpoint, making it easy to integrate with Jira custom fields.

## Features

- **Create**: Add new options for custom fields.
- **Read**: Retrieve options, either all at once or filtered by custom field ID.
- **Update**: Modify existing options.
- **Delete**: Remove options from your custom fields.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/MicroCascade-Server.git
    cd MicroCascade-Server
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:

    ```bash
    python main.py
    ```

## Usage

After deploying the server, you can manage your custom field options using the provided API endpoints.

-- check the main.py file for info
