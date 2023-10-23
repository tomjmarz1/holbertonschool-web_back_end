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
    assert.equal(calcul.calculateNumber(1.2, 3.7), 5);
  });
  
  it('should return result of adding rounded numbers', function () {
    assert.equal(calcul.calculateNumber(1.5, 3.7), 6);
    assert.equal(calcul.calculateNumber(1.3, 0), 1);
    assert.equal(calcul.calculateNumber(0, 1.2), 1);
    assert.equal(calcul.calculateNumber(1.3, 1.3), 2);
    assert.equal(calcul.calculateNumber(1.7, 1.2), 3);
    assert.equal(calcul.calculateNumber(1.3, 1.8), 3);
    assert.equal(calcul.calculateNumber(1.6, 1.8), 4);
  });
});