export default function updateUniqueItems(inputMap) {
  if (!(inputMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  const updatedMap = new Map();

  inputMap.forEach((value, key) => {
    updatedMap.set(key, value === 1 ? 100 : value);
  });

  return updatedMap;
}
