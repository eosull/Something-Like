
// Timeout for messages
setTimeout(function() {
    // Target element setup for messages
    let messages = document.getElementById("msg");
    // Trigger a new Bootstrap message
    let alert = new bootstrap.Alert(messages);
    alert.close();
    // Keep open for 3 seconds
}, 3000);
