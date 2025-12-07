"use client";
import React from "react";

export default function EpsilonSlider({ epsilon, setEpsilon }) {
  return (
    <div className="mb-6 w-full">
      <label className="block mb-2 font-semibold text-gray-700 text-sm sm:text-base">
        Epsilon: {epsilon}
      </label>
      <input
        type="range"
        min="0"
        max="0.5"
        step="0.001"
        value={epsilon}
        onChange={(e) => setEpsilon(e.target.value)}
        className="w-full"
      />
    </div>
  );
}