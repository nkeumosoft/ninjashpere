/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
const taiwindForms = require("@tailwindcss/forms");

module.exports = {
  content: ["./public/**/*.{html,js}"],
  theme: {
    extend: {
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
