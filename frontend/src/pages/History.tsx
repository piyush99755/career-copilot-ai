import { useEffect, useState } from "react";
import {getHistory} from "../services/api";

interface Analysis {
  id: number;
  role: string;
  skills: string;
  difficulty: string;
  market_demand: string;
  match_score: number;
}

const History = () => {
  const [history, setHistory] = useState<Analysis[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const data = await getHistory();
        setHistory(data);
      } catch{
        setError("Failed to load history.");
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  if (loading)
    return <p className="text-gray-600">Loading...</p>;

  if (error)
    return <p className="text-red-500">{error}</p>;

  if (history.length === 0)
    return <p>No analyses found.</p>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">
        Analysis History
      </h1>

      <div className="space-y-4">
        {history.map((item) => (
          <div
            key={item.id}
            className="rounded-lg bg-white shadow p-5"
            >
            <h2 className="font-semibold text-lg">
                {item.role}
            </h2>

            <p>
                Match Score: {item.match_score}%
            </p>

            <p>
                Difficulty: {item.difficulty}
            </p>

            <p>
                Market Demand: {item.market_demand}
            </p>

            <p>
                Skills: {item.skills}
            </p>
            </div>
        ))}
      </div>
    </div>
  );
};

export default History;