
document.addEventListener('DOMContentLoaded', function() {
  var sendButton = document.getElementById('send-btn');
  var newSessionButton = document.getElementById('new-session-btn');
  var userInput = document.getElementById('user-input');
  var chatBox = document.getElementById('chat-box');
  var sessionSidebar = document.getElementById('session-sidebar');
  var sendButton = document.getElementById('send-btn');
  var userInput = document.getElementById('user-input');
  var welcomeMessage = document.getElementById('welcome-message');
  var newSessionButton = document.getElementById('new-session-btn');
  var chatBox = document.getElementById('chat-box');

  // Function to show the welcome message
  function showWelcomeMessage() {
    welcomeMessage.style.display = 'block'; // Show the welcome message
    chatBox.innerHTML = ''; // Clear previous messages
  }

  // Function to hide the welcome message
  function hideWelcomeMessage() {
    welcomeMessage.style.display = 'none';
  }

  // Show the welcome message when the "Start New Conversation" button is clicked
  newSessionButton.addEventListener('click', showWelcomeMessage);

  // Hide the welcome message and send the user's message when the "Send" button is clicked
  sendButton.addEventListener('click', function() {
    // Add the message sending functionality here

    // Hide the welcome message if user input is not empty
    if (userInput.value.trim() !== '') {
      hideWelcomeMessage();
    }
  });

  // Call showWelcomeMessage on page load to display the welcome message initially
  showWelcomeMessage();

  var sessionCounter = 0; // To keep track of the number of sessions
  newSessionButton.addEventListener('click', function() {
    // Show the welcome message when starting a new session
    welcomeContainer.style.display = 'block';
    // Clear the chatbox and hide previous conversation, if needed
    chatBox.innerHTML = '';
    // Optionally, reset other UI elements to their initial state
  });
  function createSessionElement() {
    var sessionElement = document.createElement('div');
    sessionElement.textContent = 'Session ' + (++sessionCounter);
    sessionElement.classList.add('session');
    sessionSidebar.appendChild(sessionElement);
  }
  // Function to add a message to the chat
  function addMessageToChat(sender, message) {
    var messageElement = document.createElement('div');
    messageElement.classList.add('message');

    if (sender === 'user') {
        messageElement.classList.add('user-message');
        messageElement.innerHTML = '<span class="message-logo user-logo"></span>' + message;
    } else { // Bot message
        messageElement.classList.add('bot-message');
        // Simulate a bot response for demonstration
        messageElement.innerHTML = '<span class="message-logo bot-logo"></span>KissanGPT: ' + message;
    }

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}
  // function appendMessage(sender, message) {
  //   var messageDiv = document.createElement('div');
  //   messageDiv.textContent = sender + ': ' + message;
  //   chatBox.appendChild(messageDiv);
  //   chatBox.scrollTop = chatBox.scrollHeight; // Auto scroll to the latest message
  // }
  function callFlaskAPI(userText) {
    console.log("enter to api call")
    fetch('http://localhost:5000/openrouter-query', { // Replace with your Flask API URL if different
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userText })
    })
    .then(response => response.json())
    .then(data => {
      console.error(data);
      addMessageToChat('KisaanGPT', data);
    })
    .catch((error) => {
      console.error('Error:', error);
      addMessageToChat('KisaanGPT', 'Error fetching response');
    });
  }

  // sendButton.addEventListener('click', function() {
  //   var userText = userInput.value.trim();
  //   if (userText !== '') {
  //     console.error(userText); 
  //     appendMessage('User', userText);
  //     callFlaskAPI(userText);
  //     userInput.value = ''; // Clear the input after sending
  //   }
  // });
  sendButton.addEventListener('click', function() {
        var message = userInput.value;
        if (message) {
            addMessageToChat('user', message);
            userInput.value = ''; // Clear input field // Delay for demonstration
            callFlaskAPI(message);
        }
    });
  
  // Handle the "Enter" key to send messages
  userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      sendButton.click();
    }
  });

  newSessionButton.addEventListener('click', function() {
    // Clear previous messages and start a new session
    chatBox.innerHTML = '';
    createSessionElement();
  });
});

