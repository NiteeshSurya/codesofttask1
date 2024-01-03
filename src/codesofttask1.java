import java.util.Random;
import java.util.Scanner;

public class codesofttask1
{
        public static void main(String[] args)
        {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Welcome to the Guess the Number game!");

        while (true) {

            int secretNumber = random.nextInt(100) + 1;

            // Additional details
            int attemptsLimit = 10;
            int attemptsTaken = 0;

            while (attemptsTaken < attemptsLimit) {
                // Step 2: Prompt the user to enter their guess
                System.out.print("Enter your guess (1-100): ");
                int userGuess = scanner.nextInt();

                // Step 3: Compare the user's guess and provide feedback
                if (userGuess == secretNumber) {
                    System.out.println("Congratulations! You guessed the correct number " + secretNumber + "!");
                    break;
                } else if (userGuess < secretNumber) {
                    System.out.println("Too low. Try again.");
                } else {
                    System.out.println("Too high. Try again.");
                }

                attemptsTaken++;
            }

            // Display the user's score
            if (attemptsTaken == attemptsLimit) {
                System.out.println("Sorry, you've reached the maximum attempts. The correct number was " + secretNumber + ".");
            } else {
                System.out.println("You guessed the number in " + (attemptsTaken + 1) + " attempts.");
            }

            // Ask if the user wants to play again
            System.out.print("Do you want to play again? (yes/no): ");
            String playAgain = scanner.next().toLowerCase();
            if (!playAgain.equals("yes")) {
                System.out.println("Thanks for playing! Goodbye.");
                break;
            }
        }

        scanner.close();
    }
}
