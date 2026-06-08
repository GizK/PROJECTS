package apcw.capability;

import apcw.user.Role;
import apcw.resource.Action;
import java.util.HashMap;
import java.util.Map;

public class CapabilityManager {
    
    private final Map<Role, Capability<Action>> roleCapabilities;
    
    public CapabilityManager() {
        roleCapabilities = new HashMap<>();
        initializeCapabilities();
    }
    
    private void initializeCapabilities() {
        roleCapabilities.put(Role.STUDENT, new ReadCapability());
        roleCapabilities.put(Role.STAFF, new WriteCapability());
        roleCapabilities.put(Role.ADMIN, new WriteCapability());
    }
    
    public boolean hasCapability(Role role, Action action) {
        Capability<Action> capability = roleCapabilities.get(role);
        if (capability == null) {
            return false;
        }
        return capability.allows(action);
    }
    
    public String getCapabilityDescription(Role role) {
        Capability<Action> capability = roleCapabilities.get(role);
        if (capability == null) {
            return "No capabilities assigned";
        }
        return capability.getDescription();
    }
    
    public String getCapabilityType(Role role) {
        Capability<Action> capability = roleCapabilities.get(role);
        if (capability == null) {
            return "NONE";
        }
        return capability.toString();
    }
}