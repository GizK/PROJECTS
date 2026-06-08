package apcw.accesscontrol;

import apcw.user.Role;
import apcw.resource.Resource;
import apcw.resource.Action;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

//Represents a single line in the log
public class AccessLogEntry {

    private final LocalDateTime timestamp;
    private final String userId;
    private final Role role;
    private final Resource resource;
    private final Action action;
    private final boolean allowed;
    
    private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");

    public AccessLogEntry(String userId,
                          Role role,
                          Resource resource,
                          Action action,
                          boolean allowed) {

        this.timestamp = LocalDateTime.now();
        this.userId = userId;
        this.role = role;
        this.resource = resource;
        this.action = action;
        this.allowed = allowed;
    }

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

    @Override
    public String toString() {
        return String.format("%s, %s, %s, %s, %s, %s",
            timestamp.format(FORMATTER),
            userId,
            role != null ? role.getDesc().toUpperCase() : "UNKNOWN",
            resource != null ? resource.getResourceName() : "UNKNOWN",
            action != null ? action.name() : "UNKNOWN",
            allowed ? "ALLOW" : "REFUSE"
        );
    }
}