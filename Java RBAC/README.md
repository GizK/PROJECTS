
This project implements a secure, extensible Role‑Based Access Control (RBAC) system in Java using design patterns, generics, and structured access‑evaluation logic. It includes capability modelling, policy evaluation, logging, fault‑tolerance rules, and comprehensive testing.

---

## **Project Features**
- Capability‑based access control using Java Generics  
- Role‑based decision logic for Admin, Staff, and Student  
- Singleton policy engine for consistent system‑wide decisions  
- Factory pattern for structured user creation  
- Access logging for auditability and traceability  
- Fault‑tolerant behaviour for invalid inputs and concurrent access conflicts  
- JUnit testing for correctness, robustness, and fail‑safe behaviour  

---

## **Project Description**
- Implements a capability system using `Capability<T>` with type‑safe generics to prevent invalid permission usage.  
- Uses design patterns (Singleton, Factory, Strategy‑like logic) to ensure modularity, maintainability, and consistency.  
- Defines clear RBAC rules for Admin, Staff, and Student roles with strict least‑privilege enforcement.  
- Includes access logging to track all decisions for auditing and compliance.  
- Implements fault‑tolerance rules such as null‑input handling and concurrent access conflict prevention.  
- Provides a full suite of tests validating permissions, denial logic, invalid input handling, and logging behaviour.  

---

## **Technologies & Methods Used**
- Java OOP principles  
- Java Generics for type‑safe capability modelling  
- Design patterns (Singleton, Factory, Strategy‑like logic)  
- Enum‑based role and resource modelling  
- JUnit testing  
- Access logging and fault‑tolerance mechanisms  

---

## **My Contribution**
- Contributed to capability modelling and RBAC logic justification  
- Helped design and explain the use of Java Generics in the capability system  
- Participated in writing and reviewing the design pattern justifications  
- Ensured clarity, structure, and correctness in the report  
- Provided conceptual reasoning for CVSS‑style fault‑tolerance rules and invalid‑input handling  
- Collaborated on testing strategy and documentation  

---

## **What I Learned**
- How Java Generics can enforce type‑safe capability systems  
- How design patterns improve structure, maintainability, and correctness  
- How RBAC systems enforce least‑privilege and prevent privilege escalation  
- How to design fail‑safe behaviour for invalid inputs and concurrent access  
- How to write meaningful unit tests for access control logic  
- How to justify design decisions using OOP principles and security reasoning  

---

## **Key Implementation Insights**
### **Generics**
- Capability system uses `Capability<T>` to enforce type‑safe permissions  
- Prevents misuse of capabilities and avoids reliance on enums or strings  

### **Design Patterns**
- Singleton ensures one consistent policy engine  
- Factory centralises user creation and ID formatting  
- Strategy‑like logic enables modular role‑based decision rules  

### **Testing**
- Validates Admin full access  
- Ensures Student restrictions are enforced  
- Confirms fail‑safe behaviour for null inputs  
- Verifies logging for all access attempts  

### **Fault Tolerance**
- Null‑input denial to prevent undefined behaviour  
- Logging enforcement for traceability  
- Concurrent access conflict handling to avoid inconsistent states  
