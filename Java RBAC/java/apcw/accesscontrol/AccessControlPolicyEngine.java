package apcw.accesscontrol;

import apcw.user.User;
import apcw.user.Role;
import apcw.resource.Resource;
import apcw.resource.Action;
import apcw.resource.Scope;
import apcw.capability.CapabilityManager;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

//Access Control Policy Engine implementing RBAC.
public class AccessControlPolicyEngine {

    private final List<AccessLogEntry> logs = new ArrayList<>();
    private final CapabilityManager capabilityManager;

    public AccessControlPolicyEngine() {
        this.capabilityManager = new CapabilityManager();
    }

    public AccessDecision evaluateAccess(User user, Resource resource, Action action) {

        // Fail-safe behaviour: deny invalid requests
        if (user == null) {
            AccessDecision decision = new AccessDecision(false, "Access denied: user is null or unknown.");
            logs.add(new AccessLogEntry("unknown", null, resource, action, false));
            return decision;
        }

        if (resource == null) {
            AccessDecision decision = new AccessDecision(false, "Access denied: resource is null or unknown.");
            logs.add(new AccessLogEntry(user.getUserID(), user.getRole(), null, action, false));
            return decision;
        }

        if (action == null) {
            AccessDecision decision = new AccessDecision(false, "Access denied: action is null or unknown.");
            logs.add(new AccessLogEntry(user.getUserID(), user.getRole(), resource, null, false));
            return decision;
        }

        Role role = user.getRole();
        String resourceName = resource.getResourceName();
        Scope scope = resource.getScope();

        // Check capability using Java Generics
        if (!capabilityManager.hasCapability(role, action)) {
            String message = String.format("Access denied: %s does not have %s capability. %s",
                role.getDesc(), action, capabilityManager.getCapabilityDescription(role));
            logs.add(new AccessLogEntry(user.getUserID(), role, resource, action, false));
            return new AccessDecision(false, message);
        }

        boolean allowed = false;
        String message;

        // Check scope restrictions
        if (scope == Scope.CONFIDENTIAL && role != Role.ADMIN) {
            allowed = false;
            message = "Access denied: Only ADMIN can access CONFIDENTIAL resources.";
            logs.add(new AccessLogEntry(user.getUserID(), role, resource, action, allowed));
            return new AccessDecision(allowed, message);
        }

        // Role-based rules using if-else (since we can't switch on Resource class)
        if (role == Role.ADMIN) {
            // ADMIN permissions - full access to everything
            allowed = true;
            message = "Access granted: ADMIN full access to " + resourceName;
            
        } else if (role == Role.STAFF) {
            // STAFF permissions
            if (resourceName.contains("Exam")) {
                if (action == Action.WRITE) {
                    allowed = false;
                    message = "Access denied: STAFF cannot write Exam Papers";
                } else {
                    allowed = true;
                    message = "Access granted: STAFF can read Exam Papers";
                }
            } else if (resourceName.contains("Library") || resourceName.contains("Book")) {
                if (action == Action.READ) {
                    allowed = true;
                    message = "Access granted: STAFF can read Library Books";
                } else {
                    allowed = true;
                    message = "Access granted: STAFF can write Library Books";
                }
            } else if (resourceName.contains("Lecture") || resourceName.contains("Material")) {
                allowed = true;
                message = "Access granted: STAFF can " + action + " Lecture Materials";
            } else {
                allowed = true;
                message = "Access granted: STAFF can " + action + " " + resourceName;
            }
            
        } else if (role == Role.STUDENT) {
            // STUDENT permissions
            if (resourceName.contains("Exam")) {
                allowed = false;
                message = "Access denied: STUDENT cannot access Exam Papers";
            } else if (action == Action.WRITE) {
                allowed = false;
                message = "Access denied: STUDENT cannot write resources";
            } else {
                allowed = true;
                message = "Access granted: STUDENT can read " + resourceName;
            }
            
        } else {
            allowed = false;
            message = "Access denied: Unknown role";
        }

        logs.add(new AccessLogEntry(user.getUserID(), role, resource, action, allowed));
        return new AccessDecision(allowed, message);
    }

    // Returns read-only access logs
    public List<AccessLogEntry> getLogs() {
        return Collections.unmodifiableList(logs);
    }
}