import Header from "../Header";  // правильний шлях до Header

function Home() {
  return (
    <>
      <Header />
      <div className="container-fluid d-flex">
        <aside>
          <ul>
            <li><a href="#">Гаджети</a></li>
            <li><a href="#">Телевізори</a></li>
            <li><a href="#">Графічні планшети</a></li>
            <li><a href="#">Ігрові приставки</a></li>
            <li><a href="#">Ігрові маніпулятори</a></li>
            <li><a href="#">Планшети</a></li>
            <li><a href="#">Про нас</a></li>
          </ul>
        </aside>
        <main className="flex-grow-1 p-3">
          <div className="gallery-grid">
            {[ 
              { tag: "pc", img: "pc2.png", title: "Персональні комп'ютери" },
              { tag: "tv", img: "tv.png", title: "TV+відеотехніка" },
              { tag: "monitor", img: "Lenovo20E29w-20.png", title: "Монітори" },
              { tag: "keyboard", img: "key.png", title: "Клавіатури" },
              { tag: "mouse", img: "m.png", title: "Мишки" },
              { tag: "audio", img: "audio.png", title: "Аудіо-техніка" }
            ].map(({ tag, img, title }) => (
              <div className="gallery-item" key={tag}>
                <a href={`/products?tag=${tag}`} className="text-decoration-none">
                  <div className="grid-iteminner">
                    <img src={`/static/img/${img}`} className="grid-itemimg" alt={title} />
                    <div className="grid-itemtitle">
                      <span>{title}</span>
                    </div>
                  </div>
                </a>
              </div>
            ))}
          </div>
        </main>
      </div>
    </>
  );
}

export default Home;
