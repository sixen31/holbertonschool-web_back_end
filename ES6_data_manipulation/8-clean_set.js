export default function cleanSet(set, startString) {
  let myString = '';
  for (const value of set) {
    if (value.startsWith(startString)) {
      myString += `${value.slice(startString.length)}-`;
    }
  }
  return myString.replace(/-$/, '');
}
