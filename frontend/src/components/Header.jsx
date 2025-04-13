import { Link } from "react-router-dom";
import "./Header.css"; // створиш пізніше

function Header() {
  return (
    <header>
      <div className="logo">gShop</div>
      <input type="text" placeholder="Пошук товарів" />
      <button className="btn">Знайти</button>
      <nav>
        <Link to="/">Головна</Link>
        <Link to="/feedback">Зворотній зв'язок</Link>
        <a href="#">Ввійти</a>
        <a href="#">Реєстрація</a>
      </nav>
    </header>
  );
}

export default Header;
