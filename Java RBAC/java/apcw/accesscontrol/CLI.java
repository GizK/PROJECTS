package apcw.accesscontrol;

import apcw.user.User;
import apcw.user.Role;
import apcw.resource.Resource;
import apcw.designpatterns.Logger;
import apcw.resource.Action;
import apcw.resource.Scope;
import java.util.Scanner;

public class CLI {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        AccessControlPolicyEngine engine = new AccessControlPolicyEngine();
        Logger logger = Logger.getInstance();

        boolean running = true;

        // Pre-define resources
        Resource libraryBooks = new Resource("R1", "Library Books", Scope.PUBLIC);
        Resource lectureMaterials = new Resource("R2", "Lecture Materials", Scope.INTERNAL);
        Resource examPapers = new Resource("R3", "Exam Papers", Scope.CONFIDENTIAL);

        while (running) {

            try {
                System.out.println("\n--- MENU ---");

                System.out.println("Select user:");
                System.out.println("1 - ADMIN");
                System.out.println("2 - STAFF");
                System.out.println("3 - STUDENT");

                if (!scanner.hasNextInt()) {
                    throw new IllegalArgumentException();
                }
                int userChoice = scanner.nextInt();

                User user;

                if (userChoice == 1) {
                    user = new User("ADM001", Role.ADMIN);
                } else if (userChoice == 2) {
                    user = new User("STF001", Role.STAFF);
                } else if (userChoice == 3) {
                    user = new User("STU001", Role.STUDENT);
                } else {
                    throw new IllegalArgumentException();
                }

                System.out.println("\nSelect resource:");
                System.out.println("1 - Library Books (PUBLIC)");
                System.out.println("2 - Lecture Materials (INTERNAL)");
                System.out.println("3 - Exam Paper (CONFIDENTIAL)");

                if (!scanner.hasNextInt()) {
                    throw new IllegalArgumentException();
                }
                int resourceChoice = scanner.nextInt();

                Resource resource;

                if (resourceChoice == 1) {
                    resource = libraryBooks;
                } else if (resourceChoice == 2) {
                    resource = lectureMaterials;
                } else if (resourceChoice == 3) {
                    resource = examPapers;
                } else {
                    throw new IllegalArgumentException();
                }

                System.out.println("\nSelect capability:");
                System.out.println("1 - READ");
                System.out.println("2 - WRITE");

                if (!scanner.hasNextInt()) {
                    throw new IllegalArgumentException();
                }
                int actionChoice = scanner.nextInt();

                Action action;

                if (actionChoice == 1) {
                    action = Action.READ;
                } else if (actionChoice == 2) {
                    action = Action.WRITE;
                } else {
                    throw new IllegalArgumentException();
                }

                // POLICY ENGINE
                AccessDecision decision = engine.evaluateAccess(user, resource, action);

                String result = decision.isGranted() ? "ALLOW" : "REFUSE";

                System.out.println("\nResult: " + result);
                System.out.println(decision.getMessage());

                Logger.LogEntry entry = new Logger.LogEntry(
                        user.getUserID(),
                        user.getRole(),
                        resource,
                        action,
                        decision.isGranted()
                );

                logger.log(entry);

                System.out.println("\nContinue? (1 = Yes, 0 = No)");

                if (!scanner.hasNextInt()) {
                    throw new IllegalArgumentException();
                }
                int cont = scanner.nextInt();

                if (cont == 0) {
                    running = false;
                }

            } catch (Exception e) {
                System.out.println("Invalid input. Please try again.");
                scanner.nextLine();
            }
        }

        System.out.println("\n--- LOG HISTORY ---");
        logger.printLogs();

        scanner.close();
    }
}