import React, { useState, useEffect } from 'react';

function ChatApp() {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState(
        JSON.parse(localStorage.getItem('chatMessages')) || []
        );
    const [ws, setWs] = useState(null); // ws를 상태로 관리

    useEffect(() => {
        const newWs = new WebSocket('ws://localhost:3940/ws');
        setWs(newWs); // ws를 상태에 설정

        newWs.onopen = () => {
            console.log('Connected to WebSocket');
        };

        newWs.onmessage = (event) => {
            setMessages([...messages, event.data]);
        };

        newWs.onclose = () => {
            console.log('WebSocket connection closed');
        };

        return () => {
            newWs.close()
            localStorage.setItem('chatMessages', JSON.stringify(messages));
        };
    }, [messages]);

    const handleSendMessage = () => {
        // ws.send(message);
        // setMessage('');
        if (ws) {
            const newMessage = {
                text: message,
                timestamp: new Date().toLocaleString('ko-KR', {
                    // year: 'numeric',
                    month: 'short',
                    day: 'numeric',
                    hour: 'numeric',
                    minute: 'numeric',
                  }), // 현재 시간을 문자열로 변환
            };
            setMessages([...messages, newMessage]);
            ws.send(JSON.stringify(newMessage)); // 서버에 JSON 형식으로 전송
            setMessage('');
            }
    };

    return (
    <div className="chat-app">
        <h3>
            받은 메시지
        </h3>
        <div className="message-list">
            {messages.map((message, index) => (
            <div key={index} className="message">
            <span style={{ color: 'gray', fontSize: '14px' }}><em>{message.timestamp}</em></span>   | <strong>{message.text}</strong>
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