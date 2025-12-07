"use client";
import React from "react";

export default function ImageUploader({ handleFileChange }) {
  return (
    <div className="mb-6">
      <label className="block mb-2 font-semibold text-gray-700">
        Upload Image
      </label>
      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="w-full p-2 border rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100"
      />
    </div>
  );
}