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
>[없는 숫자 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/86051) 
###
```
import java.util.ArrayList;
import java.util.List;

class Solution {
  public int solution(int[] numbers) {

        List<Integer> numberList = new ArrayList<>();

        for (int i=0; i < numbers.length; i++) {
            numberList.add(numbers[i]);
        }

        int answer=0;

        for (int i=0; i < 10; i++) {
            if(numberList.contains(i) != true) {
                answer += i;
            }
        }

        return answer;
    }
}
```
>[내적](https://school.programmers.co.kr/learn/courses/30/lessons/70128) 
###
```
class Solution {
    public int solution(int[] a, int[] b) {

        int len = a.length;
        int answer = 0;
        for (int i=0; i < len; i++) {
            int result = a[i] * b[i];
            answer += result;
        }
        return answer;
    }

}
```

>[성격 유형 검사하기](https://school.programmers.co.kr/learn/courses/30/lessons/118666) 
###
```
import java.util.HashMap;

class Solution {
 public String solution(String[] survey, int[] choices) {

        HashMap<String, Integer> surveyResult = new HashMap<>();

        String[] characteristic = {"RT", "CF", "JM", "AN"};

        for (int i=0; i < 4; i++) {
            String characteristicA =  characteristic[i].substring(0,1);
            String characteristicB =  characteristic[i].substring(1,2);

            surveyResult.put(characteristicA, 0);
            surveyResult.put(characteristicB, 0);
        }

        for (int i=0; i < survey.length; i++) {
            int score = choices[i]-4;
            if (score > 0) {
                score = surveyResult.get(survey[i].substring(1,2)) + score;
                surveyResult.put(survey[i].substring(1,2),score);
            } else {
                score = surveyResult.get(survey[i].substring(0,1)) + score*-1;
                surveyResult.put(survey[i].substring(0,1), score);
            }
        }
        StringBuffer stringBuffer = new StringBuffer();

        if (surveyResult.get("R") > surveyResult.get("T")) {
            stringBuffer.append("R");
        } else if (surveyResult.get("R") == surveyResult.get("T")) {
            stringBuffer.append(charCompareTo("R","T"));
        } else {
            stringBuffer.append("T");
        }

        if (surveyResult.get("C") > surveyResult.get("F")) {
            stringBuffer.append("C");
        } else if (surveyResult.get("C") == surveyResult.get("F")) {
            stringBuffer.append(charCompareTo("C","F"));
        } else {
            stringBuffer.append("F");
        }

        if (surveyResult.get("J") > surveyResult.get("M")) {
            stringBuffer.append("J");
        } else if (surveyResult.get("J") == surveyResult.get("M")) {
            stringBuffer.append(charCompareTo("J","M"));
        } else {
            stringBuffer.append("M");
        }

        if (surveyResult.get("A") > surveyResult.get("N")) {
            stringBuffer.append("A");
        } else if (surveyResult.get("A") == surveyResult.get("N")) {
            stringBuffer.append(charCompareTo("A","N"));
        } else {
            stringBuffer.append("N");
        }

        System.out.println(stringBuffer);

        String answer = stringBuffer.toString();
        return answer;
    }
    
        String charCompareTo(String first, String second) {
        if (first.compareTo(second)  < 0) {
            return first;
        } else {
            return second;
        }
    }
}
```
>[신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334) 
###
```
import java.util.*;

class Solution {
 public int[] solution(String[] id_list, String[] report, int k) {
        HashMap<String,Integer> reportCountMap = new HashMap<>();
        HashMap<String, Set>  reportMap = new HashMap<>();

        for (int i=0; i < id_list.length; i++) {
            reportCountMap.put(id_list[i],0);
            reportMap.put(id_list[i],new HashSet<String>());
        }

        for (int i=0; i < report.length; i++) {
            String reporter  =  report[i].split(" ")[0];
            String badPerson = report[i].split(" ")[1];

            HashSet<String> reportSet = (HashSet<String>) reportMap.get(reporter);
            reportSet.add(badPerson);
            reportMap.put(reporter, reportSet);
        }

        ArrayList<String> badPersonList = new ArrayList<>();
        for (Set value : reportMap.values()) {
            ArrayList<String> valueList = new ArrayList<>(value);
            badPersonList.addAll(valueList);
        }

        for (String badPerson :badPersonList) {
            int count = reportCountMap.get(badPerson) + 1;
            reportCountMap.put(badPerson, count);
        }
        badPersonList.clear();
        for (String id :id_list) {
            if (reportCountMap.get(id) < k) {
                reportCountMap.remove(id);
            }
            else {
                badPersonList.add(id);
            }
        }
        int[] answer = new int[id_list.length];
        int i=0;
        for (String id : id_list) {
            ArrayList<String> badPersonListcopy = new ArrayList<>(badPersonList);
            ArrayList<String> valueList = new ArrayList<>(reportMap.get(id));
            int tempCount = badPersonListcopy.size();
            badPersonListcopy.removeAll(valueList);
            int count  = tempCount - badPersonListcopy.size();
            answer[i] = count;
            i++;
        }

        return answer;
    }
}
```
>[약수의 개수와 덧셈](https://school.programmers.co.kr/learn/courses/30/lessons/77884) 
###
```
import java.util.*;
class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        Queue<Integer> numberQue = new LinkedList<>();
        for (int i=left; i <= right; i++) {
            numberQue.add(i);
        }

        HashMap<Integer,Integer> numberMap = new HashMap<>();
        while (numberQue.isEmpty() != true) {
           int num = numberQue.poll();
           int count = 0;
           for (int i=1; i <= num; i++) {
               if(num % i == 0) {
                   count++;
               }
           }
           numberMap.put(num, count);
        }
        for (Map.Entry<Integer,Integer> map : numberMap.entrySet()) {
            if(map.getValue() % 2 ==0) {
                answer += map.getKey();
            } else {
                answer -= map.getKey();
            }
        }
        System.out.println(answer);
        return answer;
    }
}
```
>[부족한 금액 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/82612) 
###
```
class Solution {
   public long solution(int price, int money, int count) {
        long pricehap = 0;
        long moneyhap = 0;
        for (int i=0; i < count; i++) {
            pricehap += price;
            moneyhap += pricehap;
        }
        long answer = 0;

        if (moneyhap > money) {
            answer = moneyhap - money;
        }
        
        return answer;
    }
}
```