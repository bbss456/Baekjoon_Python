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
>[개인정보 수집 유효기간](https://school.programmers.co.kr/learn/courses/30/lessons/150370) 
###
```
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {

        HashMap<String,Integer> termsHash = new HashMap<>();

        SimpleDateFormat todayFormat = new SimpleDateFormat("yyyy.MM.dd");
        Date todayDate = null;

        try {
            todayDate = todayFormat.parse(today);
        } catch (ParseException e) {
            e.printStackTrace();
        }

        for (String term :terms) {
            String[] termArray =term.replace(" ",",").split(",");
            termsHash.put(termArray[0], Integer.valueOf(termArray[1]));
        }
        int count = 1;
        ArrayList<Integer> deleteList = new ArrayList<>();
        for (String privacie : privacies) {
            SimpleDateFormat sdfYMD = new SimpleDateFormat("yyyy.MM.dd");
            String[] privacieArray = privacie.replace(" ",",").split(",");
            Date date = null;
            try {
                date = sdfYMD.parse(privacieArray[0]);
            } catch (ParseException e) {
                e.printStackTrace();
            }

            Calendar cal = Calendar.getInstance();
            cal.setTime(date);
            cal.add(Calendar.MONTH, termsHash.get(privacieArray[1]));
            int day = Integer.valueOf(privacieArray[0].substring(privacieArray[0].lastIndexOf(".")+1, privacieArray[0].length()));

            if (day !=1) {
                cal.add(Calendar.DATE, -1);
            }
            else {
                cal.add(Calendar.MONTH, -1);
                cal.add(Calendar.DATE, +27);
            }

            if (sdfYMD.format(todayDate).compareTo(sdfYMD.format(cal.getTime())) > 0) {
                deleteList.add(count);
            }
            count++;
        }

        int[] answer = new int[deleteList.size()];
        for (int i=0; i < deleteList.size() ; i++) {
            answer[i] = deleteList.get(i);
        }
        return answer;
    }
}
```