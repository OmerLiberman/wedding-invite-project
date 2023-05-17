const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const config = require('config');

const dbUri = config.get('mongoURI');

const app = express();

// Middlewares
app.use(express.json());
app.use(cors());

// Routes
app.use('/api/attendies', require('./api/attendies'));

// DB connection establishment.
mongoose.connect(dbUri,
    {
      useNewUrlParser: true,
      useUnifiedTopology: true
    })
    .then(() => {
      console.log('Connection to db has been established.');
    })
    .catch(err => {
          console.error(err);
          process.exit(1);
    }
);

// Port
const PORT = process.env.PORT || 3001;
app.listen(PORT);

console.log(`App is listening to port ${PORT}.`);

app.get('/', (req, res, next) => {
  return res.status(200).json({message: 'Fuck Hazrati!'});
});