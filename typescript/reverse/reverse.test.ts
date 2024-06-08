import { reverseArray } from './reverse';

describe('reverseArray', () => {
  it('should reverse an array of numbers', () => {
    const numbers = [1, 2, 3, 4, 5];
    const reversed = reverseArray(numbers);
    expect(reversed).toEqual([5, 4, 3, 2, 1]);
  });

  it('should reverse an array of strings', () => {
    const strings = ['a', 'b', 'c', 'd', 'e'];
    const reversed = reverseArray(strings);
    expect(reversed).toEqual(['e', 'd', 'c', 'b', 'a']);
  });
});
