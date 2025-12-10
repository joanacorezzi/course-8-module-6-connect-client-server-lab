
// 1. When the page loads, fetch the existing events from the server
fetch("http://localhost:5000/events")
  .then(response => response.json())      // convert the response to JSON
  .then(events => {
    
    // loop through each event and render it on the page
    events.forEach(renderEvent);
  });

// 2. Listen for the form submission to create a new event
document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault(); // prevent the browser from refreshing the page on form submit

  // get the event title from the input with id="title"
  const title = document.querySelector("#title").value;

  // send a POST request to the backend with the new title
  fetch("http://localhost:5000/events", {
    method: "POST",                                // HTTP method
    headers: { "Content-Type": "application/json" }, 
    body: JSON.stringify({ title })               
  })
  .then(response => response.json())              // convert response to JSON
  .then(renderEvent);                             // add the new event to the page
});

// 3. Helper function to show one event inside the <ul id="event-list">
function renderEvent(event) {
  // create a new <li> element
  const li = document.createElement("li");

  // set the text of the <li> to the event title
  li.textContent = event.title;

  // find the list with id="event-list" and append 
  document.querySelector("#event-list").appendChild(li);
}
