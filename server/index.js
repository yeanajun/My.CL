const express = require('express')
const config = require('./config/key');
const app = express()
const port = 3000

const mongoose = require('mongoose')
mongoose.connect(config.mongoURI)
.then(() => console.log('MongoDB Connected...'))
.catch(err => console.log(err))

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})