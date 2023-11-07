
/**
 * Write a description of class CopyOfbruteForceTest here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.lang.*;
import java.util.*;
public class bruteForceTestB
{
    private int rowNumber = 0;
    public int rowOneFromEnd;
    public int[][] createTwoDeeArray(int lengthB, boolean uppercaseB, boolean lowercaseB, boolean symbolsB, boolean numbersB){
        //sets a number of rows for the 2d array
        int rowNumber = 1;
        if (uppercaseB){
            rowNumber += 26;    
        }
        if (lowercaseB){
            rowNumber += 26;
        }
        if (symbolsB){
            rowNumber += 32;
        }
        if (numbersB){
            rowNumber += 10;
        }
        int[][] myTwoDeeArray = new int[rowNumber][lengthB];
        //sets the values of the 2d array
        int currentRow = 0;
        if (symbolsB){
            for (int i=1; i<16; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+32;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }
        
        if (numbersB){
            for (int i=1; i<11; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+47;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }
        
        if (symbolsB){
            for (int i=1; i<8; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+57;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }

        if (uppercaseB){
            for (int i=1; i<27; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+64;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }
        
        if (symbolsB){
            for (int i=1; i<7; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+90;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }
        
        if (lowercaseB){
            for (int i=1; i<27; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+96;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }
        
        if (symbolsB){
            for (int i=1; i<5; i++){
                for (int k=0; k<lengthB; k++){
                    myTwoDeeArray[currentRow][k] = i+122;
                    System.out.println(Arrays.deepToString(myTwoDeeArray) + "\n");
                }
                currentRow += 1;
            }
        }
        rowOneFromEnd = currentRow;
        //(one row is left empty with zeroes, which will act as a reset row later)
        return myTwoDeeArray;
    }
    
    public int[] createOneDeeArray(int lengthB, int[][] twoD){
        //initializes 1d array length
        int myOneDeeArray[] = new int[lengthB];
        //sets values of 1d array based on 2d array
        for (int k=0; k<lengthB; k++){
            myOneDeeArray[k] = twoD[0][k];
        }
        return myOneDeeArray;
    }
    
    public void actualBruteForcing(int lengthB, int[][] twoD, int[] oneD){
        int rowOfRightmost = 0;
        //int rowStorer = 0;
        //initializes starting password and end password (where the program will stop brute forcing)
        String currentPassword = "";
        String endPassword = "";
        for (int k=0; k<lengthB; k++){
            currentPassword += oneD[k];
        }
        for (int k=0; k<lengthB; k++){
            endPassword += twoD[rowOneFromEnd-1][k];
        }
        //next three lines are for testing purposes
        System.out.println("starting password is: " + currentPassword);
        System.out.println("end password is: " + endPassword);
        System.out.println("one row from end: " + rowOneFromEnd);
        //prints starting password, program does not work if printed inside the while loop
        System.out.println("starting password is: " + currentPassword);
        //actual brute forcing MY LOGIC IS WROMNG SOMEWHERE HERE HELP
        while(!(currentPassword.equals(endPassword))){
            //System.out.println("Note: the current password (" + currentPassword + ") does NOT equal the end password (" + endPassword + ")");
            rowOfRightmost += 1;
            oneD[lengthB-1] = twoD[rowOfRightmost][lengthB-1];
            //checks if any value is 0, meaning that number must be reset and the digit to the left must be incremented
            for (int k=lengthB-1; k>=0; k--){
                if (oneD[k] == 0){
                    //calculates the row of the current value and sets the value to the next row
                    for (int i=0; i<rowOneFromEnd+1; i++){
                        if (oneD[k-1] == twoD[i][k-1]){
                            //rowStorer = i;
                            oneD[k-1] = twoD[i+1][k-1];
                            oneD[k] = twoD[0][k];
                            rowOfRightmost = 0;
                            break;
                        }
                    }
                    //don't think this code is necessary anymore but keeping just in case
                    //for (int i=k; i<lengthB; i++){
                      //  oneD[i-1] = twoD[rowStorer+1][i-1];
                    //}
                    //System.out.println("Test");
                    
                    //oneD[lengthB-1] = twoD[rowOfRightmost][lengthB-1];
                }
            }
            //prints current password, then goes to the next line (also updates current password variable
            currentPassword = "";
            for (int k=0; k<lengthB; k++){
                System.out.print((char)(oneD[k]));
                currentPassword += (oneD[k]);
            }
            System.out.print("\n");
            
        }
        System.out.println("Brute forcing complete"); 
    }
}
