// Get form and input/output fields
const form = document.getElementById('form');
const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');

// Handle form submit event
function handleSubmit(event) {
  event.preventDefault();
  
  // Create a new XMLHttpRequest object
  const xhr = new XMLHttpRequest();
  
  // Set the request method and URL
  xhr.open('POST', form.action);
  
  // Set the request header
  xhr.setRequestHeader('Content-Type', 'application/json');
  
  // Define the callback function
  xhr.onload = function() {
    // If the request was successful, update the output field
    if (xhr.status === 200) {
      outputText.value = JSON.parse(xhr.responseText).summary;
      document.getElementById('summary').classList.remove('hidden');
    }
  };
  
  // Send the request with the input text
  xhr.send(JSON.stringify({ 'input-text': inputText.value }));
}

// Handle clear button click event
function clearInput() {
  inputText.value = '';
  outputText.value = '';
  document.getElementById('summary').classList.add('hidden');
}

// Add event listeners
form.addEventListener('submit', handleSubmit);
document.querySelector('button[type="button"]').addEventListener('click', clearInput);
