import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import Body from "./components/Body";
import Login from "./components/Login";
import About from "./components/About";
import Contact from "./components/Contact";
import Footer from "./components/Footer";


function App() {
    const appStyle = {
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
        margin: 0,
    }

    const mianStyle = { 
        flex :1
    }
    return (
        <BrowserRouter>
            <div style={appStyle}>
                <Header />
                    <main style={mianStyle}>
                        <Routes>
                            <Route path="/" element={<Body />} />
                            <Route path="/about" element={<About />} />
                            <Route path="/login" element={<Login />} />
                            <Route path="/contact" element={<Contact />}/>
                        </Routes>
                    </main>
                    <Routes>
                        <Route path="/" element={<Footer />}/>
                    </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;
