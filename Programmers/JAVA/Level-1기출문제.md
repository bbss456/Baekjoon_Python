# Level-1 기출문제
>[나머지가 1이 되는 수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/87389) 
###
```
class Solution {
 public int solution(int n) {

        int answer = 0;
        for (int i=1; i <n; i++) {
            if (n%i == 1) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}
```
>[음양 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/76501) 
###
```
class Solution {
  public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;

        for (int i=0; i < absolutes.length; i++) {
            if (signs[i]) {
                answer += absolutes[i];
            } else {
                answer -= absolutes[i];
            }
        }
        
        return answer;
    }
}
```