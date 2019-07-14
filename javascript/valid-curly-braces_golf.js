areCurlyBracesMatchedProperly = s => {
  if (s.length === 0) return true
  else if (s.includes('{}')) return areCurlyBracesMatchedProperly(s.replace('{}', ''))
  else return false
}

// the above solution is mine. It works and I find it quite elegant and easy to understand, but the code golf demands it be less than 71 characters or it won't pass. I gave up trying to shorten it and instead forfeited my points to see the solutions. This number one solution below is so bizarre I don't even know why it works. Probably something to do with object syntax?

areCurlyBracesMatchedProperly = s => { try { s = eval(s) } catch (e) { } return !s }
