import React, { useState, useEffect } from "react";
import axios from "axios";
import { Table, Form, Button } from "react-bootstrap";
import "../index.css";

const divStyle = {
  margin: "8% 8%",
};

const ListLogs = () => {
  const [logs, setLogs] = useState([]);
  const [searchType, setSearchType] = useState("");
  const [searchValue, setSearchValue] = useState("");

  useEffect(() => {
    getLogsList();
  }, []);

  const getLogsList = () => {
    axios
      .get("http://localhost:4000/logs")
      .then((response) => {
        console.log(response);
        setLogs(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const handleSearchTypeChange = (e) => {
    setSearchType(e.target.value);
  };

  const handleSearchValueChange = (e) => {
    setSearchValue(e.target.value);
  };

  const handleSearch = () => {
    if (searchType === "") {
      getLogsList();
    } else {
      axios
        .get(`http://localhost:4000/logs/${searchType}/${searchValue}`)
        .then((response) => {
          console.log(response);
          setLogs(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    }
  };

  return (
    <div style={divStyle}>
      <h1>SIEM PROJECT</h1>
      <br/>
      <Form>
        <Form.Group>
          <Form.Label>Search By:</Form.Label>
          <Form.Check
            type="radio"
            name="searchType"
            label="Ip_addr"
            value="Ip_addrLog"
            onChange={handleSearchTypeChange}
          />
          <Form.Check
            type="radio"
            name="searchType"
            label="Date"
            value="DateLog"
            onChange={handleSearchTypeChange}
          />
          <Form.Check
            type="radio"
            name="searchType"
            label="Month"
            value="MonthLog"
            onChange={handleSearchTypeChange}
          />
          <Form.Check
            type="radio"
            name="searchType"
            label="Severity"
            value="SeverityLog"
            onChange={handleSearchTypeChange}
          />
          <Form.Check
            type="radio"
            name="searchType"
            label="Facility"
            value="FacilityLog"
            onChange={handleSearchTypeChange}
          />
        </Form.Group>
        <br/>
        <Form.Group>
          <Form.Label>Search Value:</Form.Label>
          <Form.Control
            type="text"
            name="searchValue"
            value={searchValue}
            onChange={handleSearchValueChange}
          />
        </Form.Group>
        <br/>
        <Button variant="primary" onClick={handleSearch}>
          Search
        </Button>
      </Form>
      <br/>
      <Table responsive>
        <thead>
          <tr>
            <th>#</th>
            <th>IP Address</th>
            <th>Month</th>
            <th>Date</th>
            <th>Time</th>
            <th>Severity</th>
            <th>Faciltiy</th>
            <th>Message</th>
          </tr>
        </thead>
        <tbody>
          {logs &&
            logs.map((log, i) => {
              return (
                <tr key={i}>
                  <td>{i}</td>
                  <td>{log.ip_addr}</td>
                  <td>{log.month}</td>
                  <td>{log.date}</td>
                  <td>{log.time}</td>
                  <td>{log.severity}</td>
                  <td>{log.facility}</td>
                  <td>{log.message}</td>
                 
                </tr>
              );
            })}
        </tbody>
      </Table>
    </div>
  );
};

export default ListLogs;