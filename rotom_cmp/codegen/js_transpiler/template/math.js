function max(...elements) {
  return elements.reduce((prev, cur) => (prev > cur ? prev : cur));
}

function min(...elements) {
  return elements.reduce((prev, cur) => (prev < cur ? prev : cur));
}
