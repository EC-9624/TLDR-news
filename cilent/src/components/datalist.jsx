import React, { useState, useEffect } from "react";
import axios from "axios";

function Datalist() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await axios.get("http://localhost:3000/");
      setData(response.data);
    }

    fetchData();
  }, []);
  return (
    <div className="list">
      <ul>
        {data.map((item) => (
          <li key={item._id}>
            <a href={item.link}>
              <h3>{item.title}</h3>
            </a>
            <p>{item.content}</p>
            <p>{item.published}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Datalist;
