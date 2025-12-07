import PredictionBox from "./PredictionBox";

export default function Results({
  cleanPrediction,
  advPrediction,
  cleanPreview,
  advImage,
  attackSuccess,
}) {
  return (
    <div className="w-full max-w-4xl mt-12 px-4">
      <h2 className="text-xl sm:text-2xl font-bold mb-6 text-gray-800 text-center sm:text-left">
        Results
      </h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
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

      <p className="mt-6 text-lg text-center sm:text-left">
        Attack Success:{" "}
        <b className={attackSuccess ? "text-green-600" : "text-red-600"}>
          {String(attackSuccess)}
        </b>
      </p>
    </div>
  );
}
