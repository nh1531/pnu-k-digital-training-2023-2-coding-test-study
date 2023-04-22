function solution(n) {
  function fib(k){
      if (k <= 2) return 1;
      return fib(k-2) + fib(k-1);
  }
  return fib(n)%1234567;
}

// 혹시 Python이나 JavaScript에서 재귀 호출을 사용하셨나요?

// 🚨이런 문제가 있어
// 위 언어는 타 언어에 비해 최대 재귀 호출 깊이가 작습니다.

// 💡그럼 코드를 어떻게 바꾸면 좋나요?
// 방법 #1 재귀 호출 대신 반복문을 사용하기

// 재귀 호출 대신 for문을 사용해서 첫 번째, 두 번째, 세 번째, ..., n번째 피보나치 수를 순서대로 구해보세요.

// 이러한 풀이 방식을 동적 계획법(Dynamic Programming)이라고 합니다.

// 방법 #2 재귀 호출 깊이 제한 늘리기(Python에서만 동작)

// sys.setrecursionlimit() 함수를 이용하여 재귀 호출 깊이 제한을 조정할 수 있습니다. 실제 재귀 호출 깊이보다 여유 있게 할당하는 것을 추천합니다.


function solution(n) {
  now=0;
  preb= 1;
  prebb= 0;
  for (let i =2 ; i<=n; i++){
    now = (preb+ prebb)%1234567
    prebb = preb;
    preb = now;
  }
  return now
}
[0,1,1,2,3,5,8,13]

console.log(solution(
  5
))
  // 5

//   모든 단계에서 % 연산을 사용하여, 모든 연산에서 오버플로우가 일어나지 않게 만들어 주세요.

// 🔖TIP [나머지 연산의 성질]

// 나머지 연산은 다음과 같은 특징을 갖고 있습니다

// ( a + m ) % m = a % m

// ( (a % m) + ( b % m) ) % m = ( a + b ) % m 

// ( ( a % m) * ( b % m) ) % m = ( a * b) % m 