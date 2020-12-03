package main.cn.paul.guessnum;

import java.util.*;


/**
 * Created by lfp on 2020/11/18.
 * @author lfp
 * @version 1.1
 * @since 2020.11.18
 *
 */
public class GuessNumber {
    public static void main(String[] args){
        guessNumber();
    }

    public static void guessNumber(){
        int result;
        int guess_num = 0;
        int count = 0; //正常的猜测计数。
        int TIMES=10; // 正常猜测次数大于10次,提示多少次了。
        int illegal_count = 0; //非法猜测计数
        int illegal_TIMES = 10; //非法猜测大于10次时,提示,并退出游戏

        boolean SWITCH = true;  //正常与否的开关

        //Random x = new Random(100);
        result = (int) (Math.random()*1000+1); //生成100以内的整数


        System.out.println(" *------------------------------------*");
        System.out.println(" |我们来玩个游戏吧,猜一猜1-1000的整数 |\n |     我说一个数字,你来猜怎么样?     |");
        System.out.println(" *------------------------------------*");
        System.out.println("        .........          \n\n" + " 我想好了,请输入那个数字吧:");

            do {
                System.out.print(" ");
                Scanner num = new Scanner(System.in);

                try {

                    guess_num = num.nextInt();

                    count++;

                    if (count > TIMES) {
                        System.out.print(" 加油吧少年!都" + count + "次了!");
                    }

                    if (guess_num < result) {
                        System.out.println(" 你的数小了哦!@_@");
                    } else if (guess_num > result) {
                        System.out.println(" 你的数大了哦!&_&");
                    }else {
                        System.out.println("  \n ^_^ 哎哟! 恭喜你猜对了,正式的猜了" + count +"次!");
                        System.out.println("      你已经调皮了 " + illegal_count +" 次! ");
                        count = count+illegal_count; //输出所有次数的总和
                        System.out.println("      一共猜了" + count + "次!");

                        SWITCH = false; //如果猜对了结束游戏
                    }
                }catch (InputMismatchException e){
                    System.out.println(" " + RandomWisecrack() + ",请输入一个整数!");
                    illegal_count++;
                    if (illegal_count > illegal_TIMES) {
                        System.out.printf("\n %s,已经调皮" + illegal_count + "次了! 本次游戏结束,拜拜!\n",
                                RandomWisecrack());
                        System.out.printf(" 你仅认认真真的猜了 %d 次!\n\n", count);
                        break;
                    }
                }

            }while (SWITCH);

    }

    public static boolean isNumeric(String str){ //ascii 码值判断字符串是否为数字
        for(int i=str.length();--i>=0;){
            int chr=str.charAt(i);
            if(chr<48 || chr>57)
                return false;
        }
        return true;
    }

    public static String RandomWisecrack() {

        String[] wisecracks = {"不要调皮","小样","你是想造反么","认真点"
        ,"不像话","我生气了,哼","乖,好好玩嘛","我...","好啦,乖乖","哪有你这样的"
        ,"我陪你哈","你是在想Ta么","难道是走神了","好好想想","挤破脑袋猜","哈哈"
        ,"人生总有不如意的时候,好好享受这一刻吧","我待你如初恋,你却...","&#$……@@#$@!#!%&*"};

        int RandomIndex;
        //Random random = new  Random();
        RandomIndex = (int) (Math.random()* wisecracks.length);
        return wisecracks[RandomIndex];
    }

}

class StopWatchTimer {

    public static Date timer() {

        //todo 增加一个计时器,来计算猜了多长时间
        Timer x = new Timer("test");
        //x.schedule();
        return timer();
    }
}

class GameTimerTask extends TimerTask {

    @Override
    public void run() {

    }



}


