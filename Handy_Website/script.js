// Select the textarea and button
let text = document.getElementById('text');
const send = document.getElementById('send');

// Ensure the button exists before adding an event listener
if (send) {
    send.addEventListener("click", function() {
        let textValue = text.value.trim();

        // Check if the textarea is empty
        if (textValue === "") {
            alert("You need to enter something");
        } else {
            fetch('http://127.0.0.1:5000/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ finalText: textValue })
            })
            .then(response => response.json())
            .then(data => {
                console.log("Response from server:", data);
                alert("Server response: " + data.received_text);
            })
            .catch(error => console.error('Error:', error));
        }
    });
} else {
    console.error("Button with ID 'send' not found!");
}