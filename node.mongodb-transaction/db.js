const { MongoMemoryReplSet } = require("mongodb-memory-server");
const mongoose = require("mongoose");
const {sleep} = require('./utils');

class DB {
  static set;
  static connection;
  static async connect() {
    DB.set = new MongoMemoryReplSet({
      instanceOpts: [
        { storageEngine: "wiredTiger" },
        { storageEngine: "wiredTiger" },
        { storageEngine: "wiredTiger" }
      ]
    });
    await DB.set.waitUntilRunning();
    const uri = `${await DB.set.getConnectionString()}?replicaSet=testset`;
    const dbName = await DB.set.getDbName();
    await sleep(3000); // NOTE: 为了确保本地 Replica set 确实运行了, 再等待一小会儿
    DB.connection = await mongoose.connect(uri, { 
      useNewUrlParser: true, 
      connectTimeoutMS: 3000, // NOTE: 设置等待连接成功时间, 对于本地 Replica set 尽量设置得长一点
            keepAlive: 120 
    });
  }

  static async clean() {
    for (const model of Object.values(DB.connection.models)) {
      await model.deleteMany({});
    }
  }

  static async disconnect() {
    await DB.connection.disconnect();
    await DB.set.stop();
  }
}

module.exports = {DB};
