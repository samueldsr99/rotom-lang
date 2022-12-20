function range(left, right, step) {
  const result = [];
  for (; left < right; left += step) {
    result.push(left);
  }
  return result;
}

function list(size, initValue) {
  const result = [];
  for (let i = 0; i < size; i++) {
    result.push(initValue === undefined ? 0 : initValue);
  }
  return result;
}
