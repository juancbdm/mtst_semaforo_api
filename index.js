const express = require('express');
const bodyParser = require('body-parser')
const app = express();
const port = 80;
var valorSinalLatest = {"valueS": "1"};
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.post('/', (req, res) => {
    valorSinalLatest =  Object.keys(req.body)[0];
    res.send(`${valorSinalLatest}`);
});
app.get('/', (req, res) => {
    res.send(`${valorSinalLatest}`);
});
app.listen(port);
