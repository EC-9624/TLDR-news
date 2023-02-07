const express = require("express");
const app = express();
const dotenv = require("dotenv");
const cors = require("cors");
const mongoose = require("mongoose");
const morgan = require("morgan");

dotenv.config();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(morgan("dev"));
app.use(cors());

mongoose
  .connect(process.env.MONGO_URL)
  .then(() => {
    console.log("MongoDB Conected!");
  })
  .catch((err) => console.log(err));

//model
const newsSchema = new mongoose.Schema({
  title: String,
  link: String,
  published: String,
  content: String,
});

const News = mongoose.model("News", newsSchema);

//controller
app.get("/", (req, res) => {
  News.find((err, data) => {
    if (err) return res.send(err);
    res.json(data);
  });
});

app.listen(port, () => {
  console.log(`Sever is Running on Port:${port}....`);
});
