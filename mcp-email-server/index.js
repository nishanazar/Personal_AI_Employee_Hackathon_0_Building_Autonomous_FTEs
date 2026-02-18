const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Yeh transporter Gmail ke liye hai (tum apna email/password daal sakti ho test ke liye)
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'hassebsoomro2233@gmail.com',      // apna Gmail daalo
    pass: 'your_app_password_here'          // Gmail App Password banao (2SV on hai to)
  }
});

app.post('/send-email', (req, res) => {
  const { to, subject, text } = req.body;
  const mailOptions = { from: 'nisha.test.email@gmail.com', to, subject, text };
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) return res.status(500).send(error.toString());
    res.send('Email sent: ' + info.response);
  });
});

app.listen(3000, () => console.log('MCP Email Server running on port 3000'));