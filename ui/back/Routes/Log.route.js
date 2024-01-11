const express = require("express");
const logRoute = express.Router();
const logModel = require("../Model/Log");

// To Get Log Details By ip_addr
logRoute.route("/Ip_addrlog/:Ip_addr").get((req, res) => {
  const Ip_addr = req.params.Ip_addr;
  logModel
    .find({ ip_addr: Ip_addr })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});


// To Get Log Details By month
logRoute.route("/MonthLog/:Month").get((req, res) => {
  const Month = req.params.Month;
  logModel
    .find({ month: Month })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});

// To Get Log Details By Date
logRoute.route("/DateLog/:Date").get((req, res) => {
  const Date = req.params.Date;
  logModel
    .find({ date: Date })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});

// To Get Log Details By time
logRoute.route("/TimeLog/:Time").get((req, res) => {
  const Time = req.params.Time;
  logModel
    .find({ time: Time })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});

// To Get Log Details By Hostname
logRoute.route("/FacilityLog/:Facility").get((req, res) => {
  const Facility = req.params.Facility;
  logModel
    .find({ facility: Facility })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});

// To Get Log Details By Hostname
logRoute.route("/MnemonicLog/:Mnemonic").get((req, res) => {
  const Mnemonic = req.params.Mnemonic;
  logModel
    .find({ mnemonic: Mnemonic })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});

// To Get Log Details By Severity
logRoute.route("/SeverityLog/:Severity").get((req, res) => {
  const Severity = req.params.Severity;
  logModel
    .find({ severity: Severity })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});


// To Get Log Details By Message
logRoute.route("/MessageLog/:Message").get((req, res) => {
  const Message = req.params.Message;
  logModel
    .find({ message: Message })
    .then((logs) => {
      res.json(logs);
    })
    .catch((error) => {
      console.log(error);
      res.status(500).json({ error: "An error occurred" });
    });
});

module.exports = logRoute;