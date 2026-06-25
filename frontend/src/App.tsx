import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import History from "./pages/History";
import Layout from "./components/Layout";
import Resume from "./pages/Resume";

function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path='/' element={<Dashboard />} />
        <Route path='/resume' element={<Resume />} />
        <Route path='/history'element={<History />} />
      </Route>

    </Routes>
    
  );
}

export default App;