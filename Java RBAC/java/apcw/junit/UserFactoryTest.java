package apcw.junit;

import apcw.designpatterns.UserFactory;
import apcw.user.User;
import apcw.user.Role;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

public class UserFactoryTest {
    
    @BeforeEach
    void setUp() {
        UserFactory.resetCounters();
    }  
    @Test
    void testCreateStudent() {
        User student1 = UserFactory.createStudent();
        User student2 = UserFactory.createStudent();       
        assertNotNull(student1);
        assertNotNull(student2);
        assertEquals(Role.STUDENT, student1.getRole());
        assertEquals(Role.STUDENT, student2.getRole());     
        assertEquals("STU001", student1.getUserID());
        assertEquals("STU002", student2.getUserID());
    }  
    @Test
    void testCreateStaff() {
        User staff1 = UserFactory.createStaff();
        User staff2 = UserFactory.createStaff();     
        assertNotNull(staff1);
        assertNotNull(staff2);
        assertEquals(Role.STAFF, staff1.getRole());
        assertEquals(Role.STAFF, staff2.getRole());   
        assertEquals("STF001", staff1.getUserID());
        assertEquals("STF002", staff2.getUserID());
    }
    @Test
    void testCreateAdmin() {
        User admin1 = UserFactory.createAdmin();
        User admin2 = UserFactory.createAdmin();     
        assertNotNull(admin1);
        assertNotNull(admin2);
        assertEquals(Role.ADMIN, admin1.getRole());
        assertEquals(Role.ADMIN, admin2.getRole());  
        assertEquals("ADM001", admin1.getUserID());
        assertEquals("ADM002", admin2.getUserID());
    }   
    @Test
    void testUniqueIDs() {
        User student = UserFactory.createStudent();
        User staff = UserFactory.createStaff();
        User admin = UserFactory.createAdmin();        
        assertNotEquals(student.getUserID(), staff.getUserID());
        assertNotEquals(student.getUserID(), admin.getUserID());
        assertNotEquals(staff.getUserID(), admin.getUserID());        
        assertTrue(student.getUserID().startsWith("STU"));
        assertTrue(staff.getUserID().startsWith("STF"));
        assertTrue(admin.getUserID().startsWith("ADM"));
    }   
    @Test
    void testSequentialIDs() {
        User s1 = UserFactory.createStudent();
        User s2 = UserFactory.createStudent();
        User s3 = UserFactory.createStudent();       
        assertEquals("STU001", s1.getUserID());
        assertEquals("STU002", s2.getUserID());
        assertEquals("STU003", s3.getUserID());
    }
}