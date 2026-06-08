package apcw.capability;


public interface Capability<T> {
    // Returns the type of operation this capability supports
    T getOperationType();
    
    // Checks if this capability allows a specific operation
    boolean allows(T operation);

    // Returns a description of this capability
    String getDescription();
}