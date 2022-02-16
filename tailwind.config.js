module.exports = {
  content: [
    "./spapp/templates/**/*.html"
  ],
  theme: {
    extend: {
      colors: {
        primary: "#18345e", /* navyblue */
        tertinary: "#22c1dc", /* lightblue */
        secondary: "#f0ab20", /* yellow */
        red: "#c01f48", /* for errors */
        other: "#007bd6", /* blue */
        lightGrey: "#e5e5e4", /* for background */
        transparent: 'transparent',
        current: 'currentColor',
      },
    },
  },
  plugins: [],
}
