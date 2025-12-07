import Image from "next/image";

export default function PredictionBox({ title, image, prediction }) {
  return (
    <div className="bg-white p-5 rounded-xl shadow-lg border">
      <h3 className="font-semibold text-gray-700 mb-2">{title}</h3>

      {image && (
        <Image
          src={image}
          alt={title}
          width={224}
          height={224}
          className="rounded-md w-full"
        />
      )}

      <p className="mt-3">
        Prediction: <b>{prediction || "—"}</b>
      </p>
    </div>
  );
}
