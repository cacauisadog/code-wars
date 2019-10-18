//  https://www.codewars.com/kata/iq-test/train/javascript

// Bob is preparing to pass IQ test.The most frequent task in this test is to find out which one of the given numbers differs from the others.Bob observed that one number usually differs from the others in evenness.Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

// !Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1(not 0)

function iqTest (numbers) {
  let evens = 0
  let odds = 0
  let numbersArray = numbers.split(' ')
  let evennessArray = numbersArray.map(n => n % 2 === 0)

  evennessArray.forEach(n => n ? evens++ : odds++)
  return evens > odds ? evennessArray.indexOf(false) + 1 : evennessArray.indexOf(true) + 1
}

/*
This one was a little harder than I'd like to admit (I'm currently really rusty :().
I tried a lot of fors, forEaches and stuff to try and count the amount of even numbers to match against the amount of odd numbers, but it was just really ugly. Then I thought: since there is only one condition and one differing element, why not generate another array, filled with booleans, and THEN count if I have more "trues" than "falses"? So that's what I did.
*/