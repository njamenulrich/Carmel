// script.js

const shapes = document.querySelectorAll(".shape");
const container = document.getElementById("moving-background");
const containerWidth = container.offsetWidth;
const containerHeight = container.offsetHeight;

// Configuration for movement
const MAX_SPEED = 2; // Maximum pixel movement per step
const UPDATE_INTERVAL = 50; // Milliseconds between position updates

// Initialize state for each shape
const shapeStates = Array.from(shapes).map((shape) => {
  // Start at a random position
  const startX = Math.random() * (containerWidth - shape.offsetWidth);
  const startY = Math.random() * (containerHeight - shape.offsetHeight);

  return {
    element: shape,
    // Current position
    x: startX,
    y: startY,
    // Random direction and speed
    dx: (Math.random() - 0.5) * MAX_SPEED,
    dy: (Math.random() - 0.5) * MAX_SPEED,
  };
});

function moveShapes() {
  shapeStates.forEach((state) => {
    const shape = state.element;

    // 1. Update Position
    state.x += state.dx;
    state.y += state.dy;

    // 2. Boundary Check (Bouncing off the walls)
    // Check X boundary
    if (state.x + shape.offsetWidth > containerWidth || state.x < 0) {
      state.dx = -state.dx; // Reverse horizontal direction
      // Keep it within bounds to prevent sticking
      state.x = Math.max(
        0,
        Math.min(state.x, containerWidth - shape.offsetWidth)
      );
    }

    // Check Y boundary
    if (state.y + shape.offsetHeight > containerHeight || state.y < 0) {
      state.dy = -state.dy; // Reverse vertical direction
      state.y = Math.max(
        0,
        Math.min(state.y, containerHeight - shape.offsetHeight)
      );
    }

    // 3. Apply Movement using CSS Transform for performance
    shape.style.transform = `translate(${state.x}px, ${state.y}px)`;
  });
}

// Start the animation loop
setInterval(moveShapes, UPDATE_INTERVAL);

// Optional: Recalculate container size on window resize
window.addEventListener("resize", () => {
  containerWidth = container.offsetWidth;
  containerHeight = container.offsetHeight;
});
