package apcw.accesscontrol;

import apcw.user.Role;
import apcw.resource.Resource;
import apcw.resource.Action;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class LogEntry {

    private LocalDateTime timestamp;
    private String userId;
    private Role role;
    private Resource resource;
    private Action action;
    private boolean allowed;

    public LogEntry(String userId, Role role, Resource resource, Action action, boolean allowed) {
        this.timestamp = LocalDateTime.now();
        this.userId = userId;
        this.role = role;
        this.resource = resource;
        this.action = action;
        this.allowed = allowed;
    }

    @Override
    public String toString() {

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");

        String decision = allowed ? "ALLOW" : "REFUSE";

        return formatter.format(timestamp) + ", " +
               userId + ", " +
               (role != null ? role.getDesc().toUpperCase() : "UNKNOWN") + ", " +
               formatResource(resource) + ", " +
               (action != null ? action.name() : "UNKNOWN") + ", " +
               decision;
    }
    
    private String formatResource(Resource resource) {
        if (resource == null) {
            return "UNKNOWN";
        }
        // Use the resource's name since it's a class, not an enum
        String resourceName = resource.getResourceName();
        
        if (resourceName.contains("Library") || resourceName.contains("Book")) {
            return "Library Books";
        } else if (resourceName.contains("Lecture") || resourceName.contains("Material")) {
            return "Lecture Materials";
        } else if (resourceName.contains("Exam") || resourceName.contains("Paper")) {
            return "Exam Paper";
        }
        return resourceName;
    }
    
    // Getters (optional - useful for statistics)
    public LocalDateTime getTimestamp() {
        return timestamp;
    }
    
    public String getUserId() {
        return userId;
    }
    
    public Role getRole() {
        return role;
    }
    
    public Resource getResource() {
        return resource;
    }
    
    public Action getAction() {
        return action;
    }
    
    public boolean isAllowed() {
        return allowed;
    }
}