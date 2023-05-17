const express = require('express');

const Attender = require('../models/attender');

const router = express.Router();

router.post('/', async (req, res) => {
    const {name, phone, status, attendies, recognized, kosher} = req.body;
    console.log('Received: ', req.body)
    if (!name || !phone || !status) {
        res.status(500);
    };
    try {
        const attendy = await new Attender({
            name, 
            phone,
            status,
            attendies,
            recognized,
            kosher,
        });
        await attendy.save();
        res.status(200).send(attendy._id);
    } catch (err) {
        res.status(400).json(err);
    }
});

router.get('/:id', async (req, res) => {
    const {id} = req.params;
    try {
        const attendy = await Attender.findById(id);
        if (attendy) {
            res.status(200).json({
                name: attendy.name,
                attendies: attendy.attendies,
            });
        }
    } catch (err) {
        res.status(401).json({message: 'Unrecognized'});
    }
});

router.put('/', async (req, res) => {
    const {id, name, phone, status, attendies, recognized,  kosher, travel} = req.body;
    if (!id || !name || !phone || !status) {
        res.status(500);
    };
    try {
        await Attender.findOneAndUpdate({_id: id}, {
            name,
            phone,
            status,
            attendies,
            recognized,
        });
    } catch (err) {
        res.status(400).json(err);
    }
    res.status(200).send('updated successfully');
});

router.get('/', async (req, res) => {
    res.status(200).json(await Attender.find());
});

module.exports = router;