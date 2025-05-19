import React from "react";
import divider from "./divider.svg";
import "./Header.css";

export const Header = () => {
  return (
    <header className="header">
      <section className="header-wrapper">
        <div className="header-content">
          <div className="text-content">
            <p className="breadcrumb" aria-label="Breadcrumb">
              SCREEN TEMPLATES | Web Screen Templates
            </p>
            <div className="title-row">
              <div className="title-container">
                <h1 className="title">Top Menu | Desktop</h1>
              </div>
            </div>
          </div>
          <img
            className="divider"
            alt=""
            src={divider}
            role="presentation"
            loading="lazy"
          />
        </div>
      </section>
    </header>
  );
};
