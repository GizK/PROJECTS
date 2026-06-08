package apcw.sampledata;

import apcw.user.User;
import apcw.resource.Resource;
import apcw.resource.Scope;
import apcw.designpatterns.UserFactory;

public class SampleData {
    
    public static User[] getUsers() {
        // Users with auto-generated IDs using Factory Pattern
        return new User[] { 
            UserFactory.createStudent(), // Auto-generates STU001
            UserFactory.createStaff(), // Auto-generates STF001
            UserFactory.createAdmin() // Auto-generates ADM001
        };
    }
    
    public static Resource[] getResources() { 
        // Your original 3 resources, hardcoded as you had them
        return new Resource[] { 
            new Resource("R1", "Library Books", Scope.PUBLIC),
            new Resource("R2", "Lecture Materials", Scope.INTERNAL),
            new Resource("R3", "Exam Papers", Scope.CONFIDENTIAL)
        };
    }
}