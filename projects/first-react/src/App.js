import React from "react"
// eslint-disable-next-line
import ProfilePicture from "./components/pic.jpg"
import Info from "./components/Info"
import About from "./components/About"
import Interests from "./components/Interests"
import Footer from "./components/Footer"
import "./index.css"


export default function App(){
    return(
        <div className = "container">
            <div className="pics">
                <img src = {ProfilePicture} className = "pic" alt = "pic" />
            </div>
            <div className="main">
                <Info />
                <About />
                <Interests />
            </div>
            <Footer />
        </div>

    )
}
