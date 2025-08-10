MouseSwipety
A lightweight, dependency-free JavaScript library for detecting mouse swipe gestures on web pages. MouseSwipety allows you to easily add custom interactions by capturing directional swipes.

Features
Simple Integration: Add the script to your HTML and start using it immediately.

No Dependencies: Works with plain JavaScript, no frameworks required.

Configurable: Adjust the swipe sensitivity to fit your needs.

Event-Based: Use a callback function to handle swipe events for different directions.

Installation
To use MouseSwipety, simply include the script in your HTML file before your closing </body> tag.

<script src="path/to/mouse-swipety.js"></script>

Usage
Create a new instance of MouseSwipety, passing in the DOM element you want to monitor for swipes. You can also provide an optional configuration object.

The library will listen for mouse movements within the specified element and trigger a callback function when a swipe is detected.

Example
// Get the element to listen for swipes on
const myElement = document.getElementById('my-container');

// Initialize MouseSwipety with a configuration object
const swipety = new MouseSwipety(myElement, {
  // The minimum distance in pixels for a swipe to be registered
  threshold: 50,
  // The maximum time in milliseconds between mousedown and mouseup
  timeout: 500
});

// Add a listener for swipe events
swipety.onSwipe((direction) => {
  console.log('Swipe detected:', direction);
  // 'direction' will be one of 'up', 'down', 'left', or 'right'
  // You can add your custom logic here based on the direction
});

License
This project is licensed under the MIT License.