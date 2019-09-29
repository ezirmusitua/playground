const { DB } = require("../db");
const mongoose = require('mongoose');

async function testReplicaSet() {
  await DB.connect();
  const Model = mongoose.model("Demo", new mongoose.Schema({ success: Boolean }));
  await Model.createCollection();
  const mongoSession = await Model.startSession();
  await mongoSession.startTransaction();
  try {
    await Model.create([{ success: true }], { session: mongoSession });
    await Model.findOneAndDelete
    const doc = await Model.findOne({ success: true })
      .session(mongoSession)
      .exec();
      if (!doc) throw new Error("Create Error"); 
      await mongoSession.commitTransaction();
      console.info("Replica set run successfully and mongo transaction is work")
  } catch (err) {
    console.error(err);
    await mongoSession.abortTransaction();
  } finally {
    mongoSession.endSession();
    await DB.clean();
    await DB.disconnect();
  }
}

testReplicaSet();
