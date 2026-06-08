package apcw.designpatterns;

import apcw.user.Role;
import apcw.resource.Resource;
import apcw.resource.Action;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

// Singleton Pattern - Centralized logging service

public class Logger {
    
    private static Logger instance;
    private List<LogEntry> logs;
    
    private Logger() {
        logs = new ArrayList<>();
    }
    
    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }
    
    public void log(LogEntry entry) {
        logs.add(entry);
    }
    
    public List<LogEntry> getLogs() {
        return logs;
    }
    
    public void printLogs() {
        System.out.println("\n" + "=".repeat(70));
        System.out.println("ACCESS LOG (DD-MM-YYYY HH:MM, userID, ROLE, Resource, ACTION, STATUS)");
        System.out.println("=".repeat(70));
        for (LogEntry entry : logs) {
            System.out.println(entry);
        }
    }
    
    public void clearLogs() {
        logs.clear();
    }
    
    // Inner class for log entries with required format
    public static class LogEntry {
        private final LocalDateTime timestamp;
        private final String userId;
        private final Role role;
        private final Resource resource;
        private final Action action;
        private final boolean allowed;
        private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm");
        
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
}