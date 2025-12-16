// Hàm tính tổng hai số
function sumTwoNumbers(a, b) {
    return a + b;
}

// Nhập dữ liệu từ người dùng
const a = parseFloat(prompt("Nhập số a: "));
const b = parseFloat(prompt("Nhập số b: "));

// Tính tổng và hiển thị kết quả
const result = sumTwoNumbers(a, b);
console.log(`Tổng của ${a} và ${b} là: ${result}`);