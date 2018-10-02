var expect = require('chai').expect;
var hero = require('../../src/8kyu/is-he-gonna-survive');

describe('hero', () => {

    it('should return false when the bullets do not divide equally into the number of dragons', () => {
        expect(hero(4, 5)).to.be.equal(false);
        expect(hero(7, 4)).to.be.equal(false);
        expect(hero(1500, 751)).to.be.equal(false);
        expect(hero(0, 1)).to.be.equal(false);
    });

    it('should return true when the bullets divide equally into the number of dragons', () => {
        expect(hero(10, 5)).to.be.equal(true);
        expect(hero(100, 40)).to.be.equal(true);
    });
});