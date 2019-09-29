const mongoose = require('mongoose');

const Commodity = mongoose.model('Commodity', mongoose.Schema({
  name: String,
  stock: Number
}));

const Order = mongoose.model('Order', mongoose.Schema({
  commodityId: String,
  user: String,
}));

const created = {};

module.exports = {
  getCollection: async function (name) {
    let collection;
    if (name === 'Commodity') {
      collection = Commodity;
    } else if (name === 'Order') {
      collection = Order;
    } else {
      throw new Error("Invalid Collection Name, Candidates Are Commodity, Order");
    }
    if (!created[name]) {
      created[name] = true;
      await collection.createCollection();
    };
    return collection;
  }
}