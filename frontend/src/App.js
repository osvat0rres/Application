import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import Body from "./components/Body";
import Login from "./components/Login";
import About from "./components/About";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import Extra from "./components/Extra";

function App() {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path="/" element={<Body />} />
                <Route path="/about" element={<About />} />
                <Route path="/login" element={<Login />} />
                <Route path="/contact" element={<Contact />}/>
            </Routes>
            <Extra />
            <Footer />
        </BrowserRouter>
    );
}

export default App;
