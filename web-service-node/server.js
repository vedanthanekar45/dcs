// server.js
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// Simple endpoints
app.get("/", (req, res) => {
  res.send("Welcome to Simple Web Service!");
});

app.get("/api/hello", (req, res) => {
  res.json({ message: "Hello from the Node.js Web Service 👋" });
});

app.get("/api/student", (req, res) => {
  const student = {
    name: "Shreyas Gadhe",
    branch: "IT",
    year: "3rd Year",
    college: "KBTCOE Nashik",
  };
  res.json(student);
});

app.get("/api/greet", (req, res) => {
  const name = req.query.name || "Guest";
  res.json({ message: `Hello ${name}, nice to meet you!` });
});

// Start server
const PORT = 4000;
app.listen(PORT, () => console.log(`✅ Server running on http://localhost:${PORT}`));
