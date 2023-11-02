
# Node.js and MySQL Database Operations

## Database Connection

The Node.js application connects to a MySQL database using the `mysql` library with the following configuration:

```javascript
const db = mysql.createConnection({
    host: '100.000.000.000',
    user: 'TestUser',
    password: 'TestPass',
    database: 'TestDB'
});
```

Replace the placeholder values with your actual database credentials.

## Database Table Format

The SQL queries are performed on a table named `some_table`. Replace `some_table` with the actual table name you intend to use. The expected table structure is not defined here and should be created according to the needs of the application.

## Endpoint for Data Retrieval

The `/getData` endpoint is set up to perform a `SELECT` query on the database and print the results to the server's console:

```javascript
app.get('/getData', (req, res) => {
    const query = "SELECT * FROM some_table"; // Replace with your table name
    db.query(query, (err, results) => {
        if (err) throw err;
        console.log(results);
        res.send('Check the server console for the query results');
    });
});
```

When this endpoint is accessed, it will print the query results to the console and send a simple message to the client to check the server console for the output.

## Starting the Server

The server is started on port 3000 and will log a message to the console indicating it is running:

```javascript
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
```

To start the server, run the command `node app.js` (assuming your entry file is named `app.js`).
