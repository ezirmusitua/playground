const http = require('http');
const net = require('net');
const url = require('url');

function connect(clientReq, clientSock) {
    const targetUrl = url.parse('http://' + clientReq.url);
    console.log(targetUrl);
    const proxySock = net.connect(targetUrl.port, targetUrl.hostname, () => {
        clientSock.write('HTTP/1.1 200 Connection Established\r\n\r\n');
        proxySock.pipe(clientSock);
    }).on('error', (e) => {
        console.error(e);
        clientSock.end();
    });
    clientSock.pipe(proxySock);
}

http.createServer().on('connect', connect).listen(8888, '0.0.0.0');