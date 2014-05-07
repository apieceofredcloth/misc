function fibo (n) {
    return n > 1 ? fibo(n - 1) + fibo(n - 2) : 1;
}
console.log(fibo(40));
