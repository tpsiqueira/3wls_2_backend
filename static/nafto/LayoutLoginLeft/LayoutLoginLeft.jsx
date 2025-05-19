import Checkbox from "@mui/material/Checkbox";
import Icon from "@mui/material/Icon";
import React from "react";
import { AnimatedLabel } from "../AnimatedLabel/AnimatedLabel";
import logoPetrobras from "./logo-petrobras.svg";
import "./LayoutLoginLeft.css";

export const LayoutLoginLeft = () => {
  return (
    <section className="layout-login-left">
      <aside className="login-panel">
        <header className="logo-container">
          <img
            className="logo-petrobras"
            alt="Petrobras logo"
            src={logoPetrobras}
            loading="lazy"
          />
        </header>

        <main className="login-content" role="form" aria-label="Login form">
          <h1 className="login-title">Log in to your account</h1>

          <AnimatedLabel
            className="input email-address"
            state="normal"
            text="Email Address"
          />
          <AnimatedLabel
            className="input password"
            state="normal"
            text="Password"
          />

          <div className="options-row">
            <label className="remember-me">
              <Checkbox
                checked
                icon={
                  <span className="checkbox">
                    <Icon baseClassName="material-icons-two-tone" />
                  </span>
                }
                inputProps={{ "aria-label": "Remember me" }}
              />
              Remember me
            </label>
            <a href="#" className="forgot-password">
              Forgot password?
            </a>
          </div>

          <button className="log-in-button" type="submit">
            <span className="text">Log In</span>
          </button>
        </main>
      </aside>
    </section>
  );
};
