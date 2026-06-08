package apcw.junit;

import apcw.sampledata.SampleData;
import apcw.user.User;
import apcw.resource.Resource;
import apcw.resource.Scope;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SampleDataTest {
    
    @Test
    void testGetUsers() {
        User[] users = SampleData.getUsers();
        
        assertNotNull(users);
        assertEquals(3, users.length);       
        assertNotNull(users[0].getUserID());
        assertNotNull(users[1].getUserID());
        assertNotNull(users[2].getUserID());
    }   
    @Test
    void testGetResources() {
        Resource[] resources = SampleData.getResources();       
        assertNotNull(resources);
        assertEquals(3, resources.length);        
        assertEquals("Library Books", resources[0].getResourceName());
        assertEquals("Lecture Materials", resources[1].getResourceName());
        assertEquals("Exam Papers", resources[2].getResourceName());       
        assertEquals(Scope.PUBLIC, resources[0].getScope());
        assertEquals(Scope.INTERNAL, resources[1].getScope());
        assertEquals(Scope.CONFIDENTIAL, resources[2].getScope());
    }
}