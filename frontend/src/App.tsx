import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import History from "./pages/History";
import Layout from "./components/Layout";
import Resume from "./pages/Resume";
import ResumeMatch from "./pages/ResumeMatch";
import CareerChat from "./pages/CareerChat";

function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path='/' element={<Dashboard />} />
        <Route path='/resume' element={<Resume />} />
        <Route path='/history'element={<History />} />
        <Route path='/resume-match' element={<ResumeMatch />} />
        <Route path='career-chat' element={<CareerChat />} />
      </Route>

    </Routes>
    
  );
}

export default App;