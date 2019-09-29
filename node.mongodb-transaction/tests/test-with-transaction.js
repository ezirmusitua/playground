const mongoose = require("mongoose");
const { DB } = require("../db");
const { getCollection } = require("../collections");
const { sleep } = require("../utils");

async function createOrder(user, commodityId, blockts = 0) {
  const Commodity = await getCollection("Commodity");
  const Order = await getCollection("Order");
  const mongoSession = await mongoose.startSession();
  await mongoSession.startTransaction();
  try {
    let commodity = await Commodity.findOne({_id: commodityId, stock: {$gte: 1}})
      .session(mongoSession).lean().exec();
    if (!commodity) throw new Error("Out Of Stock");
    if (blockts) {
      await sleep(blockts);
    }
    const [[created], updated] = await Promise.all([
      Order.create([{ user, commodityId }], {session: mongoSession}),
      await Commodity.findOneAndUpdate(
        {_id: commodityId, stock: {$gte: 1}}, 
        {$inc: {stock: -1}}, 
        {useFindAndModify: false}
      ).session(mongoSession).exec()
    ]);
    if (!updated) throw new Error("Out Of Stock");
    console.info(`Order Created For ${created.user}`);
    await mongoSession.commitTransaction();
  } catch {
    console.info(`Order Created For ${user} Aborted`);
    await mongoSession.abortTransaction();
  } finally {
    mongoSession.endSession();
  }
}

async function main() {
  await DB.connect();
  const Commodity = await getCollection("Commodity");
  const Order = await getCollection("Order");
  try {
    let commodity = await Commodity.create({
      name: "吮指原味鸡",
      stock: 1
    });
    createOrder('A', commodity._id.toString(), 1000);
    createOrder('B', commodity._id.toString(), 0);
  } catch (err) {
    console.error("Exception: ", err);
  } finally {
    await sleep(2000);
    const currentCommodity = await Commodity.findOne().lean().exec();
    const orderCount = await Order.estimatedDocumentCount({}).exec();
    console.info(`Finally Commidity ${currentCommodity.name} Stock ${currentCommodity.stock}`);
    console.info(`Finally Order Count: ${orderCount}`);
    await DB.clean();
    await DB.disconnect();
  }
}

main();
