const express = require("express");
const bodyParser = require("body-parser");
const multer = require("multer");
const path = require("path");
const spawn = require("child_process").spawn;

//express object and ejs init
const app = express();
app.set("view engine", "ejs");
app.use(express.static("img"));
app.use(bodyParser.urlencoded({ extended: true }));

file_name = "";
file_type = "";

//multer object and storage init
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "img");
  },
  filename: (req, file, cb) => {
    console.log(file);
    cb(null, file.originalname);
    file_name = file.originalname;
    file_type = file.mimetype.split("/")[0];
    console.log(file_type);
  },
});

const upload = multer({ storage: storage });

app.get("/", function (req, res) {
  res.render("temp");
});

app.post("/", upload.single("image"), function (req, res) {
  res.render("submit", { name: "bw_" + file_name });
  if (file_type == "video") {
    const process1 = spawn("python", ["./main.py", file_name]);
  } else {
    const process2 = spawn("python", ["./gg.py", file_name]);
  }

  process.stdout.on("data", (data) => {
    console.log(data.toString());
  });
});

app.listen(3000, function () {
  console.log("listening on port 3000");
});
