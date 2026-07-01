import { useState } from "react";
import { careerChat } from "../services/api";

const CareerChat = () => {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);

    const handleAsk = async () => {

    if (!question.trim()) return;
    
    setLoading(true);

    try {

        const data = await careerChat(
        question
        );

        setAnswer(
        data.answer
        );

    } catch (error) {

        console.error(error);

    } finally {

        setLoading(false);

    }
    };

    return (
            <div className="max-w-4xl mx-auto p-6">

                <h1>Career Coach Chat</h1>

                <textarea
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                rows={4}
                className="w-full rounded-lg border p-3"
                />

                <br />

                <button onClick={handleAsk}>
                Ask
                </button>

                {loading && (
                <p>Thinking...</p>
                )}

                {answer && (
                <div>
                    <h3>Answer</h3>
                    <div className="mt-4 rounded-lg border p-4 bg-slate-50">
                    <p className="whitespace-pre-wrap">
                        {answer}
                    </p>
                    </div>
                </div>
                )}

            </div>
            );

}
export default CareerChat;