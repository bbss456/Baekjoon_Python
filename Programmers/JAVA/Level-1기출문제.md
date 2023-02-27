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

>[키패드 누르기](https://school.programmers.co.kr/learn/courses/30/lessons/67256) 
###
```
import java.awt.*;
import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer ="";

        /* init */
        Point leftPoint = new Point();


        Point rightPoint = new Point();

        String[][] keypad = new String[4][3];

        Map<String,Point> keypadMap = new HashMap<>();

        int padheight = 0;
        int start = 0;

        while (padheight < 3) {
            int settingPointX = 0;
            int settingPointY = 0;

            if (padheight == 0) {
                start = 1;

            }

            if (padheight == 1) {
                start = 4;
                settingPointX=0;
                settingPointY=1;
            }

            if (padheight == 2) {
                start = 7;
                settingPointX=0;
                settingPointY=2;
            }

            for (int i=start; i < start+3; i++) {
                Point settingPoint = new Point(settingPointX, settingPointY);
                keypadMap.put(String.valueOf(i),settingPoint);
                settingPointX++;
            }
            padheight++;
        }

        leftPoint.x = 0;
        leftPoint.y = 3;
        rightPoint.x = 2;
        rightPoint.y = 3;

        keypadMap.put("*", new Point(0,3));
        keypadMap.put("0", new Point(1,3));
        keypadMap.put("#", new Point(2,3));

        StringBuffer stringBuffer = new StringBuffer();
        for (int number : numbers) {
           if (number == 1 || number == 4 || number ==7) {
               stringBuffer.append("L");
               Point tempLeftPad = keypadMap.get(String.valueOf(number));
               leftPoint.x = 0;
               leftPoint.y = tempLeftPad.y;
           }

            if (number == 3 || number == 6 || number == 9) {
                stringBuffer.append("R");
                Point tempRightPad = keypadMap.get(String.valueOf(number));
                rightPoint.x = 2;
                rightPoint.y = tempRightPad.y;
            }

            if (number == 2 || number == 5 || number == 8 || number == 0) {
                Point target = keypadMap.get(String.valueOf(number));
                int leftdistance = findtarget(leftPoint, target);
                int rightdistance = findtarget(rightPoint, target);

                if (leftdistance < rightdistance) {
                    stringBuffer.append("L");
                    leftPoint.x = target.x;
                    leftPoint.y = target.y;
                }
                else if (leftdistance > rightdistance) {
                    stringBuffer.append("R");
                    rightPoint.x = target.x;
                    rightPoint.y = target.y;
                }
                else if (leftdistance == rightdistance) {
                    if(hand.equals("right")) {
                        stringBuffer.append("R");
                        rightPoint.x = target.x;
                        rightPoint.y = target.y;
                    } else {
                        stringBuffer.append("L");
                        leftPoint.x = target.x;
                        leftPoint.y = target.y;
                    }
                }
            }
        }
        answer = stringBuffer.toString();
        System.out.println(answer);

        return answer;
    }

    public int findtarget (Point tempPoint, Point targetPoint) {

        int targetX = targetPoint.x;
        int targetY = targetPoint.y;

        int tempX = tempPoint.x;
        int tempY = tempPoint.y;

        int count = 0;
        while (tempX != targetX) {
            if (tempX < targetX) {
                tempX++;
            }
            else if (tempX > targetX) {
                tempX--;
            }
            count++;
        }

        while (tempY != targetY) {
            if (tempY < targetY) {
                tempY++;
            }
            else if (tempY > targetY) {
                tempY--;
            }
            count++;
        }

        return  count;
    }
}
```
>[신규 아이디 추천](https://school.programmers.co.kr/learn/courses/30/lessons/72410) 
###
```
import java.util.*;
class Solution {
       public String solution(String new_id) {

        /*1. 소문자 변환 */
        new_id = new_id.toLowerCase();

        String match = "[^0-9a-zA-Z._-]";
        /*2. 특수문자 제거 */
        new_id = new_id.replaceAll(match, "");

        /*3. 중복된 점 제거 */
        new_id = removeduplicationdot(new_id);

        /*4. 맨처음 맨뒤 점 제거 */
        new_id = removeFirstLast(new_id);

        /*5. 빈 문자열 제거 */
        if (new_id.equals("")) {
            new_id = "a";
        }
        /*6. 문자열 길이 16이상 */
        if (new_id.length() > 15) {
           new_id = new_id.substring(0,15);
           String dotCheck = String.valueOf(new_id.charAt(new_id.length()-1));
           if (dotCheck.equals(".")) {
              new_id = new_id.substring(0,14);
              System.out.println(new_id);
           }
        }
        /*7. new_id의 길이가 2자 이하라면 */

        if (new_id.length() <= 2) {
            while (new_id.length() <3) {
                new_id = new_id + String.valueOf(new_id.charAt(new_id.length()-1));
            }
        }

        System.out.println(new_id);
        String answer = new_id;
        return answer;
    }

    public String removeduplicationdot(String new_id) {
        Stack<String> stack = new Stack<>();
        stack.add(String.valueOf(new_id.charAt(0)));

        for (int i=1; i < new_id.length(); i++) {
            String Stacktop = stack.peek();
            String charID = String.valueOf(new_id.charAt(i));
            if (Stacktop.equals(".") && charID.equals(".") ) {

            } else {
                stack.add(charID);
            }
        }

        StringBuffer stringBuffer = new StringBuffer();

        for (int i=0; i < stack.size(); i++) {
            stringBuffer.append(stack.get(i));
        }

        return stringBuffer.toString();
    }

    public String removeFirstLast(String new_id) {

        String firstChar = String.valueOf(new_id.charAt(0));
        String lastChar = String.valueOf(new_id.charAt(new_id.length()-1));

        StringBuffer stringBuffer = new StringBuffer();

        if (firstChar.equals(".") && lastChar.equals(".")) {
            for (int i=1; i <new_id.length()-1; i++) {
                stringBuffer.append(String.valueOf(new_id.charAt(i)));
            }
            new_id = stringBuffer.toString();
        }

        else if (firstChar.equals(".")) {
            for (int i=1; i <new_id.length(); i++) {
                stringBuffer.append(String.valueOf(new_id.charAt(i)));
            }
            new_id = stringBuffer.toString();
        }

        else if (lastChar.equals(".")) {
            for (int i=0; i <new_id.length()-1; i++) {
                stringBuffer.append(String.valueOf(new_id.charAt(i)));
            }
            new_id = stringBuffer.toString();
        }
        return new_id;
    }

}
```
>[3진법](https://school.programmers.co.kr/learn/courses/30/lessons/68935) 
###
```
class Solution {
    public int solution(int number) {
        StringBuffer stringbuffer = new StringBuffer();
        int current = number;
        int N = 3;

        while(current > 0){
            if(current % N < 10){
                stringbuffer.append(current % N);
            } else {
                stringbuffer.append((char)(current % N - 10 + 'A'));
            }
            current /= N;
        }
       
      return Integer.parseInt(String.valueOf(stringbuffer),3);
    }
}
```
>[예산](https://school.programmers.co.kr/learn/courses/30/lessons/68935) 
###
```
import java.util.Arrays;

class Solution {
  public int solution(int[] d, int budget) {
      int answer = 0;

            int sum = 0;

        Arrays.sort(d);
        for (int i = 0; i < d.length; i++) {
            sum += d[i];
            if (sum <= budget) {
                answer++;
            } else {
                break;
            }
        }

      return answer;
  }
}
```
>[로또의 최고 순위와 최저 순위](https://school.programmers.co.kr/learn/courses/30/lessons/77484) 
###
```
import java.util.*;
class Solution {
     public int[] solution(int[] lottos, int[] win_nums) {

        /*맵 랭킹*/
        HashMap<Integer,Integer> rankMap = new HashMap<>();

        int rankCount = 6;
        for (int i=0; i <=6; i++) {
            if (i <1) {
                rankMap.put(i,rankCount);
            } else {
                rankMap.put(i,rankCount);
                rankCount--;
            }
        }

        ArrayList<Integer> arrayListMax = new ArrayList<>();
        ArrayList<Integer> arrayListMin = new ArrayList<>();

        for (int number : lottos) {
            if (number == 0) {
                arrayListMax.add(number);
            } else {
                for (int i=0; i <6; i++){
                    if (win_nums[i] == number) {
                        arrayListMin.add(number);
                        arrayListMax.add(number);
                    }
                }
            }
        }
        
        int[] answer = new int[2];

        answer[1] = rankMap.get(arrayListMin.size());
        answer[0] = rankMap.get(arrayListMax.size());
        
        return answer;
    }
}
```
>[다트 게임](https://school.programmers.co.kr/learn/courses/30/lessons/17682) 
###
```
import java.util.*;
class Solution {
     public int[] solution(int[] lottos, int[] win_nums) {

        /*맵 랭킹*/
        HashMap<Integer,Integer> rankMap = new HashMap<>();

        int rankCount = 6;
        for (int i=0; i <=6; i++) {
            if (i <1) {
                rankMap.put(i,rankCount);
            } else {
                rankMap.put(i,rankCount);
                rankCount--;
            }
        }

        ArrayList<Integer> arrayListMax = new ArrayList<>();
        ArrayList<Integer> arrayListMin = new ArrayList<>();

        for (int number : lottos) {
            if (number == 0) {
                arrayListMax.add(number);
            } else {
                for (int i=0; i <6; i++){
                    if (win_nums[i] == number) {
                        arrayListMin.add(number);
                        arrayListMax.add(number);
                    }
                }
            }
        }
        
        int[] answer = new int[2];

        answer[1] = rankMap.get(arrayListMin.size());
        answer[0] = rankMap.get(arrayListMax.size());
        
        return answer;
    }
}
```
>[1차 비밀지도](https://school.programmers.co.kr/learn/courses/30/lessons/17681) 
###
```
class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[][] map = new String[n][n];


        for (int i=0; i < n; i++) {
            String binaryString = Integer.toBinaryString(arr1[i]);
            binaryString=String.format("%1$" + n + "s", binaryString).replace(' ', '0');

            String binaryString2 = Integer.toBinaryString(arr2[i]);
            binaryString2=String.format("%1$" + n + "s", binaryString2).replace(' ', '0');

            for (int j=0; j < n; j++) {
                map[i][j] = "0";
                String number= String.valueOf(binaryString.charAt(j));
                if (number.equals("1")) {
                    map[i][j] = "#";
                }

                String number2 = String.valueOf(binaryString2.charAt(j));
                if (number2.equals("1")) {
                    map[i][j] = "#";
                }
            }
        }

        String[] answer = new String[n];
        for (int i=0; i < n; i++) {
            StringBuffer stringBuffer = new StringBuffer();
            for (int j=0; j < n; j++) {
                if(map[i][j].equals("#")) {
                    stringBuffer.append(map[i][j]);
                } else {
                    stringBuffer.append(" ");
                }
            }
            answer[i] = stringBuffer.toString();
        }

        return answer;
    }
}
```
>[숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301) 
###
```
import java.util.*;
class Solution {
     public int solution(String s) {
        Queue<String> queue = new LinkedList<>();
        StringBuffer stringBuffer = new StringBuffer();
        for (int i=0; i < s.length(); i++) {
            queue.add(String.valueOf(s.charAt(i)));
        }

        while (!queue.isEmpty()) {
            String que = queue.poll();
            switch (que) {
                case "z" :
                    stringBuffer.append(0);
                    queue.poll();
                    queue.poll();
                    queue.poll();
                    break;

                case "o" :
                    stringBuffer.append(1);
                    queue.poll();
                    queue.poll();
                    break;

                case "t" :
                    String nextChar = queue.poll();
                    if(nextChar.equals("w")) {
                        stringBuffer.append(2);
                        queue.poll();
                    } else {
                        stringBuffer.append(3);
                        queue.poll();
                        queue.poll();
                        queue.poll();
                    }
                    break;
                case "f" :
                    String nextChar2 = queue.poll();
                    if(nextChar2.equals("o")) {
                        stringBuffer.append(4);
                        queue.poll();
                        queue.poll();
                    } else {
                        stringBuffer.append(5);
                        queue.poll();
                        queue.poll();
                    }
                    break;
                case "s" :
                    String nextChar3 = queue.poll();
                    if(nextChar3.equals("i")) {
                        stringBuffer.append(6);
                        queue.poll();
                    } else {
                        stringBuffer.append(7);
                        queue.poll();
                        queue.poll();
                        queue.poll();
                    }
                    break;
                case "e" :
                    stringBuffer.append(8);
                    queue.poll();
                    queue.poll();
                    queue.poll();
                    queue.poll();
                    break;
                case "n" :
                    stringBuffer.append(9);
                    queue.poll();
                    queue.poll();
                    queue.poll();
                    break;
                default :
                    stringBuffer.append(que);
            }
        }

        System.out.println(stringBuffer.toString());

        int answer = Integer.valueOf(stringBuffer.toString());
        return answer;
    }
}
```
>[두개 뽑아서 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/68644) 
###
```
import java.util.*;
class Solution {
 public int[] solution(int[] numbers) {

        HashSet<Integer> set = new HashSet<>();

        for (int i=0; i<numbers.length; i++) {
            if(i == numbers.length) {
                break;
            }
            else {
                for(int j=i+1; j<numbers.length; j++){
                    int hap = numbers[i];
                    hap += numbers[j];
                    set.add(hap);
                }
            }
        }
        ArrayList<Integer> arrayList = new ArrayList<>(set);
        Collections.sort(arrayList);
        int[] answer = new int[arrayList.size()];
        for (int i=0; i < arrayList.size(); i++) {
            answer[i] = arrayList.get(i);
        }

        return answer;
    }
}
```