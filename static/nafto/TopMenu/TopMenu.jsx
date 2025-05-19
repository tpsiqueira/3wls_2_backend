import React from "react";
import comentario1 from "./comentario-1.svg";
import group from "./group.png";
import iconeUsuario from "./icone-usu-rio.svg";
import informacoes1 from "./informacoes-1.svg";
import logoPetrobras from "./logo-petrobras.svg";
import menu from "./menu.png";
import vector1 from "./vector-1.svg";
import "./TopMenu.css";

const NAV_LINKS = ["Link 001", "Link 001", "Link 001", "Link 001", "Link 001"];

export const TopMenu = () => {
  return (
    <header className="top-menu">
      <div className="top-menu-container">
        <nav className="navbar" aria-label="Main navigation">
          <button className="menu-button" aria-label="Open menu">
            <img src={menu} alt="Menu icon" />
          </button>

          <h1 className="app-title">Nafto Design System</h1>

          <ul className="nav-links">
            {NAV_LINKS.map((link, index) => (
              <li key={index}>
                <a href="#" className="nav-link">
                  {link}
                </a>
              </li>
            ))}
          </ul>

          <div className="nav-icons">
            <img src={vector1} alt="" aria-hidden="true" className="divider" />
            <img src={iconeUsuario} alt="User icon" className="icon" />
            <img src={group} alt="Group icon" className="icon" />
            <img src={informacoes1} alt="Information icon" className="icon" />
            <img src={comentario1} alt="Comment icon" className="icon" />
            <div className="logo-container">
              <img src={logoPetrobras} alt="Petrobras logo" className="logo" />
            </div>
          </div>
        </nav>
      </div>
    </header>
  );
};
