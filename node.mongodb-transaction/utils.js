function sleep(ts) {
  return new Promise((resolve) => setTimeout(() => resolve(), ts));
}

module.exports = {sleep};