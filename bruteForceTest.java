
/**
 * Write a description of class bruteForceTest here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class bruteForceTest
{
    static void bruteForce(int lengthB, boolean uppercaseB, boolean lowercaseB, boolean symbolsB, boolean numbersB){
        //makes array
    char[] passwordArray = new char[lengthB];
    if (uppercaseB == true){
            for (int i=0; i<=lengthB-1; i++)
                passwordArray[i] = 'A';
    } 
    for (int p=65; p<=90; p++){
        for (int o=65; o<=90; o++){
            for (int n=65; n<=90; n++){
                for (int m=65; m<=90; m++){
                    for (int k=65; k<=90; k++){
                        for (int i=65; i<=90; i++){
                            passwordArray[lengthB-1] = (char)i;
                            System.out.println(passwordArray);
                        }
                        passwordArray[lengthB-2] = (char)k;
                    }
                    passwordArray[lengthB-3] = (char)m;
                }
                passwordArray[lengthB-4] = (char)n;
            }
            passwordArray[lengthB-5] = (char)o;
        }
        passwordArray[lengthB-6] = (char)p;
    }
}
}
