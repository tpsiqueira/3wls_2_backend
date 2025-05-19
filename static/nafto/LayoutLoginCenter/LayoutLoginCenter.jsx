import Checkbox from "@mui/material/Checkbox";
import Icon from "@mui/material/Icon";
import React from "react";
import { AnimatedLabel } from "../AnimatedLabel/AnimatedLabel";
import logoPetrobras from "./logo-petrobras.svg";
import "./LayoutLoginCenter.css";

export const LayoutLoginCenter = () => {
  return (
    <main className="layout-login-center">
      <section className="login" aria-labelledby="login-title">
        <h1 id="login-title" className="login-title">
          Log in to your account
        </h1>

        <form className="login-form" noValidate>
          <AnimatedLabel
            className="email-address"
            state="normal"
            text="Email Address"
          />
          <AnimatedLabel className="password" state="normal" text="Password" />

          <div className="login-options">
            <label className="remember-me">
              <Checkbox
                checked
                icon={
                  <span className="checkbox">
                    <Icon baseClassName="material-icons-two-tone" />
                  </span>
                }
              />
              <span>Remember me</span>
            </label>

            <a href="#" className="forgot-password">
              Forgot password?
            </a>
          </div>

          <button type="submit" className="button">
            <span className="text">Log In</span>
          </button>
        </form>
      </section>

      <div className="rectangle" aria-hidden="true" />

      <img
        className="logo-petrobras"
        alt="Petrobras logo"
        src={logoPetrobras}
        loading="lazy"
      />
    </main>
  );
};
