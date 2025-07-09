# PHP weather API 
- This project is an API that retrieves real time weather data and displays it in JSON format. I wanted this project to be solid for positions such as a full stack developer, DevOp or software engineer. 
- A RESTful API that fetches and displays real-time weather data, demonstrating: Backend PHP development with OpenWeatherMap integration, Frontend JavaScript for dynamic data display, Secure API key management and error handling.
- Requirement |	Implementation	                       |     Future Scaling
Build APIs	  | RESTful PHP backend with JSON responses| Add POST/PUT endpoints
Clean Code	  | Documented with Swagger-style comments |	PHPStan static analysis
Monitoring	  | Request logging to weather.log         |	Prometheus metrics
Internal Tools|	Basic city weather lookup              |	Team alert dashboard
CI/CD	        | Manual Git pushes	                     | GitHub Actions pipeline
Testing       |	Manual test endpoint (TESTCITY)	       | PHPUnit + Postman automation
BE. Architect.|	Layered (Router→Service→API Client)    |	Microservice split
- Technologies used: Backend: PHP 8.2, cURL, REST, Frontend: JavaScript Fetch API, CSS Grid, Security: Input sanitization, .env for keys, DevOps: Git version control, request logging
- What I learnt:
1. API Development: Third-party API integration (OpenWeatherMap), JSON data validation and error handling
2. Professional Practices: Inline API documentation, Environment-based configuration
3. Debugging: Log analysis for failed requests
- Future improvements: CI/CD pipelines, Enterprise features (internal tools and further event driven design) , integration POSTMAN testing and unit testing 
   
