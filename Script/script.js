function logClick(event) {
    event.preventDefault();
    let clickDetails = null;

    // Get the current page name
    const pageName = window.location.pathname;

    // Check if the clicked element is a button or link
    if (event.target.tagName.toLowerCase() === 'button' || event.target.tagName.toLowerCase() === 'a') {
        // Populate the clickDetails object
        clickDetails = {
            page: pageName,
            timestamp: new Date().toISOString(),
            element: event.target.tagName,
            textContent: event.target.innerText,
            x: event.clientX,
            y: event.clientY
        };

        // Log the clickDetails object to check its content
        console.log("User Clicked:", clickDetails);
    }

    // Only log and send clickDetails if it is not null (i.e., a button or link was clicked)
    if (clickDetails) {
        // Send click data to the server
        fetch('http://127.0.0.1:5000/log_click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(clickDetails)
        })
            .then(response => {
                console.log('Server Response Status:', response.status);
                return response.json();
            })
            .then(data => console.log('Server Response:', data))
            .catch(error => console.error('Error:', error));
    }
}

// Add event listener to track clicks on the whole document
document.addEventListener('click', logClick);
