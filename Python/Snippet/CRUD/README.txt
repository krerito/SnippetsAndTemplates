
# Database Operations Documentation

## Database Connection

The code connects to a MySQL database using the following credentials:

- Host: 100.000.000.000
- Database: TestDB
- User: TestUser
- Password: TestUser

These credentials are for demonstration purposes and need to be replaced with the actual credentials for a production environment.

## Table Format

The operations are demonstrated on a table named `TestKerim`. The structure of the table is as follows:

- `ID_song` (Primary Key): A unique identifier for each song record.
- `songTitle`: The title of the song.
- `songLyrics`: The lyrics of the song.
- `songRelation`: A field to describe the song's relation to any other piece of data or metadata.

## CRUD Operations

CRUD stands for Create, Read, Update, and Delete, which are the four basic functions of persistent storage.

- **Create (INSERT)**: Adds a new song record to the `TestKerim` table.
- **Read (SELECT)**: Reads and retrieves song records from the `TestKerim` table.
- **Update (UPDATE)**: Modifies an existing song record in the `TestKerim` table based on its `ID_song`.
- **Delete (DELETE)**: Removes a song record from the `TestKerim` table based on its `ID_song`.
