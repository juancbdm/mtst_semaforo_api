const express = require('express');
const bodyParser = require('body-parser')
const app = express();
const port = 80;
var valorSinalLatest = "1";
app.use(bodyParser.text());
app.use(bodyParser.urlencoded({ extended: true }));
app.post('/', (req, res) => {
    valorSinalLatest = req.body
    if (typeof req.body === 'string') {
        valorSinalLatest = req.body
    }else {
        valorSinalLatest = Object.keys(req.body)[0]
    }
    console.log("definir variavel: " + valorSinalLatest);
    res.send(valorSinalLatest);
});
app.get('/', (req, res) => {
    console.log("variavel atual: " + valorSinalLatest);
    res.send(valorSinalLatest);
});
app.listen(port);
