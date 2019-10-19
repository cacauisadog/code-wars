// https://www.codewars.com/kata/get-the-middle-character/train/javascript
// You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

function getMiddle (s) {
  halfString = Math.floor(s.length / 2)

  return s.length % 2 === 0 ?
    s.slice(halfString - 1, halfString + 1) :
    s[halfString]
}

// No secret here. The half of a string is always the leftover from the length divided by 2, rounded down.