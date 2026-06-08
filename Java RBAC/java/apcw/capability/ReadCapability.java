package apcw.capability;

import apcw.resource.Action;

// ReadCapability implements Capability<Action>
public class ReadCapability implements Capability<Action> { 
    
    @Override
    public Action getOperationType() {
        return Action.READ;
    }
    
    @Override
    public boolean allows(Action operation) {
        return operation == Action.READ;
    }
    
    @Override
    public String getDescription() {
        return "Read-only: Can only read resources, cannot modify them";
    }
    
    @Override
    public String toString() {
        return "Capability<READ>";
    }
}