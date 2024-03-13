// package.json was generated automatically with 'npm init' and contains default values
// also run 'npm i express axios cors dotenv nodemon'
// this provides us with a nodejs server

const PORT = 8000
const axios = require("axios").default
const express = require('express')
const app = express()
const cors = require('cors')
require('dotenv').config()
app.use(cors())

// Arrow functions simplify assigning functions to variables
// Inserting snippet from RapidAPI
app.get('/flights', (req, res) => {
    const options = {
        method: 'GET',
        url: 'https://iatacodes-iatacodes-v1.p.rapidapi.com/api/v9/schedules',
        params: { bbox: '46.01,-12.21,56.84,9.66' },
        headers: {
            'X-RapidAPI-Key': process.env.API_KEY,
            'X-RapidAPI-Host': 'iatacodes-iatacodes-v1.p.rapidapi.com'
        }
    };

    axios.request(options).then(function (response) {
        console.log(response.data);
        res.json(response.data)
    }).catch(function (error) {
        console.error(error);
    });
})

app.listen(PORT, () => console.log('running on PORT ' + PORT))
