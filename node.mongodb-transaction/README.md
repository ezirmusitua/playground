# Demo of using mongodb transaction

[Blog Post](https://blog.ezirmusitua.site/posts/005_how-to-use-mongo-transaction)

## File usage

`tests/test-*` - test file
`collection.js` - demo used collection definition
`db.js` - encapsulation of mongodb-memory-server replica set
`utils.js` - helper functions

## How to test

to test mongodb-memory-server encapsulation, run:

```bash
node tests/test-db.js
```

to test use mongodb transaction, run:

```bash
node tests/test-with-transaction.js
```

## Note:

<p style="color:red">Only Supported For Nodejs>=12</p>
