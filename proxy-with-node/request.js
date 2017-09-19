// Reference: https://imququ.com/web-proxy.html  

const http = require('http');
const url = require('url');

function request(clientReq, clientRes) {
    const targetUrl = url.parse(clientReq.url);
    // 利用客户端请求的香港信息构造 http request options  
    const options = {
        hostname: targetUrl.hostname,
        port: targetUrl.port || 80,
        path: targetUrl.path,
        method: clientReq.method,
        headers: clientReq.headers
    };
    
    const proxyReq = http.request(options, (proxyRes) => {
        clientRes.writeHead(proxyRes.statusCode, proxyRes.headers);
        proxyRes.pipe(clientRes);
    }).on('error', (e) => {
        console.error(e);
        clientReq.end();
    });
    
    clientReq.pipe(proxyReq);
}

http.createServer().on('request', request).listen(8888, '0.0.0.0');