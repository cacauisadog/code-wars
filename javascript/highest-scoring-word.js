// https://www.codewars.com/kata/highest-scoring-word/javascript

// Given a string of words, you need to find the highest scoring word.
// Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
// You need to return the highest scoring word as a string.
// If two words score the same, return the word that appears earliest in the original string.
// All letters will be lowercase and all inputs will be valid.



function high (x) {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz'
  let wordArray = x.split(' ')

  scoreArray = wordArray.map(word => {
    letterArray = word.split('')
    let sum = 0
    letterArray.forEach(letter => {
      sum += alphabet.indexOf(letter) + 1
    })
    return sum
  })

  highestScore = Math.max.apply(null, scoreArray)
  highestScoreIndex = scoreArray.indexOf(highestScore)
  return wordArray[highestScoreIndex]
}

// This was interesting. I learned about the `apply` method, and my understanding of it right now is that it sorta works like the * operator in python, where it destructures an array into its components (the `null` part is to set the `this` context, which I didn't need for this exercise)