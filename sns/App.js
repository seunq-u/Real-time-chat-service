import React, { useState, useEffect } from 'react';

function ChatApp() {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8000/ws');

        ws.onopen = () => {
            console.log('Connected to WebSocket');
        };

        ws.onmessage = (event) => {
            setMessages([...messages, event.data]);
        };

        ws.onclose = () => {
            console.log('WebSocket connection closed');
        };

        return () => ws.close();
    }, []);

    const handleSendMessage = () => {
        ws.send(message);
        setMessage('');
    };

    return (
    <div className="chat-app">
        <div className="message-list">
            {messages.map((message, index) => (
            <div key={index} className="message">
                {message}
            </div>
            ))}
        </div>
    <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
    />
    <button onClick={handleSendMessage}>Send</button>
    </div>
    );
}

export default    
ChatApp;