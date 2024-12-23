document.getElementById('botForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const botName = document.getElementById('botName').value;
    const botLogo = document.getElementById('botLogo').files[0];
    const botInstructions = document.getElementById('botInstructions').value;
    const botGreeting = document.getElementById('botGreeting').value;

    const formData = new FormData();
    formData.append('name', botName);
    formData.append('logo', botLogo);
    formData.append('instructions', botInstructions);
    formData.append('greeting', botGreeting);

    const response = await fetch('/create_bot', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    if (response.ok) {
        alert('Bot created successfully!');
        window.location.href = "/dashboard";
    } else {
        alert(`Error creating bot: ${data.error}`);
    }
});
