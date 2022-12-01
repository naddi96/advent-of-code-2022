import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

class Solution{

    public static List<Integer> loadfile(){
        Scanner myReader;
        List <Integer> li = new LinkedList<Integer>();

        try{
            File f = new File("input_1_2022.txt");
            
                myReader = new Scanner(f);
                while(myReader.hasNextLine()) {
                    String data = myReader.nextLine();
                    if (data != ""){
                        li.add(Integer.parseInt(data)) ;             
                     }else{
                        li.add(-1);
                     }
                    }
            
            } catch (NumberFormatException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }catch (FileNotFoundException e) {
            e.printStackTrace();
        
            }
            return li;
        }
    

    public static int solution1(List<Integer> input){
        int max=-10;
        int current=0;
        for (int el : input){
            if (el ==-1){
                current=0;
                continue;
            }
            current=current+el;
            max=Math.max(max, current);
            
        }
        return max;
    }


    public static int solution2(List<Integer> input){
        int max1=Integer.MIN_VALUE;
        int max2=Integer.MIN_VALUE;
        int max3=Integer.MIN_VALUE;
        int current=0;
        for (int el : input){
            if (el==-1){current=0; continue;}
            current=current+el;
            if (max1<current){
                max3=max2;
                max2=max1;
                max1=current;
                continue;
            }

            if (max2<current){
                max1=max2;
                max2=current;
                continue;
            }

            if (max3<current){
                max3=current;
                continue;
            }



        }
        return max1+max2+max3;


    }


    public static void main(String[] args) {

        List<Integer> li =loadfile();
        int a=solution1(li);
        a=solution2(li);
        System.out.println(a);

    }

}
