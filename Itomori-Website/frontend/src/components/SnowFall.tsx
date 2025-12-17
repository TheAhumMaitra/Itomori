"use client";

import { useEffect } from "react";

export default function Snowfall() {
  useEffect(() => {
    const container = document.getElementById("snow-container");
    if (!container) return;

    const createSnowflake = () => {
      const flake = document.createElement("span");

      flake.textContent = "❄";
      flake.className =
        "fixed top-0 pointer-events-none select-none text-white animate-snowfall";

      flake.style.left = Math.random() * window.innerWidth + "px";
      flake.style.fontSize = Math.random() * 12 + 10 + "px";
      flake.style.opacity = Math.random().toString();
      flake.style.animationDuration =
        Math.random() * 6 + 6 + "s";

      container.appendChild(flake);

      setTimeout(() => flake.remove(), 12000);
    };

    const interval = setInterval(createSnowflake, 180);

    return () => clearInterval(interval);
  }, []);

  return (
    <div
      id="snow-container"
      className="fixed inset-0 z-50 pointer-events-none"
    />
  );
}
