/**
 * @param {string} s
 * @return {number}
 */
var countAsterisks = s => s.split('|').map((seg, idx) => idx % 2 === 0 ? seg.split('*').length - 1 : 0).reduce((acc, val) => acc + val);

