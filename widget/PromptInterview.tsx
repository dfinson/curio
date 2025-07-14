import { useState } from 'react';

export default function PromptInterview() {
  const [ws, setWs] = useState<WebSocket | null>(null);
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState('');

  const connect = () => {
    const url = import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws';
    const socket = new WebSocket(url);
    socket.onmessage = (ev) => setMessages((m) => [...m, ev.data]);
    setWs(socket);
  };

  const send = () => {
    if (ws) ws.send(input);
  };

  return (
    <div>
      <button onClick={connect}>Start</button>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={send}>Send</button>
      <ul>
        {messages.map((m, i) => (
          <li key={i}>{m}</li>
        ))}
      </ul>
    </div>
  );
}
