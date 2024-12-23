document.addEventListener('DOMContentLoaded', async () => {
    const botId = 1; // Replace with dynamic bot ID as needed
    await loadBotSettings(botId);

    document.getElementById('sendBtn').addEventListener('click', async () => {
        const userInput = document.getElementById('userInput').value;
        addMessage('user', userInput);
        document.getElementById('userInput').value = '';

        const response = await fetch(`/chat/${botId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_message: userInput })
        });

        const data = await response.json();
        addMessage('bot', data.message);
    });
});

async function loadBotSettings(botId) {
    const response = await fetch(`/get_bot/${botId}`);
    const bot = await response.json();

    if (bot.logo) {
        document.getElementById('botLogo').src = `/static/uploads/${bot.logo}`;
    }
    document.getElementById('botName').innerText = bot.name;

    if (bot.greeting) {
        addMessage('bot', bot.greeting);
    }
}

function addMessage(sender, text) {
    const chatBox = document.getElementById('chatBox');
    const message = document.createElement('div');
    message.className = sender === 'user' ? 'user-msg' : 'bot-msg';
    message.innerText = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}
