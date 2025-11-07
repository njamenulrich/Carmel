/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./carmel/templates/_base.html", "./carmel/templates/home.html"],
  theme: {
    extend: {
      fontFamily: {
        custom: ["OpenSans", "sans-serif"], // 'custom' is your utility class name
        // Add other fallback fonts as needed
      },
    },
  },
  plugins: [],
};

