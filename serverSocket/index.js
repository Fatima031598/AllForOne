const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

const cors = require("cors");

// const { Controller } = require("./controllers");

const host = "localhost";
const port = 3000;

const corsOptions = {
  origin: "*",
  //   methods: ['GET']
};

app.use(cors(corsOptions));
app.use(express.json());

io.on("connection", (socket) => {
  console.log("a user connected", socket.id);

  socket.on("join room", (roomCode) => {
    console.log("Here is the room code", roomCode);
  });
});

server.listen(port, host, () => {
  console.log(`listening on ${host}:${port}...`);
});