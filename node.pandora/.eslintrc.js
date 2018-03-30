module.exports = {
  'extends': 'google',
  'rules': {
    'semi': ['error', 'never'],
    'comma-dangle': ['error', {
      'arrays': 'never',
      'objects': 'never',
      'imports': 'never',
      'exports': 'never',
      'functions': 'ignore'
    }]
  }
}
