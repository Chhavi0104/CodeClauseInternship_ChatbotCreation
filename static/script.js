document.getElementById('chat-form').addEventListener('submit', async function(e) {
    e.preventDefault(); // prevent page reload
    const userInput = document.getElementById('user-input').value;

    if (userInput) {
        displayMessage('user', userInput);
        const response = await fetch('/get_response', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: userInput })
        });
        const data = await response.json();
        displayMessage('bot', data.response);
    }

    document.getElementById('user-input').value = '';
});

function displayMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom after message is added
}
