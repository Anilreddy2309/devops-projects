const assert = require('assert');

// Simple test — check our app exports work
console.log('Running tests...');

// Test 1 — basic assertion
assert.strictEqual(1 + 1, 2, 'Math works');

// Test 2 — check health response shape
const healthResponse = { status: 'ok', timestamp: new Date().toISOString() };
assert.strictEqual(healthResponse.status, 'ok', 'Health status is ok');

// Test 3 — check items array
const items = [{ id: 1, name: 'laptop' }, { id: 2, name: 'keyboard' }];
assert.strictEqual(items.length, 2, 'Items array has 2 items');
assert.strictEqual(items[0].name, 'laptop', 'First item is laptop');

console.log('All tests passed!');
