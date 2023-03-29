const express = require('express');
const bodyParser = require('body-parser')
const app = express();
const port = 80;
var valorSinalLatest = 0;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.text({type:"*/*"}));
app.post('/', (req, res) => {
    console.log(req.body);
    valorSinalLatest = req.body;
    res.send(`${valorSinalLatest}`);
});
app.get('/', (req, res) => {
    res.send(`${valorSinalLatest}`);
});
app.listen(port);
