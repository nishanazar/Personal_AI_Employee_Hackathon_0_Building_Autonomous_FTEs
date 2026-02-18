---
title: MCP Email Server Setup - Silver Tier
date: 2026-02-13
status: in_progress
---

## MCP Email Server (Node.js) - Quick Setup Guide

Goal: Claude ko real email bhejne ki permission dena (test ke liye)

1. Node.js install karo (agar nahi hai): https://nodejs.org → LTS version download
2. Broze folder mein jao: cd C:\Users\USER\hackthon_0\Broze
3. New folder banao: mkdir mcp-email-server
4. Folder mein jao: cd mcp-email-server
5. NPM init -y
6. Install dependencies: npm install express nodemailer body-parser
7. index.js file banao aur yeh code paste karo:

const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Yeh transporter Gmail ke liye hai (tum apna email/password daal sakti ho test ke liye)
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'YOUR_EMAIL@gmail.com',      // apna Gmail daalo
    pass: 'YOUR_APP_PASSWORD'          // Gmail App Password banao (2SV on hai to)
  }
});

app.post('/send-email', (req, res) => {
  const { to, subject, text } = req.body;
  const mailOptions = { from: 'YOUR_EMAIL@gmail.com', to, subject, text };
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) return res.status(500).send(error.toString());
    res.send('Email sent: ' + info.response);
  });
});

app.listen(3000, () => console.log('MCP Email Server running on port 3000'));

8. App password banao (agar 2SV on hai): myaccount.google.com → Security → App passwords
9. Run karo: node index.js
10. Claude MCP config mein add karo (future step)