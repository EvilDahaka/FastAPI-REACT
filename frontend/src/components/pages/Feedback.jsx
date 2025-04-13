import Header from "../components/Header";

function Feedback() {
  return (
    <>
      <Header />
      <div className="form-container">
        <form className="feedback-form" method="POST">
          <h2>Поділіться своїми враженнями</h2>
          <div>
            <input type="text" name="name" required placeholder="Ваше ім'я" />
          </div>
          <div>
            <input type="email" name="email" required placeholder="Ваш email" />
          </div>
          <div>
            <textarea name="message" required rows="5" placeholder="Введіть ваше повідомлення..."></textarea>
          </div>
          <button type="submit">Надіслати</button>
        </form>
      </div>
    </>
  );
}

export default Feedback;
