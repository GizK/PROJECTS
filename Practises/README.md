# Flask weather API [SimpleWeatherStaticAPI]
- This project is a simple RESTful API built using the Flask framework in Python. It provides weather information for a few predefined cities by responding with JSON data. Users can access the API using a web browser.
- Built using Flask, a lightweight Python web framework, supports GET requests to retrieve weather data, returns JSON responses using jsonify.
Handles invalid cities with a clear 404 error message, Offers a helpful home route with usage instructions, Can be run locally at http://127.0.0.1:5000/ in debug mode
- What I learnt: 
1. Web Application Development with Flask
   I learned how to set up a basic Flask application using Flask(__name__) and define URL routes with @app.route.
2. Working with JSON in Flask
   I used jsonify to convert Python dictionaries into valid JSON responses, which is essential for API development.
3. Dynamic Route Parameters
   I handled URL variables (like /weather/<city>) by extracting the city name from the URL and using it to query data.
4. Error Handling in APIs
   I implemented basic error handling to return a 404 Not Found response if the city was not present in the weather dictionary.
5. Debug Mode and Development Server
   I ran the app using app.run(debug=True), which enables hot-reloading and helpful error messages during development.
- Self-reflection: This project introduced me to the fundamentals of API development using Flask. It helped me understand how web applications communicate via HTTP, how routes and JSON responses work, and how to handle 
  dynamic URLS and errors. Even though the app was small, it gave me a practical understanding of how backend APIs serve data to clients. I now feel more confident building RESTful services and integrating Flask with 
  other tools or frontend applications.

# Linux outputs
- This project is a Linux shell-based interactive menu system written in Bash. It allows users to choose between multiple utility options such as displaying command help, performing calculations, word count operations on files, sorting content, and computing averages. It demonstrates modular scripting with defined functions and a looping menu interface.
- Displays a user-friendly interactive menu. Supports the following operations: Save help manual of a command to a file, perform word count on a file (with file existence check), perform arithmetic operations, display and sort a calendar file (normal or reverse order), and exit the program. Allows for: Reading and evaluating user input, 
calculating average of integers (fixed or dynamic count), conditional logic (if, case, for, while), file I/O and redirection, modular design with functions like option1(), option2(), etc., improving reusability and clarity.
- What I learnt: 
1. Interactive Shell Scripting
   I learned how to create a looping command-line menu with while true, read, and case, allowing for smooth user interaction.
2. Modular Function Design in Bash
   I used function definitions like option1(), option2(), etc., to organize and isolate specific logic, making the script clean and maintainable.
3. User Input and Conditional Logic
   I practiced reading user input, checking input values with if, and making branching decisions with case.
4. File Operations and Redirection
   I worked with file existence checks using [ -f filename ], output redirection using >, and sorting file contents using sort and sort -r.
5. Arithmetic Operations in Bash
   I calculated averages and evaluated expressions using $(()) and handled both fixed and variable numbers of inputs in loops.
6. Error Handling and User Feedback
   The script provides user-friendly feedback for invalid inputs or missing files, improving the user experience.
- Self-reflection: This project helped me build confidence in writing functional and interactive shell scripts. It reinforced the importance of modularity, input validation, and usability in scripting. By simulating a mini command-line utility suite, I got hands-on experience with common Linux tools (man, wc, sort) and Bash constructs like loops, conditionals, and string manipulation. I now feel more equipped to automate tasks and build robust CLI tools in Linux environments.

# HTML report webpage 
- This project is a styled weather report webpage created using HTML and internal CSS. It visually presents weather data (city, temperature, and condition) inside a styled container (div) on a colourful, readable 
   background.
- Built entirely with HTML and CSS, structured layout and class selectors, separated city name, temperature, and weather conditions. Visually styled using: custom background colours, box-shadow 
  effects, font styling (italic, bold, font size), responsive-friendly layout using inline-block and padding, commented code to improve readability and assist beginner learning.
- What I learnt: 
1. HTML Structure and Semantics
   I practiced the foundational structure of an HTML document and semantic tags
2. Internal CSS Styling
3. Class Selectors and CSS Properties
   I used dot-prefixed class selectors and applied various properties including: background-color, font-size, font-style, font-weight, box-shadow, padding and border-radius
4. Text Emphasis and Layout Techniques
   I made use of strong, inline-block, and text alignment to ensure clarity and emphasis on key weather details.
5. User Interface Design Basics
   I learned how to enhance readability through proper contrast, spacing, and visual grouping of information inside a styled container.
- Self-reflection: This project gave me a solid understanding of web design fundamentals, combining both semantic HTML and visual CSS styling. I learned how small design choices (like padding and box shadows) can 
  significantly enhance the user experience. Writing clean, commented HTML also improved my ability to document code for myself and others. This project helped me take a step forward from plain HTML content into 
   structured, styled web interfaces.

# Go weather lookup cli 
- This project is a command-line weather lookup tool written in Go. It allows the user to input a city name and returns the corresponding temperature and weather condition from a predefined map (acting as a mini 
  database). The output is formatted using JSON for readability and structure.
- Prompts user input from the command line, stores static weather data in a map[string]map[string]string, checks if the entered city exists in the map. 
If found: Displays city, temperature, and condition in JSON format. If not found: returns an error message as a JSON response. Uses: bufio.NewReader for input,
strings.TrimSpace() for input sanitisation, json.MarshalIndent() for pretty-printed JSON output.
- What I learnt: 
1. Basic Go Syntax and Structure
   I learned how to write a complete main() function, import packages, define maps, and interact with the Go runtime environment.
2. User Input Handling
   I used bufio.NewReader to read user input from the console and sanitise it using strings.TrimSpace() to remove unwanted newline or space characters.
3. Working with Maps in Go
   I created and accessed nested maps (map[string]map[string]string) to simulate a database of weather data.
4. JSON Marshalling in Go
   I practiced converting Go maps into JSON strings using json.MarshalIndent, which is useful for structured data output.
5. Conditional Logic and Error Handling
   I implemented safe key lookups with if value, exists := map[key]; exists { ... }, and returned custom JSON error messages when data wasn't found.
6. Code Commenting and Documentation
   I commented each line clearly to explain what every part of the program does, which helped me learn and reinforce Go's syntax and behaviour.
- Self-reflection: This project helped me build a foundational understanding of the Go programming language. From reading input to formatting structured JSON responses, I experienced how Go handles real-world tasks 
  like data parsing and string manipulation. I also realized how important it is to handle edge cases (like missing keys) and give clear, informative output. This project served as an excellent introduction to Go’s 
  type system, maps, and standard library, and has motivated me to explore building more advanced CLI tools and web servers in Go.

# Visual basic calculator 
- This console-based calculator allows users to perform basic arithmetic operations—addition, subtraction, multiplication, and division—between two numbers. It was developed in VB.NET using control structures and type 
  conversion techniques, reinforcing foundational programming concepts.
- Accepts two numbers as input from the console, supports operations, Includes error handling for division by zero, Uses a Select Case structure for operation selection, Displays results with formatted console output, 
  Waits for any key press to exit, creating a smooth user experience.
- What I learnt: 
1. Console Input and Output in Visual Basic
    I used Console.WriteLine and Console.ReadLine for user interaction and learned how to convert strings to numeric types (Convert.ToDouble).
2. Control Flow Using Select Case
   I practiced using Select Case to handle multiple branches based on the user's selected operation.
3. Data Type Conversion and Validation
   I gained experience converting user input into numerical types and ensuring values are usable in calculations.
4. Basic Arithmetic Logic
   I implemented addition, subtraction, multiplication, and safe division, including a check for division by zero.
5. User Interaction Handling
   The application provides a clean interface, guides the user through the process, and waits for a key press before closing (Console.ReadKey()).
- Self-reflection: This project helped reinforce foundational programming concepts using Visual Basic, such as input/output handling, conditional logic, and user experience considerations. While the logic was simple, 
  structuring it cleanly with clear prompts and validations provided a solid introduction to building interactive console applications. It also gave me more confidence working with typed variables and understanding how 
  Visual Basic handles operations.
