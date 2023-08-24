# Wine API Project with Country/State Guessing
Welcome to the Wine API project! This project is built using Python, Peewee, PostgreSQL, and Flask, and it also features a command line application that lets you guess the country/state from which the wines originate. Whether you're a wine enthusiast or just looking to explore different wines, this project has something exciting to offer.

## Table of Contents
### Project Overview
### Installation
### Usage
### API Endpoints
### Command Line Application
### Contributing
### License

#### Project Overview
This project aims to provide a user-friendly interface to explore and learn about various wines while also challenging your knowledge of wine regions. It consists of a RESTful API built with Flask, a PostgreSQL database to store wine information, and a command line application for interactive guessing games.

#### Installation
Clone this repository to your local machine:

```
git clone https://github.com/your-username/wine-api-project.git
cd wine-api-project
```

Create a virtual environment (recommended) and activate it:

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required packages using pip:

```
pip install -r requirements.txt
```

Set up your PostgreSQL database and update the database configuration in config.py:

```
DATABASE = {
    'name': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'localhost',
    'port': '5432',
}
```

Initialize the database and populate it with sample data:

```
python manage.py create_tables
python manage.py seed_data
```

#### Usage
##### API Endpoints
Start the Flask development server:

```
python app.py
```

The API endpoints will be available at http://localhost:5000. Here are the main endpoints:

- GET /wines: Get a list of all wines.
- GET /wines/<wine_id>: Get details about a specific wine.
- POST /wines: Add a new wine (authentication required).
- PUT /wines/<wine_id>: Update information about a specific wine (authentication required).
- DELETE /wines/<wine_id>: Delete a wine (authentication required).
  
#### Command Line Application
Run the command line application to guess the country/state of a random wine:

```
python cli.py play
```

Follow the prompts to make your guesses and see how well you know your wine regions!

#### Contributing
Contributions are welcome! If you'd like to improve the project or add new features, feel free to submit a pull request. Make sure to follow the project's coding style and guidelines.

#### License
This project is licensed under the MIT License.

Enjoy exploring wines and testing your knowledge of wine regions with this Wine API project! If you have any questions or feedback, don't hesitate to get in touch. Cheers! 🍷🌎
