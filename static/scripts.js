function sendMessage(characterName) {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    const chatHistory = document.getElementById('chat-history');
    const userProfilePicture = getCookie('user_profile_picture');
    const userName = getCookie('user_name');
    const botProfilePicture = document.getElementById('bot-profile-picture').src;

    console.log(`User profile picture: ${userProfilePicture}`);
    console.log(`User name: ${userName}`);
    console.log(`Character name: ${characterName}`);
    console.log(`Bot profile picture: ${botProfilePicture}`);

    if (!userProfilePicture || !userName) {
        console.error('User profile picture or user name is missing.');
        return;
    }

    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.innerHTML = `<img src="${userProfilePicture}" alt="User"><strong>${userName}:</strong> ${userInput}`;
    chatHistory.appendChild(userMessage);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput, character: characterName })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            const errorMessage = document.createElement('div');
            errorMessage.className = 'error-message';
            errorMessage.textContent = `Error: ${data.error}`;
            chatHistory.appendChild(errorMessage);
        } else {
            const botMessage = document.createElement('div');
            botMessage.className = 'assistant-message';
            botMessage.innerHTML = `<img src="${botProfilePicture}" alt="Bot"><strong>${characterName}:</strong> ${data.response}`;
            chatHistory.appendChild(botMessage);
        }
        chatHistory.scrollTop = chatHistory.scrollHeight;
    })
    .catch(error => {
        const errorMessage = document.createElement('div');
        errorMessage.className = 'error-message';
        errorMessage.textContent = `Error: ${error.message}`;
        chatHistory.appendChild(errorMessage);
    });

    document.getElementById('user-input').value = '';
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}
