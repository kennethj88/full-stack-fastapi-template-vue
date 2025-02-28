module.exports = {
  plugins: {
    'postcss-import': {
      // This disables the rule for @import statements position
      skipDuplicates: false,
      path: ['./assets/css/*'],
      order: false
    },
    'tailwindcss/nesting': {},
    tailwindcss: {},
    autoprefixer: {},
    // Any other plugins you're using
  }
}