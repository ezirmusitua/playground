const fs = require('fs');
function thread(fn) {
    const gen = fn();
    function next(err, res) {
        const ret = gen.next(res && res.slice && res.slice(0, 25));
        if (ret.done) return;
        ret.value(next);
    }

    next();
}

function read(path) {
    return (done) =>{
        fs.readFile(path, 'utf8', done);
    }
}

function * generatorRead() {
    console.log('use generator and thread to read files. ');
    const a = yield read('./example-file1.txt');
    const b = yield read('./example-file2.txt');
    console.log(a);
    console.log(b);
}

function normalRead() {
    console.log('normal read files without flow control. ');
    fs.readFile('./example-file1.txt', 'utf8', function (err, data) {
        console.log('file 1 done');
    });
    fs.readFile('./example-file2.txt', 'utf8', function (res, data) {
        console.log('file 2 done');
    });
}

thread(generatorRead);
normalRead();

