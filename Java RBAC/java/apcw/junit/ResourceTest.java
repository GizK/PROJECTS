package apcw.junit;

import apcw.resource.Resource;
import apcw.resource.Scope;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ResourceTest {
    
    @Test
    void testResourceCreation() {
        Resource resource = new Resource("R001", "Library Books", Scope.PUBLIC);
        assertNotNull(resource);
        assertEquals("R001", resource.getResourceID());
        assertEquals("Library Books", resource.getResourceName());
        assertEquals(Scope.PUBLIC, resource.getScope());
    }
    
    @Test
    void testGetResourceID() {
        Resource resource = new Resource("R001", "Library Books", Scope.PUBLIC);
        assertEquals("R001", resource.getResourceID());       
        Resource resource2 = new Resource("R002", "Exam Papers", Scope.CONFIDENTIAL);
        assertEquals("R002", resource2.getResourceID());
    }
    
    @Test
    void testGetResourceName() {
        Resource resource = new Resource("R001", "Library Books", Scope.PUBLIC);
        assertEquals("Library Books", resource.getResourceName());  
        Resource resource2 = new Resource("R002", "Lecture Materials", Scope.INTERNAL);
        assertEquals("Lecture Materials", resource2.getResourceName());
    }
    
    @Test
    void testGetScope() {
        Resource publicRes = new Resource("R001", "Library Books", Scope.PUBLIC);
        assertEquals(Scope.PUBLIC, publicRes.getScope());    
        Resource internalRes = new Resource("R002", "Lecture Materials", Scope.INTERNAL);
        assertEquals(Scope.INTERNAL, internalRes.getScope());   
        Resource confidentialRes = new Resource("R003", "Exam Papers", Scope.CONFIDENTIAL);
        assertEquals(Scope.CONFIDENTIAL, confidentialRes.getScope());
    }
}