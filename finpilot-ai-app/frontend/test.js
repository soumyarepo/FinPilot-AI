const fs = require('fs');
const path = require('path');

console.log("Running real frontend test cases...");

// ---------- Test 1: Check source file ----------
const sourcePath = path.join(__dirname, 'public', 'index.html');

if (!fs.existsSync(sourcePath)) {
  console.log("❌ Test Failed: public/index.html not found");
  process.exit(1);
}

console.log("✅ Test 1 Passed: Source file exists");

// ---------- Test 2: Check content ----------
const content = fs.readFileSync(sourcePath, 'utf-8');

if (!content || content.length < 10) {
  console.log("❌ Test Failed: index.html is empty");
  process.exit(1);
}

console.log("✅ Test 2 Passed: File has content");

// ---------- Test 3: Check HTML structure ----------
if (!content.includes("<html") || !content.includes("</html>")) {
  console.log("❌ Test Failed: Invalid HTML structure");
  process.exit(1);
}

console.log("✅ Test 3 Passed: Valid HTML structure");

// ---------- Test 4: Check build output ----------
const distPath = path.join(__dirname, 'dist', 'index.html');

if (!fs.existsSync(distPath)) {
  console.log("❌ Test Failed: dist/index.html not created (build issue)");
  process.exit(1);
}

console.log("✅ Test 4 Passed: Build output exists");

// ---------- Final ----------
console.log("🎉 All tests passed successfully!");
process.exit(0);