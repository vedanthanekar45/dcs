const express = require('express');
const app = express();

app.use(express.json());

app.post('/add', (req, res) => {
    const { num1, num2 } = req.body;
    if (typeof num1 !== 'number' || typeof num2 !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Please send num1 and num2 as numbers.' });
    }
    const sum = num1 + num2;
    const result = {
        result: sum
    };
    res.json(result);
});

const port = 3000;
app.listen(port, () => {
    console.log(`Express server is running at http://localhost:${port}`);
    console.log('Listening for POST requests at /add');
});