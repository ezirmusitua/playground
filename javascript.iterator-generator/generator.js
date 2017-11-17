function* simpleGenerator(low, high){
    for (let i = low; i <= high; i += 1) {
        yield i;
    }
}

class Range {
    constructor(low, high) {
        this.low = low;
        this.high = high;
    }

    [Symbol.iterator]() {
        return simpleGenerator(this.low, this.high);
    }
}

class FibGenerator {
    constructor() {}
    *[Symbol.iterator]() {
        let [fn1, fn2] = [0, 1];
        while (true) {
            const current = fn1;
            fn1 = fn2;
            fn2 = current + fn1;
            const _reset = yield current;
            if (_reset) {
                fn1 = 0;
                fn2 = 1;
            }
        }
    }
}

function testFibGenerator() {
    const sequence = new FibGenerator();
    for (const v of sequence) {
        if (v > 9999) break;
       console.log(v)
    }
}

function testRangeGenerator() {
    for (let i of new Range(1, 10)) {
        console.log(i);
    }
}

testRangeGenerator();
testFibGenerator();
