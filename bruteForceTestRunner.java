
/**
 * Write a description of class bruteForceTest here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.lang.*;
import java.util.*;
public class bruteForceTestRunner
{
    public static void main(String[] args){
        //creates scanners and variables relating to password elements that will be used as arguments into a method later
        Scanner pref = new Scanner(System.in);
        bruteForceTest testRunner = new bruteForceTest();
        int passwordLength;
        boolean uppercaseA;
        boolean lowercaseA;
        boolean symbolsA;
        boolean numbersA;
        //asks users questions about password, giving values to the variables listed above
        System.out.println("How long is the password? (Enter integer 1-9) :: ");
        passwordLength = pref.nextInt();
        System.out.println("length = " + passwordLength);
        pref.nextLine();
        System.out.println("Does the password contain uppercase characters? (Enter true/false) :: ");
        uppercaseA = pref.nextBoolean();
        System.out.println("Does the password contain lowercase characters? (Enter true/false) :: ");
        lowercaseA = pref.nextBoolean();
        System.out.println("Does the password contain symbols (such as !, ?, >, ., etc.)? (Enter true/false) :: ");
        symbolsA = pref.nextBoolean();
        System.out.println("Does the password contain numbers? (Enter true/false) :: ");
        numbersA = pref.nextBoolean();
        //runs method with arguments
        testRunner.bruteForce(passwordLength, uppercaseA, lowercaseA, symbolsA, numbersA);
    }
}
