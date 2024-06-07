import java.util.Scanner;

public class pat {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        if (n % 2 == 0) {
            System.out.println("n must be an odd number.");
            return;
        }
        
        int stars = 1;
        int spaces = n / 2;
        
        // Upper half
        for (int i = 0; i < (n + 1) / 2; i++) {
            // Print spaces
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }
            // Print stars
            for (int j = 0; j < stars; j++) {
                System.out.print("*");
            }
            // Move to the next line
            System.out.println();
            spaces--;
            stars += 2;
        }
        
        // Lower half
        spaces = 1;
        stars = n - 2;
        for (int i = 0; i < n/2; i++) {
            // Print spaces
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }
            // Print stars
            for (int j = 0; j < stars; j++) {
                System.out.print("*");
            }
            // Move to the next line
            System.out.println();
            spaces++;
            stars -= 2;
        }
    }
}
