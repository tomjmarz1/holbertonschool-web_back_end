var calcul = require('./0-calcul')

var assert = require('assert');

describe('calculateNumber', function () {
  it('should return result of adding rounded ', function () {
    assert.equal(calcul.calculateNumber(1, 3), 4);
  });
  it('should return result of adding rounded numbers', function () {
    assert.equal(calcul.calculateNumber(1, 3.7), 5);
  });
  it('should return result of adding rounded numbers', function () {
    assert.equal(calcul.calculateNumber(1.0, 3.7), 5);
  });
  
  it('should return result of adding rounded numbers', function () {
    assert.equal(calcul.calculateNumber(1.5, 3.7), 6);
    
  });
  it('should work with very large values', function() {
    const result = calculateNumber(Number.MAX_SAFE_INTEGER, 0.4);
    assert.equal(result, Number.MAX_SAFE_INTEGER);
  });
});