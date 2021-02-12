import logo from './logo.svg';
import './App.css';

import MainForm from './components/MainForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">

        <img src='https://www.johnhancock.com/content/dam/onejohnhancock/images/homepage/JohnHancock_rgb.svg'
          className="App-logo"
          alt="logo" />

        <MainForm />

      </header>
    </div>
  );
}

export default App;
