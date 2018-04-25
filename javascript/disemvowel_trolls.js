/*

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

*/

function disemvowel(str) {
  let vowels = "aeiouAEIOU".split('');
  let strSplit = str.split('');   
 
  for (let i=0; i<vowels.length; i++)
  {
    if ( strSplit.indexOf(vowels[i]) > -1 )
    {
      strSplit.splice(strSplit.indexOf(vowels[i]), 1);
      i--;   
    }  
  }
  
  return strSplit.join('');
}

str = "This website is for losers LOL!";

console.log(disemvowel(str));
console.log("teste");
