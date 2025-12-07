import PredictionBox from "./PredictionBox";

export default function Results({
  cleanPrediction,
  advPrediction,
  cleanPreview,
  advImage,
  attackSuccess,
}) {
  return (
    <div className="w-full max-w-4xl mt-12">
      <h2 className="text-2xl font-bold mb-6 text-gray-800">Results</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <PredictionBox
          title="Clean Image"
          image={cleanPreview}
          prediction={cleanPrediction}
        />
        <PredictionBox
          title="Adversarial Image"
          image={advImage}
          prediction={advPrediction}
        />
      </div>

      {/* Attack Success */}
      <p className="mt-6 text-lg">
        Attack Success:{" "}
        <b className={attackSuccess ? "text-green-600" : "text-red-600"}>
          {String(attackSuccess)}
        </b>
      </p>
    </div>
  );
}
