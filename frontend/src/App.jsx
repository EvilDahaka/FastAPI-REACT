import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/pages/Home"; // Оновлений шлях до компонента
import Feedback from "./components/pages/Feedback"; // Оновлений шлях до компонента

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/feedback" element={<Feedback />} />
      </Routes>
    </Router>
  );
}

export default App;
