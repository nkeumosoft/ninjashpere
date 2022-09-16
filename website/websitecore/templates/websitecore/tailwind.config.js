/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
const taiwindForms = require("@tailwindcss/forms");

module.exports = {
  content: ["./public/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: "#0096C7",
        secondary: "#03045E",
        accent: "#48CAE4",
        "accent-green": "#003045",
      },
      fontFamily: {
        sans: ["Source Sans Pro", ...defaultTheme.fontFamily.sans],
        poppins: ["Poppins", ...defaultTheme.fontFamily.sans],
        display: ["Lexend", ...defaultTheme.fontFamily.serif],
      },
      backgroundImage: {
        bottomWaveSlice: "url('assets/bottomWaveSlice.svg')",
        topWaveSlice: "url('assets/topWaveSlice.svg')",
      },
    },
  },
  plugins: [taiwindForms],
};
