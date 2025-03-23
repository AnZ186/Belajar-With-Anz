/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/*"
  ],
  theme: {
    extend: {
      colors: {
        'darkpink': '#E9456C',
        'darkblue': '#052842',
      },
      fontFamily: {
        Winky: ['Winky Sans', ]
      }
    },
  },
  plugins: [],
}

