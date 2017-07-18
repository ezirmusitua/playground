const co = require('co');

co(function* () {
    // yield any promise
    const result = yield Promise.resolve(true);
    console.log(result);
}).catch(onerror);

co(function* () {
    // resolve multiple promises in parallel
    const a = yield Promise.resolve(1);
    const b = yield Promise.resolve(a + 1);
    const c = yield Promise.resolve(b + 4);
    const res = yield [a, b, c];
    console.log(res);
    // => [1, 2, 3]
}).catch(onerror);

// errors can be try/catched
co(function* () {
    try {
        yield Promise.reject(new Error('boom'));
    } catch (err) {
        console.error(err.message); // "boom"
    }
}).catch(onerror);

function onerror(err) {
    // log any uncaught errors
    // co will not throw any errors you do not handle!!!
    // HANDLE ALL YOUR ERRORS!!!
    console.error(err.stack);
}
