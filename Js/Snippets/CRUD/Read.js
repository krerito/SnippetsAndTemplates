const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 3000;

// Conexión a la base de datos
const db = mysql.createConnection({
    host: '', 
    user: '',
    password: '',
    database: ''
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected to database');
});

// Endpoint para obtener datos
app.get('/getData', (req, res) => {
    const query = "SELECT * FROM some_table"; // Cambiar "some_table" por el nombre real de tu tabla
    db.query(query, (err, results) => {
        if (err) throw err;
        res.send(results);
    });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
