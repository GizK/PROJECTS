package apcw.junit;

import apcw.user.User;
import apcw.user.Role;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UserTest {
    
    @Test
    void testUserCreation() {
        User user = new User("U001", Role.STUDENT);
        assertNotNull(user);
        assertEquals("U001", user.getUserID());
        assertEquals(Role.STUDENT, user.getRole());
    }   
    @Test
    void testGetUserId() {
        User user = new User("U001", Role.STUDENT);
        assertEquals("U001", user.getUserID());        
        User user2 = new User("U002", Role.ADMIN);
        assertEquals("U002", user2.getUserID());
    }    
    @Test
    void testGetRole() {
        User student = new User("S001", Role.STUDENT);
        assertEquals(Role.STUDENT, student.getRole());
        assertEquals("Student", student.getRole().getDesc());
        assertEquals(1, student.getRole().getLevel());       
        User staff = new User("T001", Role.STAFF);
        assertEquals(Role.STAFF, staff.getRole());
        assertEquals("Staff", staff.getRole().getDesc());
        assertEquals(2, staff.getRole().getLevel());      
        User admin = new User("A001", Role.ADMIN);
        assertEquals(Role.ADMIN, admin.getRole());
        assertEquals("Admin", admin.getRole().getDesc());
        assertEquals(3, admin.getRole().getLevel());
    }
}