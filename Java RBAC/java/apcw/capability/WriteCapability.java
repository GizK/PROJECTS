package apcw.capability;

import apcw.resource.Action;

// WriteCapability implements Capability<Action>

public class WriteCapability implements Capability<Action> {
    
    @Override
    public Action getOperationType() {
        return Action.WRITE;
    }
    
    @Override
    public boolean allows(Action operation) {
        return operation == Action.READ || operation == Action.WRITE;
    }
    
    @Override
    public String getDescription() {
        return "Read/Write: Can read and modify resources";
    }
    
    @Override
    public String toString() {
        return "Capability<WRITE>";
    }
}