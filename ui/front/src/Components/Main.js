import React from "react";
import { Route, Routes, BrowserRouter as Router } from "react-router-dom";
import ListLogs from "../Components/ListLogs";

const Main = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<ListLogs />} />
      </Routes>
    </Router>
  );
};

export default Main;