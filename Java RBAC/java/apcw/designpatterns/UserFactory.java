package apcw.designpatterns;

import apcw.user.User;
import apcw.user.Role;

// factory Pattern - encapsulates object creation logic and automatically generates unique User IDs.
public class UserFactory {
    
    private static int studentCounter = 1;
    private static int staffCounter = 1;
    private static int adminCounter = 1;
    
    // creates a new student with auto generated ID
    public static User createStudent() {
        String userID = "STU" + String.format("%03d", studentCounter++);
        return new User(userID, Role.STUDENT);
    }
    
    // creates a new staff member with auto-generated ID
    public static User createStaff() {
        String userID = "STF" + String.format("%03d", staffCounter++);
        return new User(userID, Role.STAFF);
    }
    
    // creates a new admin with auto generated ID
    public static User createAdmin() {
        String userID = "ADM" + String.format("%03d", adminCounter++);
        return new User(userID, Role.ADMIN);
    }
    
    // reset counters
    public static void resetCounters() {
        studentCounter = 1;
        staffCounter = 1;
        adminCounter = 1;
    }
}