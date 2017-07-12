class Iterator {
    constructor(iterable, onlyKey) {
        this.iterable = iterable;
        this.onlyKey = onlyKey;
        if (Array.isArray(iterable)) {
            this.keys = Array.from({length: iterable.length}, (v, k) => k);
        } else {
            this.keys = Object.keys(iterable);
        }
        this.length = this.keys.length;
        this.currentIndex = 0;
    }

    next() {
        const nextVal = {done: true};
        if (this.currentIndex < this.length) {
            nextVal.value = this.getPair(this.currentIndex);
            nextVal.done = false;
            this.currentIndex += 1;
        }
        return nextVal;
    }

    [Symbol.iterator]() {
        return this;
    }

    getPair(index) {
        if (this.onlyKey) {
            return this.keys[index];
        }
        if (this.iterable.getValue) return [index, this.iterable.getValue(index)];
        return [this.keys[index], this.iterable[this.keys[index] || index]];
    }

}
function testIterator() {
    const lang = {Javascript: 1, Python: 2, 'C++': 3};
    const it1 = new Iterator(lang);
    for (const pair of it1) {
        console.log(pair); // prints each [index, language] pair in turn
    }

    const langs = ['JavaScript', 'Python', 'C++'];
    const it2 = new Iterator(langs);
    for (const pair of it2) {
        console.log(pair); // prints each [index, language] pair in turn
    }

    const it3 = new Iterator(lang, true);
    for (const key of it3) {
        console.log(key); // prints each [index, language] pair in turn
    }

    const it4 = new Iterator(lang);
    for (const [key, val] of it4) {
        console.log(key, val); // prints each [index, language] pair in turn
    }
}

testIterator();
