const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// List of columns for Employee schema
let Logs = new Schema(
  {
    ip_addr: {
      type: String,
    },
    month: {
      type: String,
    },
    date: {
      type: String,
    },
    time: {
      type: String,
    },
    facility: {
      type: String,
    },
    mnemonic: {
      type: String,
    },
    severity: {
      type: String,
    },
    message: {
      type: String,
    },
  },
  {
    collection: "win2_log",
  }
);

module.exports = mongoose.model("Log", Logs);