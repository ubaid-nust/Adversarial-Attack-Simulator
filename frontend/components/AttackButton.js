"use client";
import React from "react";

export default function AttackButton({ onClick, loading }) {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className={`w-full py-3 rounded-xl text-white transition 
        ${loading ? "bg-blue-300 cursor-not-allowed" : "bg-blue-600 hover:bg-blue-700"}
      `}
    >
      {loading ? "Running Attack..." : "Run FGSM Attack"}
    </button>
  );
}
