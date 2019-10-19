// https://www.codewars.com/kata/is-this-a-triangle/train/javascript
// Implement a method that accepts 3 integer values a, b, c.The method should return true if a triangle can be built with the sides of given length and false in any other case.
// (In this case, all triangles must have surface greater than 0 to be accepted).

function isTriangle (a, b, c) {
  return (a + b > c && a + c > b && b + c > a)
}

// There really wasn't any challenge in this one. The sum of two sides must always be greater than the third.