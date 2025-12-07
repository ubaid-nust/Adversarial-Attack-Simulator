"use client";

import { useState } from "react";
import ImageUploader from "@/components/ImageUploader";
import EpsilonSlider from "@/components/EpsilonSlider";
import AttackButton from "@/components/AttackButton";
import Results from "@/components/Results";

export default function Home() {
  const [image, setImage] = useState(null);
  const [epsilon, setEpsilon] = useState(0.1);
  const [loading, setLoading] = useState(false);

  const [cleanPrediction, setCleanPrediction] = useState("");
  const [advPrediction, setAdvPrediction] = useState("");
  const [attackSuccess, setAttackSuccess] = useState(null);

  const [cleanPreview, setCleanPreview] = useState(null);
  const [advImage, setAdvImage] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setImage(file);
    setCleanPreview(URL.createObjectURL(file));
  };

  const runAttack = async () => {
    if (!image) return alert("Please upload an image first.");
    setLoading(true);

    const formData = new FormData();
    formData.append("file", image);
    formData.append("epsilon", parseFloat(epsilon));

    try {
      const response = await fetch("http://54.169.204.64:8000/attack/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      setCleanPrediction(data.clean_prediction);
      setAdvPrediction(data.adversarial_prediction);
      setAttackSuccess(data.attack_success);
      setAdvImage(`data:image/png;base64,${data.base64_adv_image}`);
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen py-10 px-4 flex flex-col items-center bg-gradient-to-b from-gray-100 to-gray-200">

      <h1 className="text-3xl sm:text-4xl font-bold mb-8 text-gray-800 text-center">
        FGSM Adversarial Attack Demo
      </h1>

      <div className="bg-white w-full max-w-2xl shadow-xl rounded-2xl p-6 sm:p-8 border border-gray-100">

        <div className="p-4 mb-6 bg-blue-50 border-l-4 border-green-600 text-green-700 rounded text-sm sm:text-base">
          This model is trained for <b>animal classification</b>.  
          Please upload clear animal images for best results.
        </div>

        <ImageUploader handleFileChange={handleFileChange} />
        <EpsilonSlider epsilon={epsilon} setEpsilon={setEpsilon} />
        <AttackButton onClick={runAttack} loading={loading} />
      </div>

      {(cleanPrediction || advPrediction) && (
        <Results
          cleanPrediction={cleanPrediction}
          advPrediction={advPrediction}
          cleanPreview={cleanPreview}
          advImage={advImage}
          attackSuccess={attackSuccess}
        />
      )}
    </div>
  );
}