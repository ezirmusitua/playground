const { DB } = require("../db");
const { getCollection } = require("../collections");
const { sleep } = require("../utils");

async function createOrder(user, commodityId, blockts = 0) {
  const Commodity = await getCollection("Commodity");
  const Order = await getCollection("Order");
  let commodity = await Commodity.findOne({_id: commodityId, stock: {$gte: 1}})
    .lean().exec();
  if (!commodity) return;
  if (blockts) {
    await sleep(blockts);
  }
  const updated = await Commodity.findOneAndUpdate(
    {_id: commodityId, stock: {$gte: 1}}, 
    {$inc: {stock: -1}}, 
    {useFindAndModify: false}
  ).exec()
  if (!updated) return; // 应该直接 throw, 这里使用 return 只是为了方便测试
  const created = await Order.create({ user, commodityId });
  console.info(`Order Created For ${created.user}`);
}

async function main() {
  await DB.connect();
  const Commodity = await getCollection("Commodity");
  const Order = await getCollection("Order");
  try {
    let commodity = await Commodity.create({
      name: "吮指原味鸡", stock: 1
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
