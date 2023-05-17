const {Schema, model} = require('mongoose');

const Attender = new Schema({
    name: {type: String, required: true},
    phone: {type: String, required: true},
    status: {type: String, default: '?'},
    attendies: {type: Number, default: -1},
    recognized: {type: Boolean},
    kosher: {type: Array},
});

module.exports = model('Attender', Attender);