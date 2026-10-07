import React from "react";
import '../style/Navbar.css';

function Navbar(){
    return(
        <section className="navbar">
            <a href="/" className="navbar-item">Home</a>
            <a href="/about" className="navbar-item">About</a>
            <a href="/contact" className="navbar-item">Contact</a>
            <a href="/login" className="navbar-item>Login">Login</a>
        </section>
    )
}

export default Navbar;