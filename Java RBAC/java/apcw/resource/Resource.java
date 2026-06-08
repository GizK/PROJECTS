//implemented: fields, constructors and getters for resources
package apcw.resource;

//defining resource class
public class Resource {
	//constant attributes/ fields since the ID, name and scope doesnt change throughout the program
	private final String ResourceID;
	private final String ResourceName;
	private final Scope Scope;
	
	
	//constructors to initiate the objects
	public Resource(String ResourceID, String ResourceName, Scope Scope) {
		this.ResourceID = ResourceID;
		this.ResourceName = ResourceName;
		this.Scope = Scope;
	}
	
	//methods to return the id, name and scope of the resources
	public String getResourceID() {
		return ResourceID;
	}
	public String getResourceName() {
		return ResourceName;
	}
	
	public Scope getScope() {
		return Scope;
	}

 

}
