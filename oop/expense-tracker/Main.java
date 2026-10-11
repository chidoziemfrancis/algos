import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to our Expense Tracker System");
        System.out.println("1. Add expense");
        System.out.println("2. View all expenses");
        System.out.println("3. View specfic expense");
        System.out.println("4. Update expense");
        System.out.println("5. Delete expense");
        System.out.println("6. Search expense");
        System.out.println("7. Filter expense");
        System.out.println("8. Calculate Total Expenses: calculate the total amount spent.");
        System.out.println("9. View Category Summary: calculate total spending for each category.");
        System.out.println("10. View Expense Summary: display the number of expenses, total spending, average");
        System.out.println("11. Exit");


        //Enter Choice 

        System.out.println("Enter choice: ");
        int choice = scanner.nextInt();

        while (true){

            switch(choice) {
                case 1:
                    //Add expense 

                    break;
                    
                case 2:


            }
        }



    }
}