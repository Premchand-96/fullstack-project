import { useEffect, useState } from "react";
import "./App.css";

function App() {

  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {

    fetch("/api/users")
      .then((res) => res.json())
      .then((data) => setUsers(data));

  }, []);

  return (

    <div className="main-container">

      <div className="overlay"></div>

      <nav className="navbar">
        <div className="logo">Stackly</div>

        <ul>
          <li>Home</li>
          <li>Services</li>
          <li>Cloud</li>
          <li>Contact</li>
        </ul>
      </nav>

      <section className="hero-section">

        <div className="hero-content">

          <h1>AWS FastAPI Deployment</h1>

          <p>
            Full stack deployment using React, FastAPI,
            MySQL, Nginx and AWS EC2.
          </p>

          <button>Deploy Now</button>

        </div>

      </section>

      <section className="api-section">

        <h2>Employee Database</h2>

        <div className="users-grid">

          {users.map((user) => (

            <div className="api-card" key={user.id}>

              <h3>{user.name}</h3>

              <p>{user.email}</p>

              <p>{user.role}</p>

            </div>

          ))}

        </div>

      </section>

    </div>
  );
}

export default App;
