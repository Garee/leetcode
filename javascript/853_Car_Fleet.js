/**
 * 853. Car Fleet (Medium)
 *
 * There are n cars going to the same destination along a one-lane road.
 * The destination is target miles away.
 *
 * You are given two integer array position and speed, both of length n,
 * where position[i] is the position of the ith car and speed[i] is the
 * speed of the ith car (in miles per hour).
 *
 * A car can never pass another car ahead of it, but it can catch up to
 * it and drive bumper to bumper at the same speed. The faster car will
 * slow down to match the slower car's speed. The distance between these
 * two cars is ignored (i.e., they are assumed to have the same position).
 *
 * A car fleet is some non-empty set of cars driving at the same position
 * and same speed. Note that a single car is also a car fleet.
 *
 * If a car catches up to a car fleet right at the destination point, it
 * will still be considered as one car fleet.
 *
 * Return the number of car fleets that will arrive at the destination.
 *
 * Constraints
 *
 *   n == position.length == speed.length
 *   1 <= n <= 105
 *   0 < target <= 106
 *   0 <= position[i] < target
 *   All the values of position are unique.
 *   0 < speed[i] <= 106
 */

/**
 * Patterns: Stack
 * Time: O(nlogn) where n is len(position)
 * Space: O(n) where n is len(position)
 *
 * @param {number} target the target position to reach.
 * @param {number[]} position array of car positions.
 * @param {number[]} speed array of car speeds.
 * @return {number} the number of car fleets.
 */
var carFleet = function (target, position, speed) {
    const cars = position.map((p, i) => ({ pos: p, spe: speed[i] }));
    cars.sort((a, b) => a.pos - b.pos);

    const stack = [];
    for (let i = cars.length - 1; i > -1; i--) {
        const time = (target - cars[i].pos) / cars[i].spe;
        stack.push(time);

        if (
            stack.length > 1 &&
            stack[stack.length - 1] <= stack[stack.length - 2]
        ) {
            stack.pop();
        }
    }

    return stack.length;
};

test("example 1", () => {
    const target = 12;
    const position = [10, 8, 0, 5, 3];
    const speed = [2, 4, 1, 1, 3];
    const ans = carFleet(target, position, speed);
    expect(ans).toEqual(3);
});

test("example 2", () => {
    const target = 10;
    const position = [3];
    const speed = [3];
    const ans = carFleet(target, position, speed);
    expect(ans).toEqual(1);
});

test("example 3", () => {
    const target = 100;
    const position = [0, 2, 4];
    const speed = [4, 2, 1];
    const ans = carFleet(target, position, speed);
    expect(ans).toEqual(1);
});
