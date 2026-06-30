import { useState } from "react";
import Editor from "@monaco-editor/react";

function App() {

  const [socket, setSocket] = useState(null);
  const [code, setCode] = useState("// Welcome to CodeSync 🚀");
  const [room, setRoom] = useState("ABC123");

  function connect() {

    const ws = new WebSocket(
      `ws://localhost:8000/ws/${room}`
    );

    ws.onopen = () => {

      console.log("Connected!");

    };

    ws.onmessage = (event) => {

      setCode(event.data);

    };

    setSocket(ws);

  }

  function handleChange(value) {

    setCode(value);

    if (
      socket &&
      socket.readyState === WebSocket.OPEN
    ) {

      socket.send(value);

    }

  }

  return (

    <div>

      <div
        style={{
          padding:10,
          display:"flex",
          gap:10
        }}
      >

        <input
          value={room}
          onChange={(e)=>setRoom(e.target.value)}
        />

        <button
          onClick={connect}
        >
          Connect
        </button>

      </div>

      <Editor

        height="90vh"

        defaultLanguage="python"

        theme="vs-dark"

        value={code}

        onChange={handleChange}

      />

    </div>

  );

}

export default App;