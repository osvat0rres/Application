import React, { useState } from "react";
import "../style/Login.css";

function Login() {
const [username, setUsername] = useState("");
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");

const handleSubmit = (e) => {
    e.preventDefault();

    console.log("Login", {
        username,
        email,
        password
    });
};

return (
    <div className="mainBox">

        <div className="login-content">
            <h2 className="main-header">
                Welcome to Expense
            </h2>

            <form onSubmit={handleSubmit}>
                <h2 id="login">Login</h2>

                <div className="main-body">
                    <input type="text" placeholder="Username" 
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />

                    <input type="email" placeholder="Email address"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />

                    <input type="password" placeholder="Password" value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />

                    <button type="submit">
                        Sign In
                    </button>
                </div>
            </form>
        </div>

        <section className="login-image">
            <img src="/expense-illustration.png" alt="Expense tracking illustration" />
        </section>

    </div>
);


}

export default Login;
