This project is a Python Flask application that provides an API for managing a collection of songs. It allows users to perform various operations such as retrieving all songs, getting a song by its ID, creating a new song, updating an existing song, and deleting a song.

Installation Instructions:

To run this project locally, follow these steps:

Ensure you have Python installed on your system. You can download and install Python from the official website: https://www.python.org/

Clone or download the project code from the GitHub repository to your local machine.

Open a terminal or command prompt and navigate to the project directory.

Create a virtual environment (optional but recommended) by running the following command:

python -m venv env
Activate the virtual environment:
Copy code
env\Scripts\activate
python app.py
The application will start running on http://localhost:5000. You can access the API endpoints using a tool like Postman or by making HTTP requests from your code.

Usage Examples:

# Retrieve all songs:
GET /songs
Response:
{
  "songs": [
    {
      "Title": "Rise Up",
      "Artist": "Andra Day",
      "Genre": "Pop",
      "ID": 123123,
      "Release": 2016
    }
    {}...
  ]
}

# Get a song by its ID:
GET /songs/<ID>
Example: /songs/123123

Response:
{
  "Title": "Rise Up",
  "Artist": "Andra Day",
  "Genre": "Pop",
  "ID": 123123,
  "Release": 2016
}
  
# Create a new song:
POST /songs
Request Body:
{
  "Title": "New Song",
  "Artist": "New Artist",
  "Genre": "Pop",
  "ID": 123128,
  "Release": 2023
}
Response:
{
  "message": "Song created successfully.",
  "song": {
    "Title": "New Song",
    "Artist": "New Artist",
    "Genre": "Pop",
    "ID": 123128,
    "Release": 2023
  }
}

# Update an existing song:
PUT /songs/<ID>
Example: /songs/123123

Request Body:
{
  "Title": "Updated Song",
  "Artist": "Updated Artist",
  "Genre": "Pop",
  "ID": 123123,
  "Release": 2022
}
Response:
{
  "Title": "Updated Song",
  "Artist": "Updated Artist",
  "Genre": "Pop",
  "ID": 123123,
  "Release": 2022
}
# Delete a song:
DELETE /songs/<ID>
Example: /songs/123123

Response:
{
  "message": "Song deleted successfully."
}
